# -*- coding: utf-8 -*-
from scapy.all import IP, ICMP, Raw, send

def enviar_caracter_icmp(caracter, numero_paquete):
    # Obtener el byte menos significativo y más significativo del caracter
    byte_menos_significativo = ord(caracter) & 0xFF
    byte_mas_significativo = (ord(caracter) >> 8) & 0xFF
    
    # Calcular el número de bytes adicionales necesarios para llegar a 48 bytes
    bytes_adicionales = 48- 2 # 2 bytes para el caracter
    if bytes_adicionales > 0:
        # Crear una cadena de bytes adicionales, puedes personalizarla como desees
        datos_adicionales = bytearray([i for i in range(bytes_adicionales)])
    else:
        datos_adicionales = b''
    
    # Construir el paquete ICMP Echo Request con el caracter y los IDs únicos
    paquete = IP(dst="8.8.8.8") / ICMP(type=8, id=numero_paquete, seq=numero_paquete) / bytearray([byte_menos_significativo, byte_mas_significativo]) / Raw(load=datos_adicionales)
    
    # Enviar el paquete y mostrar el resumen junto con el número de paquete
    send(paquete, verbose=True)
    print("Paquete {}: {}".format(numero_paquete, paquete.summary()))

def enviar_mensaje_icmp(mensaje):
    for i, caracter in enumerate(mensaje, start=1):
        enviar_caracter_icmp(caracter, i)

# Ingresa el mensaje a enviar
mensaje = input("Ingrese el mensaje a enviar: ")

# Enviar cada caracter del mensaje en paquetes ICMP Echo Request
enviar_mensaje_icmp(mensaje)
