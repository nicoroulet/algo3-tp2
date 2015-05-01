n3=300
reps=50
cant_tests=50

mkdir -p ../tests/stats
# ejercicio 3
rm -f ../tests/stats/ej3.stats
python genera_tests.py 3 $n3 $cant_tests
for test in ../tests/ej3/*.in
do
	echo "test $test"
	for i in {1..$reps}
	do
		cat $test | ../src/ej3 ../tests/stats/ej3.stats > /dev/null
	done
done
python graficar.py 3
