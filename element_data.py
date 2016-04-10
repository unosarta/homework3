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
