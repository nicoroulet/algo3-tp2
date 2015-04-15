#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
struct conexion {
	int a, b, c; // pozo a, pozo b, costo
	bool operator<(const conexion c2) const {return c<c2.c;}
};

int main() {
	int n, m, C;
	cin >> n >> m >> C; // pozos, conexiones, costo refineria

	vector<conexion> conexiones;

	for (int i = 0; i < m; ++i)
	{
		conexion temp;
		cin >> temp.a >> temp.b >> temp.c;
		if (temp.c<C) conexiones.push_back(temp);
	}
	sort(conexiones.begin(), conexiones.end());

	int ultimo_arbol=0;
	vector<int> arboles(n,-1); // iesima posicion indica en que numero de arbol esta el nodo i
	vector<conexion> conexiones_finales;
	int costo_final=0;
	for (auto it = conexiones.begin(); it < conexiones.end(); ++it)
	{
		/* opciones: a y b no estan en ningun arbol
					 uno de los dos si
					 los dos estan en el mismo arbol
					 los dos estan en arboles diferentes
		*/
		if (arboles[it->a] == -1 && arboles[it->b] == -1) { // si ningun nodo esta en ningun arbol
			arboles[it->a] = arboles[it->b] = ultimo_arbol++; // wowowowowo
			conexiones_finales.push_back(*it);
			costo_final += it->c;
		}
		else if (arboles[it->a] != -1 && arboles[it->b] == -1) { // si b no esta en ningun arbol y a si
			arboles[it->b] = arboles[it->a];
			conexiones_finales.push_back(*it);
			costo_final += it->c;
		}
		else if (arboles[it->a] == -1 && arboles[it->b] != -1) { // si a no esta en ningun arbol y b si
			arboles[it->a] = arboles[it->b];
			conexiones_finales.push_back(*it);
			costo_final += it->c;
		}
		else if (arboles[it->a] != arboles[it->b]) {	// si a y b estan en arboles diferentes, los mergeamos
			int temp = arboles[it->b];
			for (int i = 0; i < n; ++i)
			{
				if (arboles[i] == temp) arboles[i] = arboles[it->a];
			}
			conexiones_finales.push_back(*it);
			costo_final += it->c;
		}
		
	}
	vector<int> refinerias;
	int i = 0;
	for (auto it = arboles.begin(); it != arboles.end(); ++it, ++i)
	{
		if (find(arboles.begin(), it, *it) == it || (*it == -1)) refinerias.push_back(i);
	}
	costo_final += refinerias.size() * C;
	cout << costo_final << " " << refinerias.size() << " " << conexiones_finales.size() << endl;
	for (int i = 0; i < refinerias.size(); ++i)
	{
		cout << refinerias[i] << endl;
	}
	for (int i = 0; i < conexiones_finales.size(); ++i)
	{
		cout << conexiones_finales[i].a << " " << conexiones_finales[i].b << endl;
	}
}