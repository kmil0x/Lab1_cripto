# -*- coding: utf-8 -*-

def descifrar_cesar(mensaje_cifrado):
    opciones_descifrado = []
    for desplazamiento in range(26):
        mensaje_descifrado = ""
        for caracter in mensaje_cifrado:
            if caracter.isalpha():
                codigo = ord(caracter)
                if caracter.islower():
                    codigo_descifrado = (codigo - ord('a') - desplazamiento) % 26 + ord('a')
                elif caracter.isupper():
                    codigo_descifrado = (codigo - ord('A') - desplazamiento) % 26 + ord('A')
                mensaje_descifrado += chr(codigo_descifrado)
            else:
                mensaje_descifrado += caracter
        opciones_descifrado.append(mensaje_descifrado)
    return opciones_descifrado

# Ingresa el mensaje cifrado
mensaje_cifrado = input("Ingrese el mensaje cifrado: ")

# Genera todas las opciones de descifrado para el mensaje cifrado dado
opciones_descifrado = descifrar_cesar(mensaje_cifrado)

# Imprime todas las opciones de descifrado
for i, opcion in enumerate(opciones_descifrado):
    print("Opción {}: {}".format(i+1, opcion))
