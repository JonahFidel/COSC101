import image

img = image.load_from_file('crayons.png')
negative = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):      # converts image to negative
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        negative.set_rgb(x, y, abs(r - 255), abs(g - 255), abs(b - 255))
    
image.save_to_file(negative, 'negative.png')
image.display_images(img, negative)
 
