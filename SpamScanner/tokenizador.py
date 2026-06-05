"""
SpamScanner 2.0 — Etapa 2: Tokenización con Expresiones Regulares

Tokens:
  MONEY: cifras precedidas o terminadas por $, £ o €
  URL:   patrones de enlace (www.x.com, http://...)
  PHONE: secuencias numéricas de 7+ dígitos
  CAPS:  palabras de 3+ letras completamente en mayúsculas
  WORD:  cualquier otra palabra
"""

import re

RE_MONEY = re.compile(r"\b[\$£€]\d+(?:\.\d+)?\b|\b\d+(?:\.\d+)?[\$£€]\b")
RE_URL = re.compile(
    r"\bhttps?://[^\s]+|www\.[^\s]+|[a-zA-Z0-9.-]+\.(?:com|org|net|edu|gov|uk|es|mx|ar)\b"
)
RE_PHONE = re.compile(r"\b\d{7,}\b")
RE_CAPS = re.compile(r"\b[A-Z]{3,}\b")


def tokenizar(texto_normalizado):
    tokens = []
    for palabra in texto_normalizado.split():
        if RE_URL.search(palabra):
            tokens.append("URL")
        elif RE_MONEY.search(palabra):
            tokens.append("MONEY")
        elif RE_PHONE.fullmatch(palabra):
            tokens.append("PHONE")
        elif RE_CAPS.fullmatch(palabra):
            tokens.append("CAPS")
        else:
            tokens.append("WORD")
    return tokens
