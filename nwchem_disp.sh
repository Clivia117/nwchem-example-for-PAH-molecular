#!/bin/bash

#SBATCH -J disp-ef
#SBATCH -n 20
#SBATCH --mail-type=ALL
#SBATCH --mail-user=lijun.pan@tuwien.ac.at

module load nwchem openmpi3

uids=`awk '{print $1}' calc_dat/ef14json_new.dat`

for uid in $uids 

do
echo $uid

for i in {0..7}
do
  echo  $uid-dis-$i 
  python asenwchem_ef_disp.py  $uid-dis-$i 
done

done

