# nwchem-example-for-PAH-molecular
This is a example to calculate energy and forces and dipole moment of PAH molecular by NWchem base on ase code. the PAH molecular from [NASA PAH database](https://www.astrochemistry.org/pahdb/).
you need to install [NWchem](https://nwchemgit.github.io/Download.html?h=install) and [amespahdbpythonsuite](https://github.com/PAHdb/AmesPAHdbPythonSuite), here we only consider chagre=0, and `uid` is identification of molecular.

### 1 you can download [NASA PAH database](https://www.astrochemistry.org/pahdb/), get `*.xml` file, which conclude all pah molecular.
- running pah2xyz to change xml file to json file `pahdball_charge0.json`
- exzact xyz file from `pahdball_charge0.json` by running `pah2xyz.py`  
### To calculated energy and forces, noto: you need to choice different `mult` for nwchem based on symmetry of PAH molecular
- running `asenwchem_ef_opt.py` by `nwchem.sh`
### Add more data, producing more displacement structure from original xyz
- running `change_position.py` by `ch_pos.sh`
### calculate energy and forces of new data
- running `asenwchem_ef_disp.py` by `nwchem_disp.sh`
 

