#include "headers/zeros_improved.h"

using namespace std;

vector < vector <float> > zeros_improved(int height, int width) {
	int i;
	vector < vector <float> > newGrid;
	newGrid.reserve(height);

	vector <float> newRow;
	newRow.assign(width, 0);

	for (i=0; i<height; i++) {
		newGrid.push_back(newRow);
	}

	return newGrid;
}
