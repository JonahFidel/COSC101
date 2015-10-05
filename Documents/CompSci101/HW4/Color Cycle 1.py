import image

img = image.load_from_file('crayons.png')
color_cycle = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):    # converts image through color cycling 
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        color_cycle.set_rgb(x, y, b, r, g)

image.save_to_file(color_cycle, 'color cycle.png')
image.display_images(img, color_cycle)
