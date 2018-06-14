#ifndef SENSE_IMPROVED_H
#define SENSE_IMPROVED_H

#include <vector>
#include <iostream>

std::vector< std::vector <float> > sense_improved(char color, 
	std::vector< std::vector <char> > &grid, 
	std::vector< std::vector <float> > &beliefs, 
	float p_hit,
	float p_miss);

#endif /* SENSE_IMPROVED.H */