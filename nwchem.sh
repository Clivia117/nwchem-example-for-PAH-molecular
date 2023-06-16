#!/bin/bash

#SBATCH -J nwchem
#SBATCH -n 20

#you can change up script base on your calculator

uids=`awk 'NR<3000  {print $2}' uid4charge0.dat`

for uid in $uids ;do
  echo $uid
  python asenwchem_ef_opt.py  $uid 
done
