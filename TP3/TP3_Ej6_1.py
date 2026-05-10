class Gramatica:

    def __init__(self, terminales, no_terminales,
                 simbolo_inicial, producciones):

        self.terminales = set(terminales)
        self.no_terminales = set(no_terminales)
        self.simbolo_inicial = simbolo_inicial
        self.producciones = producciones

    # -------------------------------------------------

    def es_regular(self):

        for izquierda, reglas in self.producciones.items():

            # En Tipo 3 el lado izquierdo debe ser
            # un único no terminal
            if izquierda not in self.no_terminales:
                return False

            for regla in reglas:

                # epsilon
                if regla == 'ε':
                    continue

                # longitud 1 -> terminal
                if len(regla) == 1:
                    if regla not in self.terminales:
                        return False

                # longitud 2 -> terminal + no terminal
                elif len(regla) == 2:

                    if (regla[0] not in self.terminales or
                        regla[1] not in self.no_terminales):
                        return False

                else:
                    return False

        return True

    # -------------------------------------------------

    def es_glc(self):

        for izquierda in self.producciones:

            # Tipo 2:
            # un solo no terminal a la izquierda
            if izquierda not in self.no_terminales:
                return False

        return True

    # -------------------------------------------------

    def clasificar(self):

        if self.es_regular():
            return "Tipo 3: Regular"

        elif self.es_glc():
            return "Tipo 2: Libre de Contexto"

        else:
            return "Tipo 0 o Tipo 1"

    # -------------------------------------------------

    def __str__(self):

        texto = "Gramática:\n"

        texto += f"Terminales: {self.terminales}\n"
        texto += f"No terminales: {self.no_terminales}\n"
        texto += f"Símbolo inicial: {self.simbolo_inicial}\n"
        texto += "Producciones:\n"

        for izquierda, reglas in self.producciones.items():

            texto += f"  {izquierda} -> "

            texto += " | ".join(reglas)

            texto += "\n"

        return texto

# FUNCIÓN PARA CARGAR DESDE TEXTO

def cargar_desde_texto(texto):

    lineas = texto.strip().split("\n")

    producciones = {}

    no_terminales = set()
    terminales = set()

    simbolo_inicial = None

    for linea in lineas:

        linea = linea.strip()

        if not linea:
            continue

        izquierda, derecha = linea.split("->")

        izquierda = izquierda.strip()

        if simbolo_inicial is None:
            simbolo_inicial = izquierda

        no_terminales.add(izquierda)

        reglas = [r.strip() for r in derecha.split("|")]

        producciones[izquierda] = reglas

        # detectar terminales y no terminales
        for regla in reglas:

            for simbolo in regla:

                if simbolo.isupper():
                    no_terminales.add(simbolo)

                elif simbolo != 'ε':
                    terminales.add(simbolo)

    return Gramatica(
        terminales=terminales,
        no_terminales=no_terminales,
        simbolo_inicial=simbolo_inicial,
        producciones=producciones
    )

# EJEMPLO

texto = """
S -> aSb | ε
"""

g = cargar_desde_texto(texto)

print(g)

print(g.clasificar())
print(g.es_regular())
print(g.es_glc())