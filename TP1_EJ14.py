# El departamento de historia está digitalizando documentos antiguos, pero el sistema generó mucha
# "basura" alrededor de los datos importantes en el documento de texto. Les pidieron extraer todas las
# fechas mencionadas en un párrafo extenso. Saben que las fechas buscadas están escritas siempre
# en el formato estricto DD/MM/YYYY. Escriban un programa utilizando el módulo re que busque y
# devuelva una lista con todas las ocurrencias que coincidan con este formato dentro del texto masivo.
# Investiguen qué función específica de las expresiones regulares en Python sirve para encontrar y
# extraer múltiples coincidencias.
# Input de ejemplo:
# "El acta original fue redactada el 15/04/1815 y posteriormente ratificada el 09/07/1816 en la
# asamblea. Se descartó por completo el borrador del 2/5/1814 por falta de firmas."
# Output esperado:
# ['15/04/1815', '09/07/1816']. 

import re

def extraer_fechas(texto):
    patron = r"(?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[0-2])/\d{4}"
    return re.findall(patron, texto)

TEXTO = input("Ingrese texto para extraer fechas en el formato DD/MM/YYYY: ")
print(extraer_fechas(TEXTO))
