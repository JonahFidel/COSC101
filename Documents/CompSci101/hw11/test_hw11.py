
# ------------------------------------------------------------------------------
# COSC 101 
# Code for automatically checking student homework submission.
# 
# Students are NOT expected to read and understand this program.
# Instead, follow these instructions:
# 1. Place this program in the SAME folder as hw11.py
# 2. Open this program in IDLE
# 3. In IDLE, select Run -> Run module 
# 4. Read the error messages that are printed and revise
#    hw11.py accordingly.
# ------------------------------------------------------------------------------


# ========================================================================
# students should not modify this program or even read below this line
# ========================================================================
























import importlib
import inspect
import os
import sys
import traceback
import unittest

# ------------------------------------ 
# CLEANING 
# ------------------------------------ 
def is_comment(s):
    return len(s.strip()) > 0 and s.strip()[0] == '#'    

def is_indented(s):
    return len(s.lstrip()) < len(s)

def is_function_header(s):
    return len(s) >= 3 and s[:4] == 'def '

def is_import_statement(s):
    return s.startswith('import ') or s.startswith('from ')

def scrape_function_defs(infilename, outfilename):
    msg = '''
This tester only tests function definitions. 
Any code that is not in a function will be 
ignored for testing purposes.'''
    print msg
    inf = open(infilename)
    outf = open(outfilename, 'w')
    line_no = 1
    for line in inf:
        if is_indented(line) or is_function_header(line) or \
           is_import_statement(line):
           outf.write(line)
        elif is_comment(line):
            outf.write(line)
        else:
            print 'Line %d of %s will be ignored: %s' % (line_no, infilename, line.rstrip())
            outf.write('#' + line)
        line_no += 1
    inf.close()
    outf.close() 


# ------------------------------------ 
# PREPARATION 
# ------------------------------------ 

hw11 = None
TESTFILENAME = 'temporary_test_copy_of_hw11.py'

def pre_setup(modname):
    '''
    Load a student submission as the generic module hw11.
    Heaven forgive me for using a global variable :-(
    '''
    global hw11
    error_msg = '''
    Your code must be written in a file named %s 
    and be placed in the same folder as %s''' % (modname, 'test_hw11.py')
    try:
        assert os.path.exists(modname), error_msg
        scrape_function_defs(modname, TESTFILENAME)
        hw11 = importlib.import_module(TESTFILENAME.replace('.py', ''))
    except SyntaxError,e:
        # print >>sys.stderr, '\n\nSyntax error in student code:'

        if e.args[0].find('Non-ASCII character') > -1:
            print >>sys.stderr, '\n\nUnable to read student code!'
            print >>sys.stderr, 'There is a syntax error on line %d of %s.' % (e.lineno, modname)
            print >>sys.stderr, '''
The problem is that this line contains a non-ASCII character, 
most likely a curly quotation mark or something.  Try editing
this line in IDLE and then re-running this test program.

Alternatively, put the following line at the very top of %s:

# -*- coding: iso-8859-15 -*-
''' % (modname)
        sys.exit()
    except Exception,e:
        print >>sys.stderr, 'Error importing student code, unable to run tests:{}'.format(str(e))
        sys.exit()

# ------------------------------------ 
# TESTS
# ------------------------------------ 

def compare_unordered_lists(L1, L2):
    # return L1 == L2
    return type(L1) == type(L2) and sorted(L1) == sorted(L2)


