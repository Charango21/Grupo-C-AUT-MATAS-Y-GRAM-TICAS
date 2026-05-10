# =====================================================
# BALANCEO DE PARÉNTESIS
# Gramática:
#
# S -> SS | (S) | ε
# =====================================================

class ValidadorParentesis:

    def __init__(self):

        self.terminales = {'(', ')'}

    # FILTRAR SOLO PARÉNTESIS

    def filtrar(self, texto):

        resultado = ""

        for c in texto:

            if c in self.terminales:
                resultado += c

        return resultado

    # VALIDAR BALANCEO

    def validar(self, cadena):

        pila = []

        for i, c in enumerate(cadena):

            # apertura
            if c == '(':
                pila.append(i)

            # cierre
            elif c == ')':

                # error: cierre sin apertura
                if not pila:
                    return False, i

                pila.pop()

        # quedaron aperturas sin cerrar
        if pila:
            return False, pila[-1]

        return True, -1

    # MOSTRAR ERROR

    def mostrar_error(self, texto, indice):

        print(texto)

        print(" " * indice + "^")

    # PROCESO COMPLETO

    def analizar(self, codigo):

        print("Código original:")
        print(codigo)

        print("\n---")

        filtrada = self.filtrar(codigo)

        print("Cadena filtrada:")
        print(filtrada)

        print("\n---")

        valido, indice = self.validar(filtrada)

        if valido:

            print("Resultado: PARÉNTESIS BALANCEADOS")

        else:

            print("Resultado: ERROR DE BALANCEO")
            print(f"Error en posición: {indice}")

            print("\nVisualización del error:")

            self.mostrar_error(filtrada, indice)

# EJEMPLOS

v = ValidadorParentesis()

# EJEMPLO CORRECTO

codigo1 = "if(x > y + 1) { print(x) }"

print("\n========== EJEMPLO 1 ==========\n")

v.analizar(codigo1)

# EJEMPLO CON ERROR

codigo2 = "if(x > y + 1)) { print(x) }"

print("\n\n========== EJEMPLO 2 ==========\n")

v.analizar(codigo2)

# EJEMPLO CON APERTURA SIN CIERRE

codigo3 = "((a+b)"

print("\n\n========== EJEMPLO 3 ==========\n")

v.analizar(codigo3)