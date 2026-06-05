#El administrador de redes de la facultad necesita su ayuda. Les entregó un archivo de texto llamado
#servidores.txt que contiene un listado enorme de direcciones IP y nombres de equipos. Sin embargo,
#muchas de las líneas están comentadas (comienzan con el símbolo #) porque esos equipos están
#dados de baja, o simplemente son líneas en blanco. Construyan un script que lea este archivo y
#genere uno nuevo llamado activos.txt que contenga únicamente los servidores en funcionamiento.
#Recuerden cómo abrir archivos en modo lectura y escritura, y cómo iterar sobre ellos.

with open("servidores.txt", "r") as archivo_lectura:
    with open("activos.txt", "w") as archivo_escritura:
        for linea in archivo_lectura:
            linea = linea.strip()
            if linea != "" and not linea.startswith("#"):
                archivo_escritura.write(linea + "\n")