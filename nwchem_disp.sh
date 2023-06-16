#!/bin/bash

#SBATCH -J nwchem
#SBATCH -n 20

#you can change up script base on your calculator

uids=`awk '{print $1}' choicedxyz_mult1.dat`

for uid in $uids 

do
echo $uid

for i in {0..7}
do
  echo  $uid-dis-$i 
  python asenwchem_ef_disp.py  $uid-dis-$i 
done

done

