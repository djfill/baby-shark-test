#!/bin/bash
while read line
do
   jpg=`echo ${line} | cut -d ',' -f3`
   no=`echo ${line} | cut -d ',' -f1`
   mv ~/baby-shark-test/assets/${no}/* ~/baby-shark-test/assets/${no}/${jpg}
done < baby-sharks.csv
