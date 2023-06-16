#!/bin/bash
#SBATCH -J nwchem
#SBATCH -n 20
#SBATCH --mail-type=ALL

#you can change the up script base on you calculator

uids=`awk '{print $1}' choicedxyz_mult1.dat`
for uid in $uids;do
  echo $uid
  python change_position.py  $uid 
done
