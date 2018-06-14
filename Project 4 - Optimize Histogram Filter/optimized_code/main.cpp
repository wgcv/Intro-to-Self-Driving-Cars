#include <iostream>
#include <cstdio>
#include <ctime>
#include <vector>

#include "headers/initialize_beliefs_improved.h"
#include "headers/sense_improved.h"
#include "headers/blur_improved.h"
#include "headers/normalize_improved.h"
#include "headers/move_improved.h"
#include "headers/print.h"

using namespace std;

int main() {

	// number of iterations 
	int iterations = 10000;

	std::clock_t start;
	double duration;
  
  	vector < vector <char> > grid { {'r', 'g', 'r', 'r', 'r'}, {'g', 'r', 'r', 'g', 'g'}, {'r', 'g', 'r', 'r', 'r'} };

	vector< vector <float> > results;
	vector< vector <float> > beliefs;

	int height = grid.size();
	int width = grid[0].size();

	cout << "number of iterations: " << iterations << " " << "\n";

	// test initialize_beliefs
	start = std::clock();
	for (int i = 0; i < iterations; i++) {
		beliefs = initialize_beliefs_improved(height, width);
	}
	duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
	std::cout << "duration milliseconds initialize beliefs " << 1000 * duration << '\n';

	// test sense
	start = std::clock();
	for (int i = 0; i < iterations; i++) {
		beliefs = sense_improved('g', grid, beliefs, .7, .2);
	}
	duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
	std::cout << "duration milliseconds sense " << 1000 * duration << '\n';

	// test blur
	start = std::clock();
	for (int i = 0; i < iterations; i++) {
		beliefs = blur_improved(beliefs);
	}
	duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
	std::cout << "duration milliseconds blur " << 1000 * duration << '\n';

	// test normalize
	start = std::clock();
	for (int i = 0; i < iterations; i++) {
		beliefs = normalize_improved(beliefs);
	}
	duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
	std::cout << "duration milliseconds normalize " << 1000 * duration << '\n';

	// test move
	start = std::clock();
	for (int i = 0; i < iterations; i++) {
		beliefs = move_improved(3, 2, beliefs);
	}
	duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
	std::cout << "duration milliseconds move " << 1000 * duration << '\n';

}