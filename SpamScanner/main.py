"""
SpamScanner 2.0 — Pipeline completo
"""

import csv
import os
import random
from maquina_turing import normalizar
from tokenizador import tokenizar
from clasificador import clasificar, puntuar, evaluar
from gramatica import clasificar_estructural

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
    todos = []

    for m in ham_msgs:
        todos.append(("HAM", m))

    for m in spam_msgs:
        todos.append(("SPAM", m))

    print("=== Pipeline Completo: Etapas 1 a 4 (MT -> ER -> Clasif -> GLC) ===\n")
    print(f"Total mensajes: {len(todos)} (50 HAM, 50 SPAM)\n")

    todas_etiquetas = []
    todos_los_tokens = []
    finales = []
    spam_para_mostrar = []

    for i, elemento in enumerate(todos, 1):
        etiqueta = elemento[0]
        mensaje = elemento[1]
        i += 1
        texto_norm, traza = normalizar(mensaje)
        tokens = tokenizar(texto_norm)
        todas_etiquetas.append(etiqueta)
        todos_los_tokens.append(tokens)

        pred = clasificar(tokens, umbral=4)
        pj = puntuar(tokens)
        acierto = "[OK]" if pred == etiqueta else "[ERR]"

        print(f"[{i:3d}] {etiqueta:4s} | pj={pj:2d} -> {pred:4s} {acierto}")
        print(f"       | {texto_norm[:70]}")
        print(f"       | tokens: {tokens}")
        print()

        veredicto = clasificar_estructural(tokens, pred)
        finales.append(veredicto)
        if pred == "SPAM":
            spam_para_mostrar.append((i, etiqueta, veredicto, texto_norm))

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

    print()
    print("=" * 60)
    print("           ETAPA 4 — VALIDACIÓN ESTRUCTURAL (GLC)")
    print("=" * 60)
    print()

    for elemento in spam_para_mostrar:
        i = elemento[0]
        etiqueta = elemento[1]
        veredicto = elemento[2]
        texto_norm = elemento[3]
        print(f"[{i:3d}] real={etiqueta:4s} | SPAM -> {veredicto:12s}")
        print(f"       | {texto_norm[:60]}")
        print()

    spam_count = finales.count("SPAM")
    atipico_count = finales.count("SPAM_ATIPICO")
    ham_count = finales.count("HAM")

    print("-" * 60)
    print(f"SPAM         : {spam_count:3d} mensajes (estructura canónica)")
    print(f"SPAM_ATIPICO : {atipico_count:3d} mensajes (estructura no canónica)")
    print(f"HAM          : {ham_count:3d} mensajes")
    print(f"Total        : {len(finales):3d} mensajes")
    print()
    print("Nota: Los árboles de derivación del informe se construyen")
    print("sobre mensajes reales que SÍ cumplen la GLC (ej: mensajes")
    print("con secuencia [caps, text, contact] o [caps, caps, text, contact]).")
