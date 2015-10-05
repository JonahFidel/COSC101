import block_paint

scale = int(raw_input("What is the scale?"))

window = block_paint.new_grid(scale)

for tin in range(0,scale,1):
    window.paint(0, tin, 'red')
    
for tin in range(0, scale/2 + 1, 1):
    window.paint(tin + 1, scale/2 + tin, 'red')
    window.paint(tin + 1, scale/2 - tin, 'red')
    
window.end()
