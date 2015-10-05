import image

img = image.load_from_file('crayons.png')
grayscale = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):       # converts image to grayscale
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        grayscale.set_rgb(x, y, (r + g + b)/3, (r + g + b)/3, (r + g + b)/3)
    

image.save_to_file(grayscale, 'grayscale.png')
image.display_images(img, grayscale)
