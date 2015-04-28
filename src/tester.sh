for f in tests.tp2.ej1.v1.1/*.in
do 
echo "Testeando ${s%.*}..."
diff -Z <(./ej1 < tests.tp2.ej1.v1.1/${s%.*}.in) tests.tp2.ej1.v1.1/${s%.*}.out
done
