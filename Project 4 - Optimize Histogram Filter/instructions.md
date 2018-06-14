INSTRUCTIONS:

In the optimized_code folder, you'll find examples of optimized histogram filter code. The changes made in this code run faster than Andy's original code; however, there is no "right" or "wrong" answer in terms of optimization.

You might have optimized using different techniques than the ones used here. The techniques used include:
- reserving memory for vectors
- passing larger variables to functions by reference
- removing variables that were not needed
- modifying vectors in place when possible instead of creating new vector variables
- iterating with ++i instead of i++
- removing dead code (lines of code that were in the files but no longer being used)
- avoiding extra for loops especially nested for loops when possible
- avoiding extra if statements
- using static and const keywords when appropriate

Run the following commands in a terminal window to see the results (you can copy and paste the commands):

cd optimized_code

g++ -std=c++11 main.cpp blur_improved.cpp initialize_beliefs_improved.cpp move_improved.cpp normalize_improved.cpp print.cpp sense_improved.cpp zeros_improved.cpp

./a.out