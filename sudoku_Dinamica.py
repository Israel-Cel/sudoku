import time

def solve_sudoku_dynamic(board):
    rows = [[False] * 10 for _ in range(9)]
    cols = [[False] * 10 for _ in range(9)]
    boxes = [[False] * 10 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                rows[i][num] = True
                cols[j][num] = True
                box_index = (i // 3) * 3 + (j // 3)
                boxes[box_index][num] = True

    dp = {}

    def solve_dp(state):

        if state in dp:
            return dp[state]

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
               
                    box_index = (i // 3) * 3 + (j // 3)

                    for num in range(1, 10):
                        if not rows[i][num] and not cols[j][num] and not boxes[box_index][num]:
                          
                            board[i][j] = num
                            rows[i][num] = cols[j][num] = boxes[box_index][num] = True

                            if solve_dp(tuple(tuple(row) for row in board)):
                                dp[state] = True
                                return True

                            board[i][j] = 0
                            rows[i][num] = cols[j][num] = boxes[box_index][num] = False

                    dp[state] = False
                    return False

        dp[state] = True
        return True

    initial_state = tuple(tuple(row) for row in board)
    solve_dp(initial_state)
    return board

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
    solved_board = solve_sudoku_dynamic(sudoku_board)
    end_time = time.time()

    print("Tablero resuelto:")
    for row in solved_board:
        print(row)

    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
