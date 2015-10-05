# Jonah Fidel
# 11/19/13
# CompSci 101
# Lab 10: Recursion

import turtle
import math

# Problem 1

def print_digits(integer):
    '''(int) -> None
    This function prints out the digits of a number in English. The function
    simply prints the number and does not return anything. 
    '''
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if integer <= 9:
        print numbers[integer],
    if integer > 9:
        rest_of_integer = integer/10
        print_digits(rest_of_integer)   # Having faith 
        print numbers[integer%10],

# Problem 2

def sierpinski(turtle, lower_left_x, lower_left_y, length):
    '''(turtle, int, int, int) -> None
    This function draws a sierpinski triangle by drawing a main triangle and calling itself three
    separate times to draw the rest of the inscribed triangles. 
    '''
    height = (math.sqrt(3)/2) * length
    if length < 10:
        return
    else:
        turtle.up()
        turtle.goto(lower_left_x, lower_left_y)
        turtle.down()
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
        sierpinski(turtle, lower_left_x, lower_left_y, length/2)                  # accounts for triangles within triangles 
        sierpinski(turtle, (lower_left_x + (length/2)), lower_left_y, length/2)
        sierpinski(turtle, (lower_left_x + (length/4)), (lower_left_y + height/2), length/2)

def main(size):
    '''
    (int) -> None
    This function establishes the turtle module and calls the sierpinski function for a window of width
    'size.' 
    '''
    joey = turtle.Turtle()
    turtle.setup(size, size)
    lower_left_x = 0
    lower_left_y = 0
    length = 400
    turtle.setworldcoordinates(lower_left_x, lower_left_y, size, size)
    joey.speed(0)
    sierpinski(joey, lower_left_x, lower_left_y, length)
    turtle.done()
main(600)
    
        
    

