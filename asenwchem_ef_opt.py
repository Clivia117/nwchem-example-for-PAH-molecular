from ase.calculators.nwchem import NWChem
from ase.io import read, write
from amespahdbpythonsuite.amespahdb import AmesPAHdb
import json
import sys 


def calc_energy_forces(uid,mu):
  calc= NWChem(label=f'pah/{uid}/{uid}-ef',
			   dft=dict(xc='B3LYP',
               			    maxiter=2000,
				    convergence= {'energy': 1e-9,
								   'rabuck': 30,
                                                 },
				    tolerances='tight',
                                   # grid='xfine',
					mult=mu,
              		          ),
			    	
			   task='gradient',
			   basis="4-31G",
			  			
             			)
  return calc        


uid=sys.argv[1]
# import numpy as np
# data=np.loadtxt('calc_dat/choicedxyz_mult2.dat')
# print()
# uids=data[:,0]
# for uid in uids:
js=f'../database/pahdball_charge0.json'
with open (js) as f:
	data = json.load(f)
sym=data[f'{int(uid)}']["symmetry"]
sym=sym[0].split('-')
if '?' in sym:
	sym=[1]
mu=sym[0]

atoms=read(f'../database/xyz_charge0/{uid}.xyz') #read xyz file
atoms.calc = calc_energy_forces(uid,mu)
e=atoms.get_potential_energy()
f=atoms.get_forces()

