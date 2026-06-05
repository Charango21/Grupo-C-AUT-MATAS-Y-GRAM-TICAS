"""
SpamScanner 2.0 — Pipeline completo
"""

import csv
import os
import random
from maquina_turing import normalizar
from tokenizador import tokenizar

BASE = os.path.dirname(os.path.abspath(__file__))
RUTA_DATASET = os.path.join(BASE, "Dataset", "SpamCollectionSpanish.csv")


def cargar_mensajes(ruta, n_ham=50, n_spam=50, seed=42):
    random.seed(seed)
    ham, spam = [], []
    with open(ruta, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["label"] == "0":
                ham.append(row["text"])
            else:
                spam.append(row["text"])
    return random.sample(ham, n_ham), random.sample(spam, n_spam)


if __name__ == "__main__":
    ham_msgs, spam_msgs = cargar_mensajes(RUTA_DATASET)
    todos = [("HAM", m) for m in ham_msgs] + [("SPAM", m) for m in spam_msgs]

    print("=== Etapa 1 + 2: Normalización y Tokenización ===\n")
    print(f"Total mensajes: {len(todos)} (50 HAM, 50 SPAM)\n")

    contador = 1

    for elemento in todos:

        i = contador

        etiqueta = elemento[0]
        mensaje = elemento[1]

        resultado_normalizacion = normalizar(mensaje)

        texto_norm = resultado_normalizacion[0]
        traza = resultado_normalizacion[1]

        tokens = tokenizar(texto_norm)

        print("[" + str(i) + "] " + etiqueta + " | " + texto_norm[:70])

        print("         | tokens: " + str(tokens))
        print()

        contador += 1
