from collections import deque


class Gramatica:

    def __init__(self, terminales, no_terminales,
                 simbolo_inicial, producciones):

        self.terminales = set(terminales)
        self.no_terminales = set(no_terminales)
        self.simbolo_inicial = simbolo_inicial
        self.producciones = producciones

    # CLASIFICACIÓN

    def es_regular(self):

        for izquierda, reglas in self.producciones.items():

            if izquierda not in self.no_terminales:
                return False

            for regla in reglas:

                if regla == 'ε':
                    continue

                if len(regla) == 1:

                    if regla not in self.terminales:
                        return False

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
        
    # DERIVACIÓN IZQUIERDA
  
    def derivar_izquierda(self, cadena):

        objetivo = cadena
        actual = self.simbolo_inicial

        pasos = [actual]

        while actual != objetivo:

            reemplazado = False

            # Buscar el NO TERMINAL más a la izquierda
            for i, simbolo in enumerate(actual):

                if simbolo in self.no_terminales:

                    nt = simbolo

                    for prod in self.producciones[nt]:

                        nueva = (
                            actual[:i] +
                            prod.replace('ε', '') +
                            actual[i+1:]
                        )

                        # poda simple
                        if len(nueva.replace('ε', '')) <= len(objetivo):

                            actual = nueva
                            pasos.append(actual)
                            reemplazado = True
                            break

                    break

            if not reemplazado:
                break

            if actual == objetivo:
                break

        print("Derivación izquierda:")

        for i, paso in enumerate(pasos, start=1):
            print(f"Paso {i}: {paso}")

    # DERIVACIÓN DERECHA

    def derivar_derecha(self, cadena):

        objetivo = cadena
        actual = self.simbolo_inicial

        pasos = [actual]

        while actual != objetivo:

            reemplazado = False

            # Buscar el NO TERMINAL más a la derecha
            for i in range(len(actual)-1, -1, -1):

                simbolo = actual[i]

                if simbolo in self.no_terminales:

                    nt = simbolo

                    for prod in self.producciones[nt]:

                        nueva = (
                            actual[:i] +
                            prod.replace('ε', '') +
                            actual[i+1:]
                        )

                        if len(nueva.replace('ε', '')) <= len(objetivo):

                            actual = nueva
                            pasos.append(actual)
                            reemplazado = True
                            break

                    break

            if not reemplazado:
                break

            if actual == objetivo:
                break

        print("Derivación derecha:")

        for i, paso in enumerate(pasos, start=1):
            print(f"Paso {i}: {paso}")

    # PERTENECE (BFS)

    def pertenece(self, cadena):

        cola = deque([self.simbolo_inicial])

        visitados = set()

        while cola:

            actual = cola.popleft()

            if actual == cadena:
                return True

            if actual in visitados:
                continue

            visitados.add(actual)

            # poda por longitud
            if len(actual.replace('ε', '')) > len(cadena):
                continue

            for i, simbolo in enumerate(actual):

                if simbolo in self.no_terminales:

                    for prod in self.producciones[simbolo]:

                        nueva = (
                            actual[:i] +
                            prod.replace('ε', '') +
                            actual[i+1:]
                        )

                        cola.append(nueva)

        return False

    # STRING

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


# CARGAR DESDE TEXTO

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
S -> aSb | ab
"""

g = cargar_desde_texto(texto)

print(g)

print(g.clasificar())

print()

g.derivar_izquierda("aaabbb")

print()

g.derivar_derecha("aaabbb")

print()

print(g.pertenece("aaabbb"))  # True
print(g.pertenece("aabb"))    # True
print(g.pertenece("aabbb"))   # False