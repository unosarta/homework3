import element_data as ed

f = open("elelib.txt", "r+")
lines = f.readlines()

element_lib = {}

for l in lines:

        line = l.split()
        if line[0].isalpha():
                element_lib[line[0]] = ed.element_data(line)
                element_lib[line[0]].update({"iso": ed.isotopes(lines,l,line)})

print(element_lib)
