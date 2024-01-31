def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)


def verificar_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0], True  # Ganador en la fila
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i], True  # Ganador en la columna

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0], True  # Ganador en la diagonal principal
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2], True  # Ganador en la diagonal secundaria

    return None, False


def jugar_tres_en_raya():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugadores = ['X', 'O']
    turno = 0

    while True:
        imprimir_tablero(tablero)

        fila = int(input(f"Jugador {jugadores[turno]}, ingrese fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugadores[turno]}, ingrese columna (0, 1, 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugadores[turno]
            ganador, hay_ganador = verificar_ganador(tablero)

            if hay_ganador:
                imprimir_tablero(tablero)
                print(f"\n¡El jugador {ganador} ha ganado!")
                break

            turno = 1 - turno  # Alternar turno entre jugadores
        else:
            print("¡Esa casilla ya está ocupada! Intente de nuevo.")

        # Verificar empate
        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            imprimir_tablero(tablero)
            print("\n¡Es un empate!")
            break


if __name__ == "__main__":
    jugar_tres_en_raya()
