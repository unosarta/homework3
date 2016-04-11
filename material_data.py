def mass_fraction(l,line,lines):

        pos = lines.index(l)
        frac_num =int(line[2])
        fracs = {}
        for i in range(frac_num):
                j = lines[pos+1+i].split()
                fracs.update({j[0]: j[1:]})
        return fracs

def mat_data(line):

        mat = {"rho": line[1]}
        return mat

def matlib_construct(file_name):

        file = open(file_name, "r+")

        lines = file.readlines()

        material_lib = {}

        for line in lines:
                l = line.split()
                if line[0].isalpha():

                        material_lib[l[0]] = mat_data(l)
                        material_lib[l[0]].update({"fraction": mass_fraction(line,l,lines)})
        return(material_lib)
