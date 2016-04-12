import element_data as ed
import material_data as md

def dicsum(dic):
	sum =0
	for i in dic:
		sum = sum + dic[i]
	return sum



def nucl_abundance(key):
	"""returns A Z and atomic abundance of a key within matdict & kills the rob"""
	matdict = md.matlib_construct('matlib')
	eledict = ed.elelib_construct('elelib')
	answer_dict = {}	
	if key in matdict:
		matlib = matdict[key]
		atoms = matlib['fraction']
		answer_dict = {}
		N = {}
		A = {}
		N_total = {}
		for i in atoms:			
			wo = atoms[i][0]
			atom = atoms[i][1]
			element_data = eledict[i]
			molar  = element_data['mm']
			rho = element_data['rho']
			isos = element_data['iso']
			percent_abundance = 0 
			N[i] = {}
			A[i] = {}
			for j in isos:
				percent_abundance = j[1]
				A[i].update({j: element_data['Z']})
				N[i].update({j: float(rho)*float(wo)/100*float(percent_abundance)/float(molar)})			
			N_total[i] = dicsum(N[i])	
		io = {}
		for i in N:
			io[i] = {}
			for j in N[i]:
				io[i][j] = N[i][j]/N_total[i]
			
		for i in atoms:
			answer_dict[i] = {}
			for j in A[i]:
				answer_dict[i].update({i+str(j[0]): [A[i][j],j[0],io[i][j]]}) 
		return {key: answer_dict}
		
			
			
		
