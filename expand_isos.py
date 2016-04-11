import material_data as md
import element_data as ed

def iso_abund(material, element_lib):

        N = {}
        for i in material['fraction']:
                for j in element_lib[i]["iso"]:
                        N.update({(i,j): material['rho']*material['fraction'][i][1]*j[1]*element_lib[i]['mm']})

        for i in N:
                N_tot = N_tot + N[i]

        ia = {}
        for i in N:
                ia.update({i:N[i]/N_tot})
        return ia

def read_through(material_lib, element_lib):

        f = md.matlib_construct(material_lib)
        mat_ia = {}
        for i in f:
                mat_ia.update({i: iso_abund(f[i], ed.elelib_construct(element_lib))})
        return mat_ia
