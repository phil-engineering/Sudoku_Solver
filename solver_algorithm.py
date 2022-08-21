# Imports
import math
import time

# Global definitions for the algorithm
ROW_SEARCH = 0
COLUMN_SEARCH = 1
SQUARE_SEARCH = 2

# Used to print a Sudoku in the console for better visualization
def print_sudoku_terminal(sudoku_grid):
    for i in range(0, 9):
        row = ""
        for j in range(0, 9):
            if j == 8:
                row += " {} ".format(sudoku_grid[i][j])
            elif math.floor(j % 3) == 2:
                row += " {} ||".format(sudoku_grid[i][j])
            else:
                row += " {} |".format(sudoku_grid[i][j])
        print(row)
        if i == 8:
            break
        elif math.floor(i % 3) == 2:
            print("-------------------------------------")


# Row are from 1 to 9
def check_number_in_row(sudoku_grid, row, number):
    number_found = []
    global_number_position = []
    index = 0
    for i in sudoku_grid[row-1]:
        index += 1
        if i == number:
            number_found.append(True)
            global_number_position.append((row - 1) * 9 + index)

    return number_found, global_number_position


# Column are from 1 to 9
def check_number_in_column(sudoku_grid, column, number):
    number_found = []
    global_number_position = []
    index = 0
    for row_sweep in range(1, 10):
        index += 1
        if sudoku_grid[row_sweep-1][column-1] == number:
            number_found.append(True)
            global_number_position.append((row_sweep - 1) * 9 + column)

    return number_found, global_number_position


# Column are from 1 to 9
def check_number_in_3x3_square(sudoku_grid, square_number, number):
    number_found = []
    global_number_position = []
    index = 0
    if 1 <= square_number <= 3:
        _row = list(range(1, 4))
        _column = list(range(1 + (square_number - 1) * 3, 4 + (square_number - 1) * 3))
    elif 4 <= square_number <= 6:
        _row = list(range(4, 7))
        _column = list(range(1 + (square_number - 4) * 3, 4 + (square_number - 4) * 3))
    elif 7 <= square_number <= 9:
        _row = list(range(7, 10))
        _column = list(range(1 + (square_number - 7) * 3, 4 + (square_number - 7) * 3))
    else:
        _row = list(range(1, 4))
        _column = list(range(1, 4))

    for row_sweep in _row:
        for column_sweep in _column:
            index += 1
            if sudoku_grid[row_sweep-1][column_sweep-1] == number:
                number_found.append(True)
                global_number_position.append((row_sweep - 1) * 9 + column_sweep)

    return number_found, global_number_position


def check_valid_position_row(sudoku_grid, _row):
    print(missing_number(sudoku_grid, 0, _row))

# List all the missing number for a row, column or square
def missing_number(sudoku_grid, type_of_search, _id):
    number = list(range(1, 10))
    status = []
    position = 0
    list_missing_numbers = []
    for i in number:
        if type_of_search == ROW_SEARCH:
            status, position = check_number_in_row(sudoku_grid, _id, i)
        elif type_of_search == COLUMN_SEARCH:
            status, position = check_number_in_column(sudoku_grid, _id, i)
        elif type_of_search == SQUARE_SEARCH:
            status, position = check_number_in_3x3_square(sudoku_grid, _id, i)

        if len(status) == 0:
            list_missing_numbers.append(i)
        # print("Number: {}; Found? {}; Position: {}".format(i, status, position))

    return list_missing_numbers

# List all the position for the missing numbers in the Sudoku as for row, column or square
def find_empty_position(sudoku_grid, type_of_search):
    position = []
    list_missing_numbers = []
    for i in range(1, 10):
        if type_of_search == ROW_SEARCH:
            status, position = check_number_in_row(sudoku_grid, i, 0)
        elif type_of_search == COLUMN_SEARCH:
            status, position = check_number_in_column(sudoku_grid, i, 0)
        elif type_of_search == SQUARE_SEARCH:
            status, position = check_number_in_3x3_square(sudoku_grid, i, 0)

        # print("Number: {}; Position: {}".format(i, position))
        list_missing_numbers.append(position)

    return list_missing_numbers

# Write a value to any position in a Sudoku grid
def write_value_to_sudoku(sudoku_grid, absolute_position, _value):
    _row = int((absolute_position - 1) / 9) + 1
    _column = absolute_position - (_row - 1) * 9

    print("Wrote {} to position {}".format(_value, absolute_position))
    sudoku_grid[_row-1][_column-1] = _value


def absolute_position_to_column_position(abs_position):
    _row = int((abs_position - 1) / 9) + 1
    return abs_position - (_row - 1) * 9


