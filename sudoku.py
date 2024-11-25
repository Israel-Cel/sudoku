import time 
# sudoku_resolvedor_dividir_vencer.py

def resolver_sudoku_dv(tablero):

    # Encuentra la celda vacía con el menor número de posibilidades (divide el problema)
    vacia = encontrar_mejor_celda(tablero)
    if not vacia:
        return True  # Si no hay celdas vacías, el Sudoku está resuelto.
    fila, columna = vacia

    # Probar números válidos en la celda seleccionada
    for num in range(1, 10):
        if es_valido(tablero, num, fila, columna):
            # Asigna un número si es válido
            tablero[fila][columna] = num
            # Llama recursivamente para resolver el resto del tablero
            if resolver_sudoku_dv(tablero):
                return True
            # Si no se encuentra solución, deshace el movimiento (backtracking)
            tablero[fila][columna] = 0

    return False  # Si no se puede colocar ningún número válido, retorna False


def encontrar_mejor_celda(tablero):
    """
    Encuentra la celda vacía con menos posibilidades válidas.
    para tablero: Matriz de 9x9 representando el tablero de Sudoku.
    return: Una tupla (fila, columna) de la celda seleccionada, o None si no hay celdas vacías.
    """
    mejor_celda = None
    min_posibilidades = 10  # Inicia con un valor imposible (mayor que 9 posibilidades).

    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:  # Si la celda está vacía
                # Calcula cuántos números son válidos para esta celda
                posibilidades = sum(1 for num in range(1, 10) if es_valido(tablero, num, fila, columna))
                if posibilidades < min_posibilidades:
                    # Actualiza la celda con menos posibilidades
                    min_posibilidades = posibilidades
                    mejor_celda = (fila, columna)
                # Si hay una celda con solo 1 posibilidad, seleccionarla inmediatamente
                if min_posibilidades == 1:
                    break

    return mejor_celda


def es_valido(tablero, num, fila, columna):
    """
    Verifica si un número puede colocarse en una celda específica sin violar
    las reglas del Sudoku: no puede repetirse en la misma fila, columna o subcuadro 3x3.

    tablero: Matriz de 9x9 representando el tablero de Sudoku.
    num: Número que se intenta colocar en la celda.
    fila: Fila de la celda.
    columna: Columna de la celda.
    True si el número es válido, False en caso contrario.
    """
    # Verifica si el número ya existe en la fila
    if any(tablero[fila][i] == num for i in range(9)):
        return False

    # Verifica si el número ya existe en la columna
    if any(tablero[i][columna] == num for i in range(9)):
        return False

    # Verifica si el número ya existe en el subcuadro 3x3 correspondiente
    inicio_cuadro_fila, inicio_cuadro_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_cuadro_fila, inicio_cuadro_fila + 3):
        for j in range(inicio_cuadro_columna, inicio_cuadro_columna + 3):
            if tablero[i][j] == num:
                return False

    return True  # Si pasa todas las verificaciones, el número es válido


def imprimir_tablero(tablero):
    
   #Imprime el tablero de Sudoku en un formato legible para el usuario, con separadores para los bloques 3x3.
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Línea horizontal para separar bloques 3x3

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Separador vertical para bloques 3x3

            # Imprime el número o un punto si la celda está vacía
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")

        print()  # Nueva línea al final de cada fila


if __name__ == "__main__":
    tablero_sudoku = [
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

    print("Tablero inicial:")
    imprimir_tablero(tablero_sudoku)

    inicio = time.time()  
    resuelto = resolver_sudoku_dv(tablero_sudoku) 
    fin = time.time()   

    if resolver_sudoku_dv(tablero_sudoku):
        print("\nSolución encontrada:")
        imprimir_tablero(tablero_sudoku)
    else:
        print("\nNo se encontró solución.")

    print(f"\nTiempo de ejecución: {fin - inicio:.6f} segundos")