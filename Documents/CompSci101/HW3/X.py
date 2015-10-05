import block_paint

scale = int(raw_input("What is the scale?"))

window = block_paint.new_grid(scale)

for tin in range(scale):
    tin = tin + 1
    window.paint(scale-tin, scale-tin, 'red')
    window.paint(tin - 1, scale - tin, 'red')

window.end()