def absolute_position_to_row_position(abs_position):
    return int((abs_position - 1) / 9) + 1


def absolute_position_to_square_position(abs_position):
    _row = int((abs_position - 1) / 9) + 1
    _column = abs_position - (_row - 1) * 9
    _square = int((_column - 1) / 3) + 3 * int((_row - 1) / 3) + 1

    return _square


def check_and_write_for_single_missing_number(sudoku_grid, type_of_search, _id):
    missing_number_list = missing_number(sudoku_grid, type_of_search, _id)
    position_of_missing_number_list = find_empty_position(sudoku_grid, type_of_search)[_id - 1]

    if len(missing_number_list) == 1:   # Only one missing number
        print("Missing number: {} at position {}".format(missing_number_list[0], position_of_missing_number_list[0]))
        write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[0], missing_number_list[0])
    else:
        uuu = 1
        # print("More then one number missing...")


# Check in a row for any missing number. Then for each missing number, check
#   if we have enough information to add one in the empty positions
def check_combinaision_row(sudoku_grid, _row):
    # First loop check in columns and second loop check in squares
    for search_type in range(0, 2):
        missing_number_list = missing_number(sudoku_grid, 0, _row)
        position_of_missing_number_list = find_empty_position(sudoku_grid, 0)[_row - 1]
        relative_position_of_missing_number_list = position_of_missing_number_list.copy()
        # print(missing_number_list, position_of_missing_number_list)

        # Create an empty 2D list
        found_array = [[0 for c in range(len(missing_number_list))] for r in range(len(position_of_missing_number_list))]

        # Check in each colomn of the missing number to see if it's possible position or not
        # Convert the absolute position array to column position array
        for i in range(len(relative_position_of_missing_number_list)):
            if search_type == 0:    # Search by column
                relative_position_of_missing_number_list[i] = absolute_position_to_column_position(position_of_missing_number_list[i])
            else:                   # Search by square
                relative_position_of_missing_number_list[i] = absolute_position_to_square_position(position_of_missing_number_list[i])

        for index_num, number in enumerate(missing_number_list):
            for index_type, column_square in enumerate(relative_position_of_missing_number_list):
                if search_type == 0:  # Search by column
                    number_found, global_number_position = check_number_in_column(sudoku_grid, column_square, number)
                else:                 # Search by square
                    number_found, global_number_position = check_number_in_3x3_square(sudoku_grid, column_square, number)
                # print("Num: {}; Column (or Square): {}; Found? {}; Position: {}".format(number, column_square, number_found, global_number_position))
                if len(number_found) != 0:
                    # print(index_num, index_col)
                    found_array[index_num][index_type] = int(number_found[0])

        # print(found_array)
        for i in range(len(missing_number_list)):
            if len(found_array[i]) <= 1:
                write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[0], missing_number_list[i])
                break
            if 1 < len(found_array[i]) <= 2:
                if found_array[i][0] or found_array[i][1]:
                    # print("Writing in {}".format(search_type))
                    # print(found_array[i], position_of_missing_number_list[0], missing_number_list[i])
                    index = found_array[i].index(0)
                    write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[index], missing_number_list[i])
                    break
            if 3 <= len(found_array[i]) <= 9:
                write_condition = 0
                for _count in found_array[i]:
                    if _count == 0:
                        write_condition += 1
                if write_condition == 1:
                    index = found_array[i].index(0)
                    write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[index], missing_number_list[i])
                    break

    check_and_write_for_single_missing_number(sudoku_grid, 0, _row)


