#!/bin/bash

i="0"

while [ $i -lt 1000 ]
do
    sleep 0.5
    echo $i
    ./call.sh &
    i=$[$i+1]
done
