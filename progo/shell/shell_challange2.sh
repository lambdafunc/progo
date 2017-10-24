for i in {1..99}
do
     [ $(($i%2)) -ne 0 ] && echo $i
done
