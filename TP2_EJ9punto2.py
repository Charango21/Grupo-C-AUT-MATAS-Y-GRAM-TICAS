def comentario_valido(cadena):
    estado = "q0"

    for simbolo in cadena:

        if estado == "q0":
            if simbolo == "/":
                estado = "q1"
            else:
                return False

        elif estado == "q1":
            if simbolo == "*":
                estado = "q2"
            else:
                return False

        elif estado == "q2":
            if simbolo in ["a", "b"]:
                estado = "q2"
            elif simbolo == "*":
                estado = "q3"
            else:
                return False

        elif estado == "q3":
            if simbolo == "/":
                estado = "q4"
            elif simbolo in ["a", "b"]:
                estado = "q2"
            elif simbolo == "*":
                estado = "q3"
            else:
                return False

        elif estado == "q4":
            return False

    return estado == "q4"


# Pruebas
pruebas = ["/*aba*/", "/*/", "/**/", "/*aaab"]

for cadena in pruebas:
    print(cadena, "->", comentario_valido(cadena))