# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:30:26 2020

@author: Pablo Bolaños Gallego
"""
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
print("BIENVENIDO A MI CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto a cifrar: ").upper()
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27): "))

texto_cifrado = ""
texto_descifrado = ""
for l in texto_claro:
    if l in abecedario:
        pos_letra = abecedario.index(l)
        nueva_pos = (pos_letra + clave) % len(abecedario)
        texto_cifrado+= abecedario[nueva_pos]
    else:
        texto_cifrado+= l
for l in texto_cifrado:
    if l in abecedario:
        pos_letra = abecedario.index(l)
        nueva_pos = (pos_letra - clave) % len(abecedario)
        texto_descifrado+= abecedario[nueva_pos]
    else:
        texto_descifrado+= l
print("\nEl mensaje cifrado es:", texto_cifrado)
print("\nEl mensaje descifrado es: ",texto_descifrado)