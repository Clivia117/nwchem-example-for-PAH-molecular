#!/bin/bash

#SBATCH -J nwchem
#SBATCH -n 20
#SBATCH --mail-type=ALL
#SBATCH --mail-user=lijun.pan@tuwien.ac.at

module load nwchem openmpi3

#uids=`awk 'NR<3000  {print $2}' ../database/uid4charge0.dat`
uids=`awk '{print $1}' calc_dat/ef1.dat`
#for uid in 309 346 631 2602 2844 2946 2969 3055 3096 3145 4003 ;do
for uid in $uids ;do
  echo $uid
  python asenwchem_ef.py  $uid 
done
