uids=`awk '{print $1}' ../database/uid4charge0_mult1.dat`

for uid in $uids

do

a=`awk 'NR<2  {print $0}' ../database/xyz_charge0/$uid.xyz` #read from xyz file

if [ $a -gt 40 -a $a -le 50 ] 
then
echo $uid $a >> choicedxyz_mult1.dat
fi

done


