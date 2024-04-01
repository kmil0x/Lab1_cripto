# -*- coding: utf-8 -*-

def cifrado_cesar(texto, clave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            # Determinar si el caracter es mayúscula o minúscula
            mayuscula = caracter.isupper()
            # Obtener el índice en el alfabeto y aplicar el desplazamiento
            indice = (ord(caracter) - ord('A' if mayuscula else 'a') + clave) % 26
            # Convertir el nuevo índice de nuevo a caracter
            nuevo_caracter = chr(ord('A' if mayuscula else 'a') + indice)
            resultado += nuevo_caracter
        else:
            # Si no es una letra, mantener el caracter sin cambios
            resultado += caracter
    return resultado

# Solicitar al usuario ingresar el texto y la clave
texto_original = input("Ingrese el texto a cifrar: ")
clave = int(input("Ingrese corrimiento (número entero): "))

# Cifrar el texto ingresado por el usuario
texto_cifrado = cifrado_cesar(texto_original, clave)

# Mostrar el resultado
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
