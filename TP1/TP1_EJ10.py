#Imaginen que el sistema de alumnos recibió inscripciones a las mesas de exámenes, pero los
# nombres ingresados tienen un formato caótico. Algunos están en mayúsculas, otros en minúsculas
# y muchos contienen espacios extra innecesarios al principio o al final de la cadena. Escriban una
# función que reciba uno de estos strings desordenados y lo devuelva en formato "Título" (solo la
# primera letra en mayúscula), eliminando cualquier espacio sobrante en los extremos. Exploren los
# métodos nativos que los objetos string de Python ya nos ofrecen para limpiar y transformar texto sin
# usar librerías externas. 

def transformar(nombre):
    resultado = ""
    mayuscula = True

    for i in nombre:
        if i == " ":
            resultado += i
            mayuscula = True
        else:
            if mayuscula:
                resultado += i.upper()
                mayuscula = False
            else:
                resultado += i.lower()
    return resultado

nombre_usuario = input("Escribi tu nombre completo: ")

nombre_formateado = transformar(nombre_usuario)

print("Nombre en formato titulo:", nombre_formateado)
