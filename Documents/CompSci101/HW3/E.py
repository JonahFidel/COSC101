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
