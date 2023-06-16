uids=`awk '{print $1}' ../database/uid4charge0_mult2.dat`

for uid in $uids

do

a=`awk 'NR<2  {print $0}' ../database/xyz_charge0/$uid.xyz`

if [ $a -gt 40 -a $a -le 50 ] 
then
echo $uid $a
fi

done


