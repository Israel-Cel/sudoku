import time

def is_valid(board, row, col, num):

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_least_choices_cell(board):
   
    min_options = float('inf')
    best_cell = None

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Celda vacía
                options = 0
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        options += 1

                if options < min_options:
                    min_options = options
                    best_cell = (row, col)

    return best_cell


def greedy_sudoku_solver(board):
   
    while True:
        
        cell = find_least_choices_cell(board)
        if not cell:
           
            return True

        row, col = cell
        found = False
        for num in range(1, 10):
            if is_valid(board, row, col, num):
             
                board[row][col] = num
                found = True
                break

        if not found:

            return False


if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    start_time = time.time()
    solved = greedy_sudoku_solver(sudoku_board)
    end_time = time.time()

    if solved:
        print("Tablero resuelto:")
        for row in sudoku_board:
            print(row)
    else:
        print("El enfoque voraz no pudo resolver el Sudoku.")

    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
