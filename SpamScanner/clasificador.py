"""
SpamScanner 2.0 — Etapa 3: Clasificación por Peso Predictivo

Asigna pesos a tokens y clasifica como SPAM si la suma supera un umbral U.
Pesos: MONEY=3, PHONE=3, URL=2, CAPS=1, WORD=0
"""

PESOS = {
    "MONEY": 3,
    "PHONE": 3,
    "URL": 2,
    "CAPS": 1,
    "WORD": 0,
}


def clasificar(tokens, umbral):
    if puntuar(tokens) > umbral:
        return "SPAM"
    else:
        return "HAM"


def puntuar(tokens):
    suma = 0
    for t in tokens:
        peso = PESOS.get(t, 0)
        suma = suma + peso
    return suma


def evaluar(tokens_por_msj, etiquetas_reales, valores_u):
    resultados = []
    for u in valores_u:
        tp = fp = tn = fn = 0
        for tokens, real in zip(tokens_por_msj, etiquetas_reales):
            pred = clasificar(tokens, u)
            if pred == "SPAM" and real == "SPAM":
                tp += 1
            elif pred == "SPAM" and real == "HAM":
                fp += 1
            elif pred == "HAM" and real == "HAM":
                tn += 1
            elif pred == "HAM" and real == "SPAM":
                fn += 1
        total = tp + tn + fp + fn
        accuracy = (tp + tn) / total if total else 0
        precision = tp / (tp + fp) if (tp + fp) else 0
        recall = tp / (tp + fn) if (tp + fn) else 0
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall)
            else 0
        )
        resultados.append(
            {
                "U": u,
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1": f1,
                "tp": tp,
                "fp": fp,
                "tn": tn,
                "fn": fn,
            }
        )
    return resultados
