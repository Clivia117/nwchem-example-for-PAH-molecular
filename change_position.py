import ase 
from ase.io import read, write
import numpy as np
from ase import Atoms
import sys 

uid=sys.argv[1]


atoms=read(f'../database/xyz_charge0/{uid}.xyz')

pos=atoms.positions
formula=atoms.symbols

#if 'O' in formula or 'N' in formula:
#	print(uid)
for i in range(8): #produce 10 random displacemnet
	dis=np.random.normal(0,0.03,size=pos.shape)
	new_pos =pos+dis

	atoms_dis =Atoms(formula,positions=new_pos)
	write(f'disp_xyz/mult1/{uid}-dis-{i}.xyz',atoms_dis)
