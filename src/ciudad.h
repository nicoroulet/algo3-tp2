#include <vector>
#include <iostream>

enum direccion {U, L, D, R};
class Ciudad {
public:
	Ciudad(std::vector<std::vector<int> > &calles);
	unsigned int calle(int i, int j, direccion d);
private:
	std::vector<std::vector<int> > calles;
};