# Check in a column for any missing number. Then for each missing number, check
#   if we have enough information to add one in the empty positions
def check_combinaision_column(sudoku_grid, _column):
    # First loop check in columns and second loop check in squares
    for search_type in range(0, 2):
        missing_number_list = missing_number(sudoku_grid, 1, _column)
        position_of_missing_number_list = find_empty_position(sudoku_grid, 1)[_column - 1]
        relative_position_of_missing_number_list = position_of_missing_number_list.copy()
        # print(missing_number_list, position_of_missing_number_list)

        # Create an empty 2D list
        found_array = [[0 for c in range(len(missing_number_list))] for r in range(len(position_of_missing_number_list))]

        # Check in each colomn of the missing number to see if it's possible position or not
        # Convert the absolute position array to column position array
        for i in range(len(relative_position_of_missing_number_list)):
            if search_type == 0:    # Search by column
                relative_position_of_missing_number_list[i] = absolute_position_to_row_position(position_of_missing_number_list[i])
            else:                   # Search by square
                relative_position_of_missing_number_list[i] = absolute_position_to_square_position(position_of_missing_number_list[i])

        for index_num, number in enumerate(missing_number_list):
            for index_type, column_square in enumerate(relative_position_of_missing_number_list):
                if search_type == 0:  # Search by column
                    number_found, global_number_position = check_number_in_row(sudoku_grid, column_square, number)
                else:                 # Search by square
                    number_found, global_number_position = check_number_in_3x3_square(sudoku_grid, column_square, number)
                # print("Num: {}; Column (or Square): {}; Found? {}; Position: {}".format(number, column_square, number_found, global_number_position))
                if len(number_found) != 0:
                    # print(index_num, index_col)
                    found_array[index_num][index_type] = int(number_found[0])

        # print(found_array)
        for i in range(len(missing_number_list)):
            if len(found_array[i]) <= 1:
                write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[0], missing_number_list[i])
                break
            if 1 < len(found_array[i]) <= 2:
                if found_array[i][0] or found_array[i][1]:
                    # print("Writing in {}".format(search_type))
                    index = found_array[i].index(0)
                    write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[index], missing_number_list[i])
                    break
            if 3 <= len(found_array[i]) <= 9:
                write_condition = 0
                for _count in found_array[i]:
                    if _count == 0:
                        write_condition += 1
                if write_condition == 1:
                    index = found_array[i].index(0)
                    write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[index], missing_number_list[i])
                    break

    check_and_write_for_single_missing_number(sudoku_grid, 1, _column)


# Check in a square for any missing number. Then for each missing number, check
#   if we have enough information to add one in the empty positions
def check_combinaision_square(sudoku_grid, _square):
    # First loop check in columns and second loop check in squares
    for search_type in range(0, 2):
        missing_number_list = missing_number(sudoku_grid, 2, _square)
        position_of_missing_number_list = find_empty_position(sudoku_grid, 2)[_square - 1]
        relative_position_of_missing_number_list = position_of_missing_number_list.copy()
        # print(missing_number_list, position_of_missing_number_list)

        # Create an empty 2D list
        found_array = [[0 for c in range(len(missing_number_list))] for r in range(len(position_of_missing_number_list))]

        # Check in each colomn of the missing number to see if it's possible position or not
        # Convert the absolute position array to column position array
        for i in range(len(relative_position_of_missing_number_list)):
            if search_type == 0:    # Search by column
                relative_position_of_missing_number_list[i] = absolute_position_to_row_position(position_of_missing_number_list[i])
            else:                   # Search by square
                relative_position_of_missing_number_list[i] = absolute_position_to_column_position(position_of_missing_number_list[i])

        for index_num, number in enumerate(missing_number_list):
            for index_type, column_square in enumerate(relative_position_of_missing_number_list):
                if search_type == 0:  # Search by column
                    number_found, global_number_position = check_number_in_row(sudoku_grid, column_square, number)
                else:                 # Search by square
                    number_found, global_number_position = check_number_in_column(sudoku_grid, column_square, number)
                # print("Num: {}; Column (or Square): {}; Found? {}; Position: {}".format(number, column_square, number_found, global_number_position))
                if len(number_found) != 0:
                    # print(index_num, index_col)
                    found_array[index_num][index_type] = int(number_found[0])

        # print(found_array)
        for i in range(len(missing_number_list)):
            if len(found_array[i]) <= 1:
                write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[0], missing_number_list[i])
                break
            if 1 < len(found_array[i]) <= 2:
                if found_array[i][0] or found_array[i][1]:
                    # print("Writing in {}".format(search_type))
                    index = found_array[i].index(0)
                    write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[index], missing_number_list[i])
                    break
            if 3 <= len(found_array[i]) <= 9:
                write_condition = 0
                for _count in found_array[i]:
                    if _count == 0:
                        write_condition += 1
                if write_condition == 1:
                    index = found_array[i].index(0)
                    write_value_to_sudoku(sudoku_grid, position_of_missing_number_list[index], missing_number_list[i])
                    break

    check_and_write_for_single_missing_number(sudoku_grid, 2, _square)


# Check if all rows, column or square have missing numbers.
def is_sudoku_completed(sudoku_grid):
    _sudoku_completed = False
    row_missing_cumulation = 0
    for _row in range(1, 10):
        # Check each row to see if there's missing numbers
        missing_number_list = missing_number(sudoku_grid, 0, _row)
        row_missing_cumulation += len(missing_number_list)

    if row_missing_cumulation == 0:
        _sudoku_completed = True
    return _sudoku_completed, row_missing_cumulation


# Get time in milliseconds
def current_milli_time():
    return round(time.time() * 1000)


# Get time in nanoseconds
def current_nano_time():
    return round(time.time_ns())
