from ase.io.nwchem import read_nwchem_out
from ase.db import connect
import os

outname=f'dir_what_you_want_to_save/anyname_you_want.json'
inputfile='dir_of_nwo'
db = connect(outname)
if os.path.exists(outname):
	os.remove(outname)
i=0
for root,dirs,files in os.walk(inputfile):
    for file in files:
        if 'Job information' in file:
            continue
        else:
            #print(file)
            with open(os.path.join(inputfile,file),'r') as f:
                contents = f.read()
               # if 'Dipole Moment'  in contents:
                if 'DFT ENERGY GRADIENTS'  in contents: # DFT ENERGY GRADIENTS #'Dipole Moment'
                    r=True
                    print(f'{file} is {r}')
                else:
                    r=False
                    print(f'{file} is {r}')
                if r==True:
                    i+=1
                    data = read_nwchem_out(open(os.path.join(inputfile,file),'r'))
                    db.write(data)



