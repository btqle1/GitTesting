move_count = 0
correct_row = False
correct_column = False

def solution(src, dest):
    # break down numbered tiles into 2d array form
    src_row = int(src / 8)
    src_column = src % 8
    dest_row = int(dest / 8)
    dest_column = dest % 8

    # print("Current position: " + str(src_row) + ":" + str(src_column))
    # print("Destination: " + str(dest_row) + ":" + str(dest_column))

    global correct_row
    global correct_column
    global move_count


    # Calculate the valid 5x5 area around source
    valid_area = calculate_area(src_row, src_column)

    # Check if rows/column matches
    for i in range(len(valid_area[0])):
        if dest_row == valid_area[0][i]:
            correct_row = True
    for i in range(len(valid_area[0])):
        if dest_column == valid_area[1][i]:
            correct_column = True
    # print(correct_row)
    # print(correct_column)
    if correct_row == True and correct_column == True:
        move_count = move_count + final_move(src_row, src_column, dest_row, dest_column)
        return move_count

    # Move and recursively use function to try again
    else:
        correct_row = False
        correct_column = False
        move_count = move_count + 1
        # print(move_count)
        new_src = calculate_next_move(src_row, src_column, dest_row, dest_column)
        solution(new_src, dest)

    return move_count

def calculate_area(src_row, src_column):
    valid_rows = [None, None, None, None, None]
    valid_columns = [None, None, None, None, None]
    for i in range(5):
        if 0 <= (src_row + (i - 2)) <= 7:
            valid_rows[i] = src_row + (i-2)
        if 0 <= (src_column + (i - 2)) <= 7:
            valid_columns[i] = src_column + (i-2)
    valid_area = [valid_rows, valid_columns]
    # print(valid_rows)
    # print(valid_columns)
    return valid_area

def calculate_next_move(src_row, src_column, dest_row, dest_column):
    new_src_row = 0
    new_src_column = 0
    if abs(src_row - dest_row) > 2:
        if src_column > dest_column:
            new_src_column = src_column - 1
        else:
            new_src_column = src_column + 1
        if src_row > dest_row:
            new_src_row = src_row - 2
        else:
            new_src_row = src_row + 2
    else:
        if src_row > dest_row:
            new_src_row = src_row - 1
        else:
            new_src_row = src_row + 1
        if src_column > dest_column:
            new_src_column = src_column - 2
        else:
            new_src_column = src_column + 2
    new_src = ((new_src_row * 8) + new_src_column)
    return new_src

def final_move(src_row, src_column, dest_row, dest_column):
    row_diff = abs(src_row - dest_row)
    column_diff = abs(src_column - dest_column)
    moves = 0

    if row_diff == 0 and column_diff == 0:
        moves = 0
    elif row_diff == 1 and column_diff == 1:
        if check_corner(src_row, src_column, dest_row, dest_column) == True:
            moves = 4
        else:
            moves = 2
    elif row_diff == 2 and column_diff == 2:
        moves = 4
    elif (row_diff == 0 and column_diff == 1) or (row_diff == 1 and column_diff == 0):
        moves = 3
    elif (row_diff == 0 and column_diff == 2) or (row_diff == 2 and column_diff == 0):
        moves = 2
    else:
        moves = 1

    return moves

def check_corner(src_row, src_column, dest_row, dest_column):
    if (src_row == 0 and src_column == 0 and dest_row == 1 and dest_column == 1) or \
            (src_row == 1 and src_column == 1 and dest_row == 0 and dest_column == 0) or \
            (src_row == 0 and src_column == 7 and dest_row == 1 and dest_column == 6) or \
            (src_row == 1 and src_column == 6 and dest_row == 0 and dest_column == 7) or \
            (src_row == 7 and src_column == 0 and dest_row == 6 and dest_column == 1) or \
            (src_row == 6 and src_column == 1 and dest_row == 7 and dest_column == 0) or \
            (src_row == 7 and src_column == 7 and dest_row == 6 and dest_column == 6) or \
            (src_row == 6 and src_column == 6 and dest_row == 7 and dest_column == 7):
        return True


# x = solution(0,63)
# print("Total moves: " + str(x))