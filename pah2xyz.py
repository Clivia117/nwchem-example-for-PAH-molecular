import json
from ase import Atoms
from ase.io import read, write

from pkg_resources import resource_filename
from amespahdbpythonsuite.amespahdb import AmesPAHdb


charge= 0
mag=2
q=charge
js=f'pahdball_charge{charge}.json'
"""
# Read the database.
xml = 'nasapahdb_all.xml'
pahdb = AmesPAHdb(filename=xml,
                      check=False, cache=False)

uids=pahdb.search(f"charge={charge}") #return udis
b=pahdb.getspeciesbyuid(uids)
print(f'numbers of selection: {len(uids)}')
exit(1)
#convert dict to json
print('building database')
spec=b.data
json_object = json.dumps(spec, separators=(',', ':')) #write to one line string
with open (js,'w') as f:
    f.write(json_object) #the json file for read structure to xyz file
print('done')
"""
with open (js) as f:
    data = json.load(f)
print(data['493']["symmetry"])
exit(1)

for uid in uids:
    pos=data[f'{uid}']["geometry"]
    formula=data[f'{uid}']["formula"]
    method = data[f'{uid}']['method']
    print(data['2298']['n_quartet'],data['2298']['n_quintet'],data['2298']['weight'])
    exit(1)
    print(f"uid: {uid} , {formula}")
    if '+' in formula or '-' in formula:
      formula=formula.replace(formula[-1], '')
    types=[]
    coords=[]
    for i in range(len(pos)):
        coord=[pos[i]["x"],pos[i]["y"],pos[i]["z"]]
        type=pos[i]["type"]
        types.append(int(type))
        coords.append(coord)
    atom=Atoms(positions=coords,numbers=types,info={'q':q})
    if method=='UB3LYP':
    	write(f'xyz_charge{charge}/mult2/{uid}.xyz',atom)
    	print(f'{uid} write to mult2')
    else: 	
        write(f'xyz_charge{charge}/mult1/{uid}.xyz',atom)
        print(f'{uid} write to mult1')
