from ase.calculators.nwchem import NWChem
from ase.io import read, write
from amespahdbpythonsuite.amespahdb import AmesPAHdb
import json
import sys 

def calc_energy_forces(uid):
  calc= NWChem(label=f'pah-disp/{uid}/{uid}-ef',
			   dft=dict(xc='B3LYP',
               			    maxiter=2000,
				    convergence= {'energy': 1e-9,
                                                   'rabuck': 30,
                                                 },
				    tolerances='tight',
                                   # grid='xfine',
				  # mult=3,
              		          ),
			    	
                          task='gradient',
			  basis="4-31G",		
			  			
             			)
  return calc        


uid=sys.argv[1]
atoms=read(f'disp_xyz/mult1/{uid}.xyz') #read xyz file
atoms.calc = calc_energy_forces(uid)
e=atoms.get_potential_energy()
f=atoms.get_forces()

