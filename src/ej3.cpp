#include <iostream>
#include <algorithm>

typedef struct {
	int a, b, c; // pozo a, pozo b, costo
	operator<(c2) {return c<c2.c}
} conexion;

int main() {
	int n, m, C;
	cin << n << m << C; // pozos, conexiones, costo refineria

	vector<conexion> conexiones;

	for (int i = 0; i < m; ++i)
	{
		conexion temp;
		cin << temp.a << temp.b << temp.c;
		if (c<C) conexiones.push_back(temp);
	}
	sort(conexiones);

	int ultimo_arbol=0;
	vector<int> arboles(n,-1); // iesima posicion indica en que numero de arbol esta el nodo i
	vector<conexion> conexiones_finales;
	for (auto it = conexiones.begin(); it < conexiones.end(); ++it)
	{
		/* opciones: a y b no estan en ningun arbol
					 uno de los dos si
					 los dos estan en el mismo arbol
					 los dos estan en arboles diferentes
		*/
		if (arbol[it->a] == -1 && arbol[it->b] == -1) { // si ningun nodo esta en ningun arbol
			arbol[it->a] = arbol[it->b] = ultimo_arbol++; // wowowowowo
			conexiones_finales.push_back(*it);
		}
		else if (arbol[it->a] != -1 && arbol[it->b] == -1) { // si b no esta en ningun arbol y a si
			arbol[it->b] = arbol[it->a];
			conexiones_finales.push_back(*it);
		}
		else if (arbol[it->a] == -1 && arbol[it->b] != -1) { // si a no esta en ningun arbol y b si
			arbol[it->a] = arbol[it->b];
			conexiones_finales.push_back(*it);
		}
		else if (arbol[it->a] != arbol[it->b]) {	// si a y b estan en arboles diferentes, los mergeamos
			int temp = arbol[it->b];
			for (int i = 0; i < n; ++i)
			{
				if (arbol[i] == temp) arbol[i] = arbol[it->a];
			}
			conexiones_finales.push_back(*it);
		}
		
	}

}