all: ej1 ej2 ej3

ej1: ej1.cpp
	g++ -std=c++11 ej1.cpp -o ej1 

ej2: ej2.cpp ciudad.o
	g++ -std=c++11 -g ej2.cpp ciudad.o -o ej2

ej3: ej3.cpp
	g++ -std=c++11 ej3.cpp -o ej3 

ciudad.o: ciudad.h ciudad.cpp
	g++ -c ciudad.cpp -o ciudad.o

clean:
	rm -f ej1
	rm -f ej2
	rm -f ej3
	rm -f ciudad.o
