#include <iostream>
#include <vector>

#include "ciudad.h"

using namespace std;

struct data {
	int u, d, l, r; // up down left right, con cuantos soldados podes llegar a los vecinos
	int i, j;
};

int main() {
	int n, m, s;
	cin >> n >> m >> s;

	vector<vector<int> > calles(2*n, vector<int>(m));
	for (int i = 0; i < n; ++i)
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
	Ciudad c(calles);
	return 0;
}
