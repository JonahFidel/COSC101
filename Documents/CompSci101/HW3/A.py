import block_paint

scale = int(raw_input("What is the scale?"))

window = block_paint.new_grid(scale)

for tin in range(scale):
    tin = tin + 1
    window.paint(0, tin/2, 'red')
    window.paint(scale - 1, tin/2, 'red')
    window.paint(tin - 1, scale/2, 'red')
    window.paint(scale/2, scale - 1, 'red')
for tin in range(scale/2):
    window.paint(tin, scale/2 + 1 + tin, 'red')
    window.paint(tin + scale/2 + 1, scale - tin - 1, 'red')
    

window.end()
