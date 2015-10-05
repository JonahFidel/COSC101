import image

img = image.load_from_file('crayons.png')
contrast = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):      # raises image contrast by a factor of 2 times the distance from 128
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        contrast.set_rgb(x, y, max(min(r + (r - 128)*2, 255), 0), max(min(g + (g - 128)*2, 255), 0) , max(min(b + (b - 128)*2, 255), 0))
    
image.save_to_file(contrast, 'contrast.png')
image.display_images(img, contrast)
