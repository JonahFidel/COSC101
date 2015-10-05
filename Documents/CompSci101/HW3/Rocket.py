scale = raw_input("Please enter a scale: ")

print
print
print

for tin in range(int(scale) * 2 - 1):
    print (((int(scale)) * 2 - 1) - int(tin)) * " " + (tin + 1) * "/" + "**" + (tin + 1) * "\\"
    tin = tin + 1

for tin in range(int(scale)):
    print "|" + (int(scale) - tin - 1) * "." + (tin + 1) * "/\\" + ((int(scale) + (int(scale)-2)) - (tin*2)) * "." + (tin + 1) * "/\\" + (int(scale) - tin - 1) * "." + "|" 
   
for tin in range(int(scale)):
    print "|" + tin * "." + (int(scale) - tin) * "\\/" + (tin*2) * "." + (int(scale) - tin) * "\\/" + tin * "." + "|"

print "+" + int(scale) * 2 * "=*" + "+" 
    

for tin in range(int(scale)):
    print "|" + tin * "." + (int(scale) - tin) * "\\/" + (tin*2) * "." + (int(scale) - tin) * "\\/" + tin * "." + "|"

for tin in range(int(scale)):
    print "|" + (int(scale) - tin - 1) * "." + (tin + 1) * "/\\" + ((int(scale) + (int(scale)-2)) - (tin*2)) * "." + (tin + 1) * "/\\" + (int(scale) - tin - 1) * "." + "|"

print "+" + int(scale) * 2 * "=*" + "+" 

for tin in range(int(scale) * 2 - 1):
    print (((int(scale)) * 2 - 1) - int(tin)) * " " + (tin + 1) * "/" + "**" + (tin + 1) * "\\"
    tin = tin + 1
