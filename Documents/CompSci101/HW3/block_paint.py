#!/usr/bin/env python

__author__ = "jsommers@colgate.edu"
__doc__ = '''
Simple library for painting blocks on a (by default, square) gridded window.  
'''

import sys
import Tkinter

class InvalidDimension(Exception):
    pass

class InvalidXValue(InvalidDimension):
    pass

class InvalidYValue(InvalidDimension):
    pass

class BlockPainter(Tkinter.Frame):
    '''
    The main graphical frame that wraps up the buttons and canvas for
    drawing the blocks on screen. 
    '''
    def __init__(self, scale):
        self.root = Tkinter.Tk()
        Tkinter.Frame.__init__(self, self.root)
        self.root.title('Block Painter')
        self.width = scale  # make a square
        self.height = scale
        self.pix_per_block = 20
        self._createWidgets()
        self.pack()

    def _createWidgets(self):
        self.quit = Tkinter.Button(self, text="Quit", command=self.quit)
        self.quit.pack(anchor="n",fill="x")

        self.canvas = Tkinter.Canvas(self)
        self.canvas["width"] = (self.width) * self.pix_per_block + 1
        self.canvas["height"] = (self.height) * self.pix_per_block + 1
        self.canvas["relief"] = 'raised'
        self.canvas.pack(anchor="s",fill="both",padx=10)
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        self.canvas.create_rectangle(0, 0,
                                     self.width*self.pix_per_block,
                                     self.width*self.pix_per_block)
        # grid lines
        for i in range(self.width+1):
            self.canvas.create_line(i*self.pix_per_block, 
                                    0,
                                    i*self.pix_per_block, 
                                    self.width*self.pix_per_block-1)
            self.canvas.create_line(0, 
                                    i*self.pix_per_block,
                                    self.width*self.pix_per_block-1,
                                    i*self.pix_per_block)


    def paint(self, x, y, color):
        '''Paint the block with coordinates (x,y) the given color.
        Raise an exception if x,y or color are invalid.'''
        if not (0 <= x < self.width):
            raise InvalidXValue("X dimension {} is invalid".format(x))
        if not (0 <= y < self.height):
            raise InvalidYValue("Y dimension {} is invalid".format(y))

        # make origin be at lower left
        y = self.height - y - 1

        self.canvas.create_rectangle(x*self.pix_per_block, y*self.pix_per_block, 
                                    (x+1)*self.pix_per_block, (y+1)*self.pix_per_block,
                                    fill=color)

    def end(self):
        self.root.mainloop()
        try:
            self.root.destroy()
        except:
            pass

def new_grid(scale):
    '''Make a new grid canvas, scale blocks wide and scale blocks high'''
    return BlockPainter(scale)


if __name__ == '__main__':
    print >>sys.stderr, '*' * 60
    print >>sys.stderr, '''
You should not run this file directly.  It should only be imported.
Try:

    import block_paint

at the top of your own script, then run your script from IDLE 
(not this one).
'''
    print >>sys.stderr, '*' * 60

