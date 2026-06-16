"""
SpamScanner 2.0 — Etapa 4: Validación Estructural (Gramáticas Libres de Contexto)

Reduce tokens al alfabeto {caps, money, text, contact} y valida contra una GLC
usando el algoritmo CYK.

GLC formal:
  G = (V, T, P, S)
  V = {S, G, C, N, U}
  T = {caps, money, text, contact}
  P:
    S → G U
    U → C N
    G → caps | G G
    C → money | text | C C
    N → contact | N N

Veredicto final:
  - HAM: ya era HAM en etapa 3
  - SPAM: SPAM en etapa 3 y aceptado por la GLC
  - SPAM_ATIPICO: SPAM en etapa 3 pero rechazado por la GLC
"""

REGLAS_CNF = [
    ("S", "G", "U"),
    ("U", "C", "N"),
    ("G", "caps", None),
    ("G", "G", "G"),
    ("C", "money", None),
    ("C", "text", None),
    ("C", "C", "C"),
    ("N", "contact", None),
    ("N", "N", "N"),
]


def reducir_tokens(tokens):
    """Convierte tokens de Etapa 2 al alfabeto reducido {caps, money, text, contact}.
    WORDs consecutivos se fusionan en un solo 'text'.
    """
    reducidos = []
    for t in tokens:
        if t == "MONEY":
            reducidos.append("money")
        elif t in ("URL", "PHONE"):
            reducidos.append("contact")
        elif t == "CAPS":
            reducidos.append("caps")
        elif t == "WORD":
            if reducidos and reducidos[-1] == "text":
                continue
            reducidos.append("text")
    return reducidos


def cyk_acepta(secuencia):
    """Algoritmo CYK: retorna True si la secuencia es generada por la GLC."""
    n = len(secuencia)
    if n == 0:
        return False
    tabla = [[set() for _ in range(n + 1)] for _ in range(n)]

    for i, tok in enumerate(secuencia):
        for lhs, rhs1, rhs2 in REGLAS_CNF:
            if rhs2 is None and rhs1 == tok:
                tabla[i][1].add(lhs)

    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            for k in range(1, length):
                izquierda = tabla[i][k]
                derecha = tabla[i + k][length - k]
                for lhs, rhs1, rhs2 in REGLAS_CNF:
                    if rhs2 is not None and rhs1 in izquierda and rhs2 in derecha:
                        tabla[i][length].add(lhs)

    return "S" in tabla[0][n]


def clasificar_estructural(tokens, pred_etapa3):
    """Veredicto final segun etapa 3 + GLC."""
    if pred_etapa3 == "HAM":
        return "HAM"
    reducidos = reducir_tokens(tokens)
    # Elimina text (WORDs) del inicio y final — son relleno.
    while reducidos and reducidos[0] == "text":
        reducidos.pop(0)
    while reducidos and reducidos[-1] == "text":
        reducidos.pop()
    if cyk_acepta(reducidos):
        return "SPAM"
    return "SPAM_ATIPICO"
