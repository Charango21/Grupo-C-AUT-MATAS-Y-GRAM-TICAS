"""
SpamScanner 2.0 — Pipeline completo
"""

import csv
import os
import random
from maquina_turing import normalizar
from tokenizador import tokenizar
from clasificador import clasificar, puntuar, evaluar

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

    print("=== Etapa 1 + 2 + 3: Normalización, Tokenización y Clasificación ===\n")
    print(f"Total mensajes: {len(todos)} (50 HAM, 50 SPAM)\n")

    todas_etiquetas = []
    todos_los_tokens = []

    for i, (etiqueta, mensaje) in enumerate(todos, 1):
        texto_norm, traza = normalizar(mensaje)
        tokens = tokenizar(texto_norm)
        todas_etiquetas.append(etiqueta)
        todos_los_tokens.append(tokens)

        pred = clasificar(tokens, umbral=4)
        pj = puntuar(tokens)
        if pred == etiqueta:
            acierto = "[OK]"
        else:
            acierto = "[ERR]"

        print(f"[{i:3d}] {etiqueta:4s} | pj={pj:2d} -> {pred:4s} {acierto}")
        print(f"       | {texto_norm[:70]}")
        print(f"       | tokens: {tokens}")
        print()

    print("=" * 60)
    print("           EVALUACIÓN — ETAPA 3")
    print("=" * 60)

    valores_u = [2, 4, 6]
    resultados = evaluar(todos_los_tokens, todas_etiquetas, valores_u)

    print(f"\n{'Umbral U':>9} {'Accuracy':>9} {'Precision':>10} {'Recall':>8} {'F1':>7}   {'TP':>3} {'FP':>3} {'TN':>3} {'FN':>3}")
    print("-" * 68)
    for r in resultados:
        print(
            f"{r['U']:>9}  {r['accuracy']:>8.2%}  {r['precision']:>9.2%}  "
            f"{r['recall']:>7.2%}  {r['f1']:>6.2f}   {r['tp']:>3} {r['fp']:>3} {r['tn']:>3} {r['fn']:>3}"
        )

    mejor = max(resultados, key=lambda r: r["accuracy"])
    print(f"\n-> Mejor umbral: U = {mejor['U']} (accuracy: {mejor['accuracy']:.2%})")
