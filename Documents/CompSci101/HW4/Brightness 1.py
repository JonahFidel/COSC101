import image

# asks user for input
brightness_change = int(raw_input("Enter how much you want to change the brightness: "))

img = image.load_from_file('crayons.png')
brightness = image.copy_image(img)

w = img.width()
h = img.height()

for x in range(w):      # changes brightness by a factor determined by the user
    for y in range(h):
        r, g, b = img.get_rgb(x, y)
        brightness.set_rgb(x, y, max(min(r + brightness_change, 255), 0), max(min(g + brightness_change, 255), 0), max(min(b + brightness_change, 255), 0))

image.save_to_file(brightness, 'brightness.png')
image.display_images(img, brightness)
 
