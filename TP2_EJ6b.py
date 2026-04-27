# AFD resultante
# Estados: A, B, C
# Estado inicial: A
# Estados de aceptación: A, B, C (todos aceptan)
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
                estado = "C"
            else:
                return False

        elif estado == "C":
            if simbolo == "a":
                estado = "B"
            elif simbolo == "b":
                estado = "C"
            else:
                return False

    # Todos los estados son de aceptación
    return estado in ["A", "B", "C"]


# Pruebas
cadenas = ["", "a", "b", "aa", "ab", "ba", "bbb", "aababb"]

for cadena in cadenas:
    if afd(cadena):
        print(f"'{cadena}' -> Aceptada")
    else:
        print(f"'{cadena}' -> Rechazada")
