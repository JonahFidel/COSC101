import image

img = image.load_from_file('crayons.png')
posterize = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):      # posterizes the image
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        posterize.set_rgb(x, y, (r/32)*32, (g/32)*32, (b/32)*32)
    
image.save_to_file(posterize, 'posterize.png')
image.display_images(img, posterize)
