# nwchem-example-for-PAH-molecular
This is a example to calculate energy and forces and dipole moment of PAH molecular by NWchem base on ase code. the PAH molecular from [NASA PAH database]{https://www.astrochemistry.org/pahdb/}.
you need to install [NWchem]{https://nwchemgit.github.io/Download.html?h=install} and [amespahdbpythonsuite]{https://github.com/PAHdb/AmesPAHdbPythonSuite} 

## 1 exzact xyz file from pahdball_charge0.json by runing pah2xyz.py  
you need to choice different `mult` for nwchem based on symmetry of PAH molecular
## 2 running asenwchem_ef_opt.py by nwchem.sh 
## 3 producing more displacement structure from original xyz
## 4 running asenwchem_ef_disp.py by nwchem_disp.sh
## 5 turn output *.nwo file to json, note that: you should divide them to two json file, one is only contain nwo from original xyz, the other one is contain nwo from diplacement xyz. 

