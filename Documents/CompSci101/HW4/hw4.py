# ----------------------------------------------------------
# HW 4
# ----------------------------------------------------------
# Please answer these questions after having completed the 
# entire assignment.
# ----------------------------------------------------------
# Name: Jonah Fidel  
# Hours spent in total: 4  
# Collaborators (if any):  
# Feedback: What was the hardest part of this assignment?
#   obamafy
# Feedback: Any suggestions for improving the assignment?	
#   great assignment
# ----------------------------------------------------------

import image

brightness_change = int(raw_input("Enter how much you want to change the brightness: ")) # establishes user input early on for a later image conversion

# -------------------------------
# 1.  Grayscale problem
# -------------------------------

img = image.load_from_file('crayons.png')
grayscale = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        grayscale.set_rgb(x, y, (r + g + b)/3, (r + g + b)/3, (r + g + b)/3)   # sets the grayscale value to the average of the red, green and blue values for each pixel
    

image.save_to_file(grayscale, 'grayscale.png')

print

# -------------------------------
# 2.  Color cycle problem
# -------------------------------

color_cycle = image.copy_image(img)

for x in range(w):
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        color_cycle.set_rgb(x, y, b, r, g)  # cycles the colors by replacing red with blue, green with red, and blue with green pigments for each pixel 

image.save_to_file(color_cycle, 'color cycle.png')

print

# -------------------------------
# 3.  Negatives
# -------------------------------

negative = image.copy_image(img)


for x in range(w):
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        negative.set_rgb(x, y, abs(r - 255), abs(g - 255), abs(b - 255)) # creates a negative image by taking the absolute color values for the pixels minus 255
    
image.save_to_file(negative, 'negative.png')

print

# -------------------------------
# 4.  Brightness
# -------------------------------

brightness = image.copy_image(img)

for x in range(w):
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        brightness.set_rgb(x, y, max(min(r + brightness_change, 255), 0), max(min(g + brightness_change, 255), 0), max(min(b + brightness_change, 255), 0))  # increases or decrease brightness by an increment previously entered by the user

image.save_to_file(brightness, 'brightness.png')

print

# -------------------------------
# 5.  Increase contrast
# -------------------------------

contrast = image.copy_image(img)



for x in range(w):
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        contrast.set_rgb(x, y, max(min(r + (r - 128)*2, 255), 0), max(min(g + (g - 128)*2, 255), 0) , max(min(b + (b - 128)*2, 255), 0))  # increases contrast by abs(128 - value)*2, unless the value is greater than 255 or less than 0  
    
image.save_to_file(contrast, 'contrast.png')

print


# -------------------------------
# 6.  Posterize
# -------------------------------

posterize = image.copy_image(img)

for x in range(w):
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        posterize.set_rgb(x, y, (r/32)*32, (g/32)*32, (b/32)*32)   # posterizes the image by dividing by 32, rounding to the nearest integer, and then multiplying by 32
    
image.save_to_file(posterize, 'posterize.png')

print

# -------------------------------
# 7.  Obamafy
# -------------------------------

imgtwo = image.load_from_file('obama.png')
obamafy = image.copy_image(imgtwo)

w = imgtwo.width()
h = imgtwo.height()

for x in range(w):
    for y in range(h):
        r, g, b = imgtwo.get_rgb(x, y)

        if (r + g + b)/3 < 60:                # if the grayscale value is less than 60, make the pixel dark blue 
            obamafy.set_rgb(x, y, 0, 51, 76)

        elif (r + g + b)/3 < 121:             # if the grayscale is 60 <= value < 121, make the pixel red
            obamafy.set_rgb(x, y, 217,26,33)

        elif (r + g + b)/3 <= 182:                # if the grayscale is 121 <= value < 182, make the pixel light blue
            obamafy.set_rgb(x, y, 112, 150, 158)

        else:                                       # if the grayscale value is greater than or equal to 182, make the pixel yellow
            obamafy.set_rgb(x, y, 252, 227, 166)
            
image.save_to_file(obamafy, 'obamafy.png')
# -------------------------------
# 8.  Challenge problem 
# -------------------------------


# -------------------------------
# Lastly, display everything.  One call
# to image.display_images will do it.  Just
# pass all your image objects as parameters
# to that function.
# -------------------------------
# image.display_images(  )

image.display_images(img, grayscale, color_cycle, negative)     # NOTE: the user must quit out of each set of images for the next set to be displayed
image.display_images(brightness, contrast, posterize)            
image.display_images(imgtwo, obamafy)

