# Vemos primero un ejemplo de como plantear las funciones de
# Encriptado y desencriptado

"""
def encriptar(texto):
    print("El texto a encriptar es: " + texto)
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    print('Texto encriptado: ' + textoFinal)


def desencriptar(texto):
    print("El texto a desencriptar es: " + texto)
    textoFinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    print('Texto desencriptado: ' + textoFinal)

encriptar('prueba de texto')
print("\n")
desencriptar('pxrxuxexbxax xdxex xtxexxxtxox')
"""

# Vamos ahora con la encriptación de un texto

def encriptar(texto):
    print("El texto a encriptar es: " + texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal


def desencriptar(texto):
    print("El texto a desencriptar es: " + texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)
    return textoFinal



def encriptarArchivo(rutaArchivo):
    # Primero leemos el archivo de texto
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    # Y hacemos el reemplazo
    archivo = open(rutaArchivo, "w")
    archivo.write(textoEncriptado)
    archivo.close()
    print("Encriptación realizada con éxito")


def desencriptarArchivo(rutaArchivo):
    # Primero leemos el archivo de texto
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    # Y hacemos el reemplazo
    archivo = open(rutaArchivo, "w")
    archivo.write(textoDesencriptado)
    archivo.close()
    print("Desencriptación realizada con éxito")

# Ahora vamos a permitir que el usuario elija que archivo es el que quiere
# encriptar a través de la consola de Python

respuestaEoD = input("Presione 'E' para encriptar, u otra cosa para desencriptar: ")
rutaArchivo = input("Ingrese la ruta del archivo: ")

if respuestaEoD == "E":
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)

