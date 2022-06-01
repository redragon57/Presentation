#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "1) échantillon"
    echo "2) nombre de point"
    echo "3) taille d'incrémentation"
else
    javac Main.java
    java Main $1 $2 $3 0 > result.csv
    sed -i 's/,/./g' result.csv
    R CMD BATCH big2.r
    java Main $1 $2 150000 1 > result_ex7.csv
    sed -i 's/,/./g' result_ex7.csv
    R CMD BATCH big2_ex7.r
fi
