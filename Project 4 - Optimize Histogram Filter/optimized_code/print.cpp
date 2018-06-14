#include "headers/print.h"
using namespace std;

void print_vector_float(vector< vector <float> > grid) {
	int rows = grid.size();
	int cols = grid[0].size();

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			cout << grid[i][j] << " ";
		}
		cout << '\n';
	}
	cout << '\n';
}

void print_vector_char(vector< vector <char> > grid) {
	int rows = grid.size();
	int cols = grid[0].size();

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			cout << grid[i][j] << " ";
		}
		cout << '\n';
	}
	cout << '\n';
}