class TestHomework11(unittest.TestCase):

    def check_existence(self, fname):
        self.assertTrue(hasattr(hw11, fname), 'Did not find function called %s' % fname)

    def check_example(self, statement_str, eq_tester=None):
        '''
        Expects statement_str to be a doc string example like this:

        """
        >>> x = 5
        >>> y = x + 3
        >>> y
        8
        """
        
        It does not support arbitrary code.  But rather, the format
        is a sequence of statements followed by a test expression (the 
        second to the last line) followed by the expected result (the
        very last line).

        eq_tester is a function that takes two arguments and returns True
        if the arguments are equal.  if eq_tester is None, then equality is used.
        '''
        if eq_tester is None:
            eq_tester = lambda x,y: x == y

        statements = [statement.lstrip() for statement in statement_str.strip().split('\n')]
        test_expression = statements[-2]
        expected_result = eval(statements[-1])
        del statements[-2:]

        executed_statements = []
        try:
            for statement in statements:
                executed_statements.append(statement)
                exec statement.replace('>>> ', '')
            executed_statements.append(test_expression)
            student_result = eval(test_expression.replace('>>> ', ''))
        except Exception,e:
            msg = "An error occurred:\n"
            formatted_lines = traceback.format_exc().splitlines()
            msg += '\n'.join(executed_statements + formatted_lines) 
            self.fail(msg)

        if not eq_tester(expected_result, student_result):
            msg = "Test failed:\n"
            msg += '\n'.join(executed_statements)
            msg += '\nExpected:\n'
            msg += '\t%r' % (expected_result)
            msg += '\nReceived:\n'
            msg += '\t%r' % (student_result)
            self.fail(msg)

    # todo: fix hw11.download_page ugliness
    # todo: fix stack trace show lines from test code
    def test_01_download_page(self):
        fname = 'download_page'
        self.check_existence(fname)
        test = '''
        >>> download_page = hw11.download_page  # this line needed for testing purposes only
        >>> pagename = 'a.html'
        >>> text = download_page(pagename)
        >>> 'The word "chocolate" entered the English language' in text
        True
        '''
        self.check_example(test)

    def test_02_extract_links(self):
        fname = 'extract_links'
        self.check_existence(fname)
        test = '''
        >>> extract_links = hw11.extract_links  # this line needed for testing purposes only
        >>> extract_links('hello<a href="a.html">bye</a>see<a href="b.html">ya</a>')
        ['a.html', 'b.html']
        '''
        self.check_example(test)

    def test_03_remove_tags(self):
        fname = 'remove_tags'
        self.check_existence(fname)
        test = '''
        >>> remove_tags = hw11.remove_tags  # this line needed for testing purposes only
        >>> remove_tags('A<b>B</b>C')
        'ABC'
        '''
        self.check_example(test)

    def test_04_normalize_word(self):
        fname = 'normalize_word'
        self.check_existence(fname)
        test = '''
        >>> normalize_word = hw11.normalize_word  # this line needed for testing purposes only
        >>> normalize_word("That's")
        'thats'
        '''
        self.check_example(test)

    def test_05_index_page(self):
        fname = 'index_page'
        self.check_existence(fname)
        test = '''
        >>> index_page = hw11.index_page  # this line needed for testing purposes only
        >>> myindex = {}
        >>> index_page('fake.html', '<b>I</b> HearT "CHOCOlate!" chocolate', myindex)
        >>> myindex['chocolate']
        ['fake.html']
        '''
        self.check_example(test)

    def test_06_crawl_web(self):
        fname = 'crawl_web'
        self.check_existence(fname)
        test = '''
        >>> crawl_web = hw11.crawl_web  # this line needed for testing purposes only
        >>> pagename = 'a.html'
        >>> myindex = {}
        >>> mywebgraph = {}
        >>> crawl_web(pagename, myindex, mywebgraph)
        >>> mywebgraph['j.html']
        ['i.html']
        '''
        self.check_example(test)

        test = '''
        >>> crawl_web = hw11.crawl_web  # this line needed for testing purposes only
        >>> pagename = 'a.html'
        >>> myindex = {}
        >>> mywebgraph = {}
        >>> crawl_web(pagename, myindex, mywebgraph)
        >>> 'chocolate' in myindex
        True
        '''
        self.check_example(test)

    def test_07_random_surfer(self):
        fname = 'random_surfer_simulation'
        self.check_existence(fname)
        test = '''
        >>> random_surfer_simulation = hw11.random_surfer_simulation  # this line needed for testing purposes only
        >>> pagename = 'a.html'
        >>> myindex = {}
        >>> mywebgraph = {'fake1.html':['fake2.html'], 'fake2.html':['fake3.html'], 'fake3.html':['fake1.html'], }
        >>> p = 0
        >>> num_simulations = 3
        >>> random_surfer_simulation(mywebgraph, p, num_simulations)
        {'fake1.html': 0.33, 'fake2.html': 0.33, 'fake3.html': 0.33}
        '''
        def dict_almost_equals(d1, d2):
            if type(d2) != type({}):
                return False
            if d1.keys() != d2.keys():
                return False
            for k in d1:
                if abs(d1[k] - d2[k]) > 0.01:
                    return False
            return True
        self.check_example(test, dict_almost_equals)

    def test_08_list_union(self):
        fname = 'list_union'
        self.check_existence(fname)
        test =     '''
        >>> list_union = hw11.list_union  # this line needed for testing purposes only
        >>> list_union(['a.html', 'c.html'], ['a.html', 'b.html'])
        ['a.html', 'b.html', 'c.html']
        '''
        self.check_example(test, compare_unordered_lists)

    def test_09_list_intersection(self):
        fname = 'list_intersection'
        self.check_existence(fname)
        test =     '''
        >>> list_intersection = hw11.list_intersection  # this line needed for testing purposes only
        >>> list_intersection(['a.html', 'c.html'], ['a.html', 'b.html'])
        ['a.html']
        '''
        self.check_example(test, compare_unordered_lists)

    def test_10_list_difference(self):
        fname = 'list_difference'
        self.check_existence(fname)
        test =     '''
        >>> list_difference = hw11.list_difference  # this line needed for testing purposes only
        >>> list_difference(['a.html', 'c.html'], ['a.html', 'b.html'])
        ['c.html']
        '''
        self.check_example(test, compare_unordered_lists)

    def test_11_get_query_hit(self):
        fname = 'get_query_hits'
        self.check_existence(fname)
        test = '''
        >>> get_query_hits = hw11.get_query_hits  # this line needed for testing purposes only
        >>> myindex = {'dog': ['fake.html', 'fake2.html']}
        >>> get_query_hits('dog', myindex)
        ['fake.html', 'fake2.html']
        '''
        self.check_example(test)

        test = '''
        >>> get_query_hits = hw11.get_query_hits  # this line needed for testing purposes only
        >>> myindex = {'dog': ['fake.html']}
        >>> get_query_hits('cat', myindex)
        []
        '''
        self.check_example(test)


    def test_12_process_query(self):
        fname = 'process_query'
        self.check_existence(fname)
        test = '''
        >>> process_query = hw11.process_query  # this line needed for testing purposes only
        >>> myindex = {'cat' : ['fake1.html','fake3.html'], 'dog' : ['fake1.html']}
        >>> process_query('AND CAT dOg!!', myindex)
        ['fake1.html']
        '''
        self.check_example(test)

    def check_docstring(self, fname, f):
        # f = getattr(hw11, fname)
        docstring = f.__doc__
        self.assertIsNotNone(docstring, 'Function %s missing docstring' % fname)
        self.assertTrue(len(docstring) > 0, 'Function %s missing docstring' % fname)
        # self.assertTrue(docstring.find('->') > -1, 'Docstring for function %s missing type contract' % fname)

    def test_100_docstrings(self):
        '''Tests docstrings, even docstrings for helper functions'''
        for fname, f in inspect.getmembers(hw11, inspect.isfunction):
            self.check_docstring(fname, f)


