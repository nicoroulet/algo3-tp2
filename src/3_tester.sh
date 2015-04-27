NAMES="
001
002
003
004
005
006
007
008
009
010
011
012
013
014
015
016
017
018
019
020
021
022
023
024
025
026
027
028
029
030
031
032
033
034
035
036
037
038"

for f in $NAMES
do 
echo "Testeando $f..."
diff -Z -q <(./ej3 < tests.tp2.ej3.v1.1/$f.in | sed -n '1p' | awk '{print $1}') tests.tp2.ej3.v1.1/$f.out
done
