# PROYECTO TA TE TI

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
    combinaciones = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in combinaciones:
        if tablero[combo[0]] == jugador and tablero[combo[1]] == jugador and tablero[combo[2]] == jugador:
            return True
    return False


jugador_actual = "X"

while True:
    imprimir_tablero()

    # ================= INPUT + VALIDACIÓN =================
    while True:
        input_jugador = input(f"Jugador {jugador_actual}, elegí una posición (1-9): ")

        if not input_jugador.isdigit():
            print("Tenés que ingresar un número.")
            continue

        posicion = int(input_jugador) - 1

        if posicion < 0 or posicion > 8:
            print("El número tiene que estar entre 1 y 9.")
            continue

        if tablero[posicion] != " ":
            print("Esa posición ya está ocupada.")
            continue

        break
    # ======================================================

    # jugar movimiento
    tablero[posicion] = jugador_actual

    # verificar ganador
    if verificar_ganador(jugador_actual):
        imprimir_tablero()
        print(f"¡Felicidades! Ganó {jugador_actual}")
        break

    # verificar empate
    if " " not in tablero:
        imprimir_tablero()
        print("Empate, jueguen de nuevo.")
        break

    # cambiar jugador
    jugador_actual = "O" if jugador_actual == "X" else "X"