#include "headers/blur_improved.h"
#include "headers/zeros_improved.h"

using namespace std;

vector < vector <float> > blur_improved(vector < vector < float> > &grid) {

	static float GLOBAL_BLURRING = 0.12;

	static float CENTER = 1.0 - GLOBAL_BLURRING;
	static float CORNER = GLOBAL_BLURRING / 12.0;
	static float ADJACENT = GLOBAL_BLURRING / 6.0;

	static vector <int> DX = {-1, 0, 1};
	static vector <int> DY = {-1, 0, 1};

	static vector < vector <float> > GLOBAL_WINDOW = { {CORNER, ADJACENT, CORNER}, {ADJACENT, CENTER, ADJACENT}, {CORNER, ADJACENT, CORNER} };


	vector < vector <float> > window;
	vector < vector <float> > newGrid;
	vector <float> row;
	vector <float> newRow;

	int height = grid.size();
	int width = grid[0].size();

	int i, j, ii, jj, new_i, new_j;
	int dx, dy;

	float multiplier;
	float newVal;

	// initialize new grid to zeros
	newGrid = zeros_improved(height, width);

	// original way
	for (i=0; i< height; i++ ) {
		for (j=0; j<width; j++ ) {
			newVal = grid[i][j];
			for (ii=0; ii<3; ii++) {
				dy = DY[ii];
				for (jj=0; jj<3; jj++) {
					dx = DX[jj];
					new_i = (i + dy + height) % height;
					new_j = (j + dx + width) % width;
					multiplier = GLOBAL_WINDOW[ii][jj];
					newGrid[new_i][new_j] += newVal * multiplier;
				}
			}
		}
	}

	return newGrid;
}
