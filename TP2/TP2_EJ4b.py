from collections import defaultdict
transiciones = defaultdict(list)

# Transiciones normales
transiciones[("q0", "a")].append("q1")
transiciones[("q2", "b")].append("q3")
transiciones[("q8", "a")].append("q9")
transiciones[("q10", "b")].append("q11")

# Transiciones epsilon
transiciones[("q4", "ε")] += ["q0", "q2"]
transiciones[("q1", "ε")] += ["q5"]
transiciones[("q3", "ε")] += ["q5"]
transiciones[("q6", "ε")] += ["q4", "q7"]
transiciones[("q5", "ε")] += ["q4", "q7"]
transiciones[("q7", "ε")] += ["q14"]
transiciones[("q12", "ε")] += ["q13"]
transiciones[("q14", "ε")] += ["q8", "q10", "q12"]
transiciones[("q9", "ε")] += ["q15"]
transiciones[("q11", "ε")] += ["q15"]
transiciones[("q13", "ε")] += ["q15"]

estado_inicial = "q6"
estados_finales = {"q15"}


def epsilon_closure(estados):
    pila = list(estados)
    cierre = set(estados)

    while pila:
        estado = pila.pop()
        for siguiente in transiciones.get((estado, "ε"), []):
            if siguiente not in cierre:
                cierre.add(siguiente)
                pila.append(siguiente)

    return cierre


def mover(estados, simbolo):
    resultado = set()

    for estado in estados:
        for siguiente in transiciones.get((estado, simbolo), []):
            resultado.add(siguiente)

    return resultado


def acepta(cadena):
    actuales = epsilon_closure({estado_inicial})

    for simbolo in cadena:
        actuales = mover(actuales, simbolo)
        actuales = epsilon_closure(actuales)

    return len(actuales.intersection(estados_finales)) > 0


# Pruebas
cadenas = ["", "a", "b", "ab", "ba", "abba", "bbb"]

for cadena in cadenas:
    print(f"Cadena: '{cadena}' -> {acepta(cadena)}")