def first_dictionary(file_name):
    file1 = open(file_name)
    dictionary = {}
    for line in file1:
        line = line.split()
        for word in line:
            if not word[-1].isalpha():
                word = word[:-1]
                word = word.lower()
                dictionary += word 
            else:
                word = word.lower()
                dictionary += word
    return dictionary

                

def count_words(file_name):
    new_dictionary = {}
    
