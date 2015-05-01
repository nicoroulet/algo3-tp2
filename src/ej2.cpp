#include <iostream>
#include <vector>
#include <queue>
#include <list>

#include "ciudad.h"

using namespace std;

struct coord {
	int i, j;
	unsigned int s;
} __attribute__((packed));
struct data {
	//int u, d, l, r; // up down left right, con cuantos soldados podes llegar a los vecinos
	coord pre; // predecesor
	bool visitado;
} __attribute__((packed));

int main() {
	int n, m, Ih, Iv, Bh, Bv;
	unsigned int s;
	cin >> n >> m >> s >> Ih >> Iv >> Bh >> Bv;
	Iv--;Ih--;Bv--;Bh--;
	vector<vector<int> > calles(2*n-1, vector<int>(m));
	for (int i = 0; i < n-1; ++i) //leo la matriz
	{
		for (int j = 0; j < m-1; ++j)
		{
			cin >> calles[2*i][j];
		}
		for (int j = 0; j < m; ++j)
		{
			cin >> calles[2*i+1][j];
		}
	}
	for (int j = 0; j < m-1; ++j)
	{
		cin >> calles[2*n-2][j];
	}
	Ciudad c(calles);

	vector<vector<vector<data> > > grafo(n, vector<vector<data> >(m, vector<data>(s+1, {{-1,-1,0},false})));
	queue<coord> q;
	q.push(coord({Ih, Iv, s}));
	// bfs
	while(!q.empty()){
		coord n = q.front();
		q.pop();
		for (int d = 0; d < 4; ++d) // conecto a los vecinos con la cantidad de soldados correspondientes
		{
			if (n.s > 2 * c.calle(n.i, n.j, (direccion)d)) {
				coord vecino = {n.i - (d==U) + (d==D), n.j - (d==L) + (d==R), min(2 * n.s - c.calle(n.i, n.j, (direccion)d), n.s)};
				if (!grafo[vecino.i][vecino.j][vecino.s].visitado) {
					grafo[vecino.i][vecino.j][vecino.s] = {n, true};
					q.push(vecino);
				}
			}
		}
		// break;
	}
	
	unsigned int sfinal;
	for (sfinal = s; !grafo[Bh][Bv][sfinal].visitado && sfinal > 0; --sfinal) {} // busco el bunker visitado con mas soldados
	if (sfinal == 0) {
		cout << 0 << endl;
		return 0;
	}
	list<coord> camino;
	coord aux = {Bh,Bv,sfinal};
	while(aux.i != Ih || aux.j != Iv) {
		camino.push_front(aux);
		aux = grafo[aux.i][aux.j][aux.s].pre;
	}
	cout << sfinal << endl;
	for (auto it = camino.begin(); it != camino.end(); ++it) {
		cout << it->i << " " << it->j << endl;
	}

	return 0;
}
