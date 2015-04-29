#include <vector>
#include <iostream>

class Ciudad {
public:
	enum direccion {U, R, D, L};
	Ciudad(std::vector<std::vector<int> > &calles);
	int calle(int i, int j, direccion d);
private:
	std::vector<std::vector<int> > calles;
};