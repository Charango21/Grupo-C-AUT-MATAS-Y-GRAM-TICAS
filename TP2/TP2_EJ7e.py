# AFD obtenido por subconjuntos
# Estados: A, B, C, D, E
# Estado inicial: A
# Estado de aceptación: E
# Alfabeto: {a, b}

def afd(cadena):
    estado = "A"

    for simbolo in cadena:

        if estado == "A":
            if simbolo == "a":
                estado = "B"
            elif simbolo == "b":
                estado = "C"
            else:
                return False

        elif estado == "B":
            if simbolo == "a":
                estado = "B"
            elif simbolo == "b":
                estado = "D"
            else:
                return False

        elif estado == "C":
            if simbolo == "a":
                estado = "B"
            elif simbolo == "b":
                estado = "C"
            else:
                return False

        elif estado == "D":
            if simbolo == "a":
                estado = "B"
            elif simbolo == "b":
                estado = "E"
            else:
                return False

        elif estado == "E":
            if simbolo == "a":
                estado = "B"
            elif simbolo == "b":
                estado = "C"
            else:
                return False

    return estado == "E"


# =========================
# PRUEBAS
# =========================
pruebas = [
    "abb",      # válida
    "aabb",     # válida
    "babb",     # válida
    "ab",       # inválida
    "bbbb",     # inválida
]

for cadena in pruebas:
    if afd(cadena):
        print(f"{cadena} -> ACEPTADA")
    else:
        print(f"{cadena} -> RECHAZADA")