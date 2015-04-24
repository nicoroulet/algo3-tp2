#include <iostream>
#include <vector>

using namespace std;

enum vehiculo {
trash,Bici,Moto,Buggy
};

struct datos{
	int costo, i, j, k;
	vehiculo v;
};

datos magicMin(datos d1, datos d2) {
	if (d1.costo < d2.costo) {
		return d1;	
	} else {
		return d2;	
	}
}

int main() {
	int n, k_m, k_b;
	cin >> n >> k_m >> k_b;
	k_m++;k_b++;
	vector<int> costo_bici(n);
	vector<int> costo_moto(n);
	vector<int> costo_buggy(n);

	for (int i = 0; i < n; ++i)
	{
		cin >> costo_bici[i] >> costo_moto[i] >> costo_buggy[i];
		cout << " " << costo_bici[i] << " " << costo_moto[i] << " " << costo_buggy[i] << endl;
			
	}
	
	vector<vector<vector<datos>>> matriz(n+1, vector<vector<datos>>(k_m, vector<datos>(k_b, {0,0,0,0,trash})));
	for (int i = 1; i <= n; ++i)
	{
		matriz[i][0][0] = {matriz[i-1][0][0].costo + costo_bici[i-1],i-1,0,0,Bici};	//Inicializamos primer posición
		for (int m = 1; m < k_m; ++m)
		{
			//Inicializamos primera columna
			datos d1 = {matriz[i-1][m-1][0].costo + costo_moto[i-1],i-1,m-1,0, Moto};
			datos d2 = {matriz[i-1][m][0].costo + costo_bici[i-1],i-1,m,0,Bici};
			matriz[i][m][0] = magicMin(d1,d2);
		}

		for(int b = 1; b < k_b; ++b){
			//Inicializamos primera fila
			datos d1 = {matriz[i-1][0][b-1].costo + costo_buggy[i-1],i-1,0,b-1,Buggy};
			datos d2 = {matriz[i-1][0][b].costo + costo_bici[i-1],i-1,0,b,Bici}; // aca anda mal pero ni idea porque
			matriz[i][0][b] = magicMin(d1,d2);	
		}

		//Recorremos el resto de la matriz[i]
		for (int m = 1; m < k_m; ++m)
		{
			for (int b = 1; b < k_b; ++b)
			{	//hacemos un minimo entre los tres, y seteamos el costo, y la posicion previa
				datos d1 = {matriz[i-1][m][b-1].costo + costo_buggy[i-1],i-1,m,b-1,Buggy};
				datos d2 = {matriz[i-1][m][b].costo + costo_bici[i-1],i-1,m,b,Bici};
				datos d3 = {matriz[i-1][m-1][b].costo + costo_moto[i-1],i-1,m-1,b,Moto};
				matriz[i][m][b] = magicMin(d1,magicMin(d2,d3));
			}
		}
	}
	vector<int> out;
	datos d = matriz[n][k_m-1][k_b-1];
	while (out.size() < n){
		out.insert(out.begin(),d.v);
		d = matriz[d.i][d.j][d.k];
	}
	cout << matriz[n][k_m-1][k_b-1].costo;
	for (vector<int>::iterator it = out.begin(); it != out.end(); ++it){
		cout << " " << *it;	
	}
	cout << endl;
	return 0;
}
