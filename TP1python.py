#Ejercicio 10
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
