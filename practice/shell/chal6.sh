read resp
if [ "$resp" = "Y" ] || [ "$resp" = "y" ]
then
    echo 'YES'
elif [ "$resp" = "N" ] || [ "$resp" = "n" ]
then
    echo 'NO'
fi
