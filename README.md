CspSolver-Sudoku
================

A constraint satisfaction problem (CSP) solver that solves sudoku puzzles. 

####cspbase.py
Contains the building blocks of formulating a constraint satisfaction problem: the variables and constraints classes.

####sudoku_csp.py
Contains the methods that can be used to formulate a CSP from a given sudoku board specification and solve it. It has functions to:
- enforce generalized arc consistency (GAC)
- create all-diff and not-equal constraints
- generate variables from sudo specification
- generate satisfying tuples for constraints

Finally, using these functions, it can create models for to solve sudoku problems in 3 ways:
- using all-diff constraint
- using not-equal constraint
- using not-equals first and then all-diff constraints
These functions are intended to compare performance in solving the problem using different approach.

####test_boards.py
Sample test boards with different levels of difficulty that are used to test different models and print out how long each model takes to solve these problems. 
