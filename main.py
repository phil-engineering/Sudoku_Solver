# Imports
from solver_algorithm import *

# Definition of the Sudoku to be tested in 2D arrays
empty_sudoku = [[0,3,0,4,0,0,0,0,0],[5,0,2,9,0,8,6,0,7],[0,9,1,0,0,0,2,0,4],[0,0,0,0,1,0,0,0,0],[0,7,0,0,0,0,0,0,0],[0,6,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0],[0,0,5,0,0,0,0,0,0]]
easy_sudoku1 = [[8,5,0,0,0,0,0,1,0],[0,0,0,3,0,6,4,5,0],[0,3,0,5,0,0,0,0,6],[0,0,0,9,4,3,6,2,7],[6,9,2,0,0,8,5,0,0],[0,0,0,0,0,2,0,9,0],[0,0,0,2,0,1,9,7,0],[9,2,1,4,0,7,0,0,5],[0,7,3,0,9,0,2,6,0]]
medium_sudoku1 = [[3,0,0,0,0,1,7,0,0],[0,7,0,0,0,0,3,4,5],[0,0,0,0,0,3,0,9,0],[0,0,2,0,0,0,4,7,0],[0,0,0,3,0,0,1,0,2],[7,6,0,1,0,9,0,3,0],[0,0,0,0,5,0,0,1,3],[9,1,0,0,0,0,0,0,0],[6,8,3,9,0,0,0,0,4]]
hard_sudoku1 = [[0,9,2,0,0,0,5,0,0],[8,0,5,0,0,0,0,6,7],[7,0,4,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,6,0,0],[0,7,3,1,6,0,0,8,0],[0,0,0,0,4,8,2,0,0],[0,0,9,0,7,0,0,3,0],[0,0,0,6,3,1,0,4,5]]
ETS_sudoku1 = [[0,0,4,0,0,9,7,8,2],[0,0,0,0,0,4,0,0,5],[2,0,0,7,0,0,0,0,9],[0,0,0,0,0,0,8,9,0],[0,0,0,0,3,0,0,0,0],[0,3,2,0,0,0,0,0,0],[4,0,0,0,0,7,0,0,8],[9,0,0,3,0,0,0,0,0],[7,2,8,6,0,0,5,0,0]]

# Select the Sudoku from the list above
sudoku_to_solve = medium_sudoku1

# Program starts here
sudoku_completed = False
loop_count = 0
stop_time = 0

# Print the unsolved Sudoku in the console
print_sudoku_terminal(sudoku_to_solve)
# Start timer before t
start_time = current_nano_time()
# Try to solve the sudoku in 100 attempts
for k in range(0, 100):
    for ii in range(1, 10):
        # Check if the Sudoku has been solved in the last iteration
        sudoku_completed = is_sudoku_completed(sudoku_to_solve)
        # If the Sudoku is completly solved, we quit the loop!
        if sudoku_completed[0]:
            stop_time = current_nano_time()
            break

        # Call the algorithm to check each row, column and square.
        # Trying to solve the puzzle
        check_combinaision_row(sudoku_to_solve, ii)
        check_combinaision_column(sudoku_to_solve, ii)
        check_combinaision_square(sudoku_to_solve, ii)

    loop_count += 1     # Loop counter for statistics
    # If the Sudoku is completly solved, we quit the loop!
    if sudoku_completed[0]:
        break

# Verdict: Solved or not?
if is_sudoku_completed(sudoku_to_solve)[0] == False:
    print("Unable to solve...  :(")
else:
    print("Sudoku solved in {} loops.".format(loop_count))
    print("Solving time : {} ns".format((stop_time - start_time) / 1e6))
# Print the solved Sudoku in the console
print_sudoku_terminal(sudoku_to_solve)