def print_test_results(tr):
    '''A hack of unittest to print (hopefully) more user friendly messages.
    '''
    for test_name, error_str in tr.errors:
        print >>sys.stderr, '='*80
        print >>sys.stderr, test_name
        print >>sys.stderr, '-'*80
        print >>sys.stderr, error_str
        print >>sys.stderr, '-'*80

    for test_name, error_str in tr.failures:
        print >>sys.stderr, '='*80
        print >>sys.stderr, test_name
        print >>sys.stderr, '-'*80
        idx = error_str.find('AssertionError: ')  # todo: fix this ugliness
        if idx > -1:
            idx += len('AssertionError: ')
        else:
            idx = 0
        print >>sys.stderr, error_str[idx:]
        print >>sys.stderr, '-'*80

    num_errors = len(tr.errors)
    num_failures = len(tr.failures)
    num_passed = tr.testsRun - (num_errors + num_failures)
    print "Ran %d tests.  %d passed, %d failed, and %d had unexpected errors" % (tr.testsRun, num_passed, num_failures, num_errors)
    if tr.wasSuccessful():
        print "All tests passed!  Remember that..."
        print "- Passing these tests does NOT mean your program is necessarily bug free!"
        print "- This program does not include tests for the functions print_ranked_results and search_engine."



def main():
    print '\n\nRunning tests:'
    print '~'*80
    # unittest.main(verbosity=2, exit=True, failfast=False)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHomework11)
    tr = unittest.TestResult()
    suite.run(tr)
    print_test_results(tr)
    if os.path.exists(TESTFILENAME):
        os.remove(TESTFILENAME)
    if os.path.exists(TESTFILENAME+'c'):
        os.remove(TESTFILENAME+'c')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        del sys.argv[1]
    else:
        filename = 'hw11.py'
    pre_setup(filename)
    main()

