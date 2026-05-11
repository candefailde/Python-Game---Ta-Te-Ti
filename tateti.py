#PROYECTO TA TE TI
tablero = [" " for _ in range(9)]

def imprimir_tablero():
    print()
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+--+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+--+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")
    print()

def verificar_ganador(jugador):
    combinaciones = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for combo in combinaciones:
        if (tablero[combo[0]] == jugador and tablero[combo[1]] == jugador and tablero[combo[2]] == jugador):
            return True
    return False

jugador_actual = "X"

while True:
    imprimir_tablero()
    input_jugador = input(f"Jugador {jugador_actual}, elegi una pocision (1-9): ")
    while input_jugador not in [1,2,3,4,5,6,7,8,9]:
        input_jugador = input(f"Jugador {jugador_actual} la posicion no el valida, volve a intentar: ")
    posicion = int(input_jugador) - 1

    if (tablero[posicion]) != " ":
        print("Posicion ocupada")
        continue

    tablero[posicion] = jugador_actual

    if verificar_ganador(jugador_actual):
        imprimir_tablero()
        print(f"Felicidades, ganaste {jugador_actual}!")
        break

    if " " not in tablero:
        imprimir_tablero()
        print("Empate, jueguen de nuevoo")
        break

    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"