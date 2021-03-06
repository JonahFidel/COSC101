import image

img = image.load_from_file('obama.png')
obamafy = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):     # obamafies the image 
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        if (r + g + b)/3 < 60:
            obamafy.set_rgb(x, y, 0, 51, 76)
        elif (r + g + b)/3 < 121:
            obamafy.set_rgb(x, y, 217,26,33)
        elif (r + g + b)/3 <= 182:
            obamafy.set_rgb(x, y, 112, 150, 158)
        else:
            obamafy.set_rgb(x, y, 252, 227, 166)
            
image.save_to_file(obamafy, 'obamafy.png')
image.display_images(img, obamafy)
