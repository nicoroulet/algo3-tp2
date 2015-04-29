#include "ciudad.h"

using namespace std;

Ciudad::Ciudad(vector<vector<int> > &c) {
	calles=c;
}

int Ciudad::calle(int i, int j, Ciudad::direccion d) {
	// i y j indexan desde 0
	// las direcciones U y D son pares, L y R son impares
	return calles[2 * i + (d + 1) & 1][j - d & 1];
}