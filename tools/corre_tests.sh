n1=50
n2=50
n3=200
cant_tests=50

mkdir -p ../tests/stats

#ejercicio 1
if [ $1 = 1 ]; then
	python genera_tests.py 1 $n1 $cant_tests
	echo $n1 $cant_tests > ../tests/stats/ej1_n.stats
	echo $n1 $cant_tests > ../tests/stats/ej1_km.stats
	echo $n1 $cant_tests > ../tests/stats/ej1_kb.stats
	for test in ../tests/ej1/n/*.in
	do
		echo "test $test"
		i=${test#*_}
		i=${i%.in}
		for _ in {1..20}
		do
			cat $test | ../src/ej1 ../tests/stats/ej1_n.stats /dev/null /dev/null $i > /dev/null
		done
	done

	for test in ../tests/ej1/km/*.in
	do
		echo "test $test"
		i=${test#*_}
		i=${i%.in}
		for _ in {1..20}
		do
			cat $test | ../src/ej1 /dev/null ../tests/stats/ej1_km.stats /dev/null $i > /dev/null
		done
	done

	for test in ../tests/ej1/kb/*.in
	do
		echo "test $test"
		i=${test#*_}
		i=${i%.in}
		for _ in {1..20}
		do
			cat $test | ../src/ej1 /dev/null /dev/null ../tests/stats/ej1_kb.stats $i > /dev/null
		done
	done

	python graficar.py 1
fi

#ejercicio 2
if [ $1 = 2 ]; then
	python genera_tests.py 2 $n2 $cant_tests
	echo $n2 $cant_tests > ../tests/stats/ej2_nm.stats
	echo $n2 $cant_tests > ../tests/stats/ej2_s.stats
	for test in ../tests/ej2/nm/*.in
	do
		echo "test $test"
		i=${test#*_}
		i=${i%.in}
		for _ in {1..20}
		do
			cat $test | ../src/ej2 ../tests/stats/ej2_nm.stats /dev/null $i > /dev/null
		done
	done

	for test in ../tests/ej2/s/*.in 
	do
		echo "test $test"
		i=${test#*_}
		i=${i%.in}
		for _ in {1..20}
		do
			cat $test | ../src/ej2 /dev/null ../tests/stats/ej2_s.stats $i > /dev/null
		done
	done
	python graficar.py 2
fi

# ejercicio 3
if [ $1 = 3 ]; then
	python genera_tests.py 3 $n3 $cant_tests
	echo $n3 $cant_tests > ../tests/stats/ej3.stats
	for test in ../tests/ej3/*.in
	do
		echo "test $test"
		i=${test#*_}
		i=${i%.in}
		for _ in {1..20}
		do
			cat $test | ../src/ej3 ../tests/stats/ej3.stats $i > /dev/null
		done
	done
	python graficar.py 3
fi