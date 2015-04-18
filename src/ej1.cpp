#include <iostream>
#include <vector>

using namespace std;

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
	vector<vector<int> > pre(k_m, vector<int>(k_b,0));
	vector<vector<int> > actual(k_m, vector<int>(k_b));
	for (int i = 0; i < n; ++i)
	{
		actual[0][0] = pre[0][0] + costo_bici[i];	//Inicializamos primer posición
		for (int m = 1; m < k_m; ++m)
		{
			//Inicializamos primera columna
			actual[m][0] = min(pre[m-1][0] + costo_moto[i], pre[m][0] + costo_bici[i]);
		}

		for(int b = 1; b < k_b; ++b){
			//Inicializamos primera fila
			actual[0][b] = min(pre[0][b-1] + costo_buggy[i], pre[0][b] + costo_bici[i]);	
		}

		//Recorremos el resto de la matriz
		for (int m = 1; m < k_m; ++m)
		{
			for (int b = 1; b < k_b; ++b)
			{
				actual[m][b] = min(pre[m-1][b] + costo_moto[i], min(pre[m][b-1] + costo_buggy[i], pre[m][b] + costo_bici[i]));
			}
		}
		actual.swap(pre);
	}
	cout << pre[k_m-1][k_b-1] << endl;
	return 0;
}