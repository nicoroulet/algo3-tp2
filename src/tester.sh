for f in tests.tp2.ej1.v1.1/*.in
do 
echo "Testeando ${f%.*}..."
diff -Z <(./ej1 < tests.tp2.ej1.v1.1/${f%.*}.in) tests.tp2.ej1.v1.1/${f%.*}.out
done
