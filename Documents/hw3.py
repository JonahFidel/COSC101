# ----------------------------------------------------------
# HW 3
# ----------------------------------------------------------
# Please answer these questions after having completed the 
# entire assignment.
# ----------------------------------------------------------
# Name: Jonah Fidel  
# Hours spent in total: 5 
# Collaborators (if any): Alex Indick, lab tutors 
# Feedback: What was the hardest part of this assignment?
#   letter K and letter A 
# Feedback: Any suggestions for improving the assignment?	
#   Very good assignment. Fun to work on. Possibly include further hints for some of the harder letters such as A and K but other than that very fun assignment!
# ----------------------------------------------------------


print '''This is some example code for using the block_paint
library.  If the following import statement fails, you should
ensure that this file (hw3.py) appears in the same folder/directory
as the block_paint.py file.'''

import block_paint

# set an arbitrary scale; you should ask the user for the scale
scale = 13

# make a new window to draw in
window = block_paint.new_grid(scale)

# draw two vertical lines
for i in range(scale):
    window.paint(0, i, 'red')
    window.paint(scale-1, i, 'blue')

# all done drawing
window.end()

print
print
print

# RETRO FONT 'E'
# write your code for drawing the letter E here

import block_paint

scale = int(raw_input("What is the scale?"))

window = block_paint.new_grid(scale)

for tin in range(scale):
    tin = tin + 1
    window.paint(0, tin - 1, 'red')
    window.paint((scale - tin) * 2/3, 0, 'red')
    window.paint((scale - tin) * 2/3, scale - 1, 'red')
    window.paint((scale - tin) * 2/3, (scale - 1)/2, 'red')

window.end()

print
print
print

# RETRO FONT 'X'
# write your code for drawing the letter X here

import block_paint

scale = int(raw_input("What is the scale?"))

window = block_paint.new_grid(scale)

for tin in range(scale):
    tin = tin + 1
    window.paint(scale-tin, scale-tin, 'red')
    window.paint(tin - 1, scale - tin, 'red')

window.end()

print
print
print

# RETRO FONT 'K'
# write your code for drawing the letter K here

import block_paint

scale = int(raw_input("What is the scale?"))

window = block_paint.new_grid(scale)

for tin in range(0,scale,1):
    window.paint(0, tin, 'red')
    
for tin in range(0, scale/2 + 1, 1):
    window.paint(tin + 1, scale/2 + tin, 'red')
    window.paint(tin + 1, scale/2 - tin, 'red')
    
window.end()

print
print
print

# RETRO FONT 'A'
# write your code for drawing the letter A here

import block_paint

scale = int(raw_input("What is the scale?"))

window = block_paint.new_grid(scale)

for tin in range(scale):
    tin = tin + 1
    window.paint(0, tin/2, 'red')
    window.paint(scale - 1, tin/2, 'red')
    window.paint(tin - 1, scale/2, 'red')
    window.paint(scale/2, scale - 1, 'red')
for tin in range(scale/2):
    window.paint(tin, scale/2 + 1 + tin, 'red')
    window.paint(tin + scale/2 + 1, scale - tin - 1, 'red')
    

window.end()

print
print
print

# TEXT ART
# write your rocket text art program here

scale = raw_input("Please enter a scale: ")

print
print
print

for tin in range(int(scale) * 2 - 1):
    print (((int(scale)) * 2 - 1) - int(tin)) * " " + (tin + 1) * "/" + "**" + (tin + 1) * "\\"
    tin = tin + 1

for tin in range(int(scale)):
    print "|" + (int(scale) - tin - 1) * "." + (tin + 1) * "/\\" + ((int(scale) + (int(scale)-2)) - (tin*2)) * "." + (tin + 1) * "/\\" + (int(scale) - tin - 1) * "." + "|" 
   
for tin in range(int(scale)):
    print "|" + tin * "." + (int(scale) - tin) * "\\/" + (tin*2) * "." + (int(scale) - tin) * "\\/" + tin * "." + "|"

print "+" + int(scale) * 2 * "=*" + "+" 
    

for tin in range(int(scale)):
    print "|" + tin * "." + (int(scale) - tin) * "\\/" + (tin*2) * "." + (int(scale) - tin) * "\\/" + tin * "." + "|"

for tin in range(int(scale)):
    print "|" + (int(scale) - tin - 1) * "." + (tin + 1) * "/\\" + ((int(scale) + (int(scale)-2)) - (tin*2)) * "." + (tin + 1) * "/\\" + (int(scale) - tin - 1) * "." + "|"

print "+" + int(scale) * 2 * "=*" + "+" 

for tin in range(int(scale) * 2 - 1):
    print (((int(scale)) * 2 - 1) - int(tin)) * " " + (tin + 1) * "/" + "**" + (tin + 1) * "\\"
    tin = tin + 1

