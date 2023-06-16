#!/bin/bash

#SBATCH -J nwchem
#SBATCH -n 20
#SBATCH --mail-type=ALL
#SBATCH --mail-user=lijun.pan@tuwien.ac.at

module load nwchem openmpi3

#uids=`awk 'NR<3000  {print $2}' ../database/uid4charge0.dat`
uids=`awk '{print $1}' choicedxyz_mult1.dat`
for uid in $uids;do
  echo $uid
  python change_position.py  $uid 
done
