#include "ciudad.h"
#include <climits>
using namespace std;

Ciudad::Ciudad(vector<vector<int> > &c) {
	calles=c;
}

unsigned int Ciudad::calle(int i, int j, direccion d) { //recibe la esquina y una direccion, devuelve la cantidad de zombis que hay en esa cuadra
	// i y j indexan desde 0
	// las direcciones U y D son pares, L y R son impares
	if (i-(d==U) < 0 || 2*i+(d==D) >= calles.size() || j-(d==L) < 0 || j-(d==L)+(d==R)>=calles[0].size()){
		cerr << "Indice " << i << " " << j << " fuera de rango!\n";
		return INT_MAX;
	}
	return calles[2*i + (d == D) - (d == U)][j - (d == L)];
}