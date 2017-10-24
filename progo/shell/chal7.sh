read x
read y
read z

if (( ("$x"=="$y") && ("$y"=="$z") && ("$x"=="$z") ))
then
    echo "EQUILATERAL"
elif (( ("$x"!="$y") && ("$y"!="$z") && ("$x"!="$z") ))
then
    echo "SCALENE"
else echo "ISOSCELES"
fi
