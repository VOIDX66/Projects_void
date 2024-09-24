import random
#from rich import print

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def disp_moves(board):
    disp_moves = []

    for i, _ in enumerate(board):
        for j, data_j in enumerate(board[i]):
            if data_j == " ":
                disp_moves.append((i, j))
    #print(disp_moves)
    return disp_moves

def verificar_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != ' ':
            return fila[0]  

    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != ' ':
            return tablero[0][col]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
        return tablero[0][0]

    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != ' ':
        return tablero[0][2]

    return None

def play(player1,player2,board):
    while True:
        movimientos = disp_moves(board)
        if movimientos:
            movimiento = random.choice(movimientos)
            fila, columna = movimiento
            board[fila][columna] = player1
            movimientos.remove(movimiento)
            #print_board(board)
            estado = verificar_ganador(board)
            if estado:
                return estado
            if movimientos:
                movimiento = random.choice(movimientos)
                fila, columna = movimiento
                board[fila][columna] = player2
                movimientos.remove(movimiento)
                #print_board(board)
                estado = verificar_ganador(board)
                if estado:
                    return estado
            else:
                #print_board(board)
                return None


def play_ntimes(n):
    count_p1 = 0
    count_p2 = 0
    count_empate = 0

    player1 = "X"
    player2 = "O"

    for i in range(n):
        board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]

        print(f"\nJUEGO {i+1}")
        resultado = play(player1,player2,board)
        if resultado == player1:
            count_p1 += 1
        elif resultado == player2:
            count_p2 += 1
        else:
            count_empate += 1
        print_board(board)
    print(f"GANADOR {player1} : {count_p1} | {round((count_p1/n)*100,2) if count_p1 !=0 else 0}%")
    print(f"GANADOR {player2} : {count_p2} | {round((count_p2/n)*100,2) if count_p2 !=0 else 0}%")
    print(f"EMPATE : {count_empate}    | {round((count_empate/n)*100,2) if count_empate !=0 else 0}%")

play_ntimes(10000)