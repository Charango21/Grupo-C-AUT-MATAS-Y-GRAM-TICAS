# Escribir una expresión regular que valide una dirección de mail según estas reglas:
# • Nombre de usuario: letras mayúsculas, minúsculas, números y solo los caracteres
# especiales guion medio ( - ) y guion bajo ( _ ).
# • Debe haber exactamente un símbolo @ separando usuario y dominio.
# • Dominio: solo letras mayúsculas, minúsculas y números (sin caracteres especiales).
# • Extensión: entre 2 y 4 letras (ej: .com, .org, .edu, .info).

import re

def validar_mail(email):
    patron = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$"
    return bool(re.match(patron, email))

EMAIL=input("Ingrese email: ")
print(validar_mail(EMAIL))