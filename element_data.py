def isotopes(lines,l,line):
        isos = []
        pos = lines.index(l)
        iso_num = int(line[4])
        for i in range(iso_num):
                isos.append(tuple(lines[pos+1+i].split()))
        return isos

def element_data(line):

        ele = {"mm": line[1], "Z": line[2], "rho": line[3]}
        return ele

def elelib_construct(file_name):

        f = open(file_name, "r+")
        lines = f.readlines()

        element_lib = {}

        for l in lines:

                line = l.split()
                if line[0].isalpha():
                        element_lib[line[0]] = element_data(line)
                        element_lib[line[0]].update({"iso": isotopes(lines,l,line)})
        return element_lib
