# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:46:05 2020

@author: Pablo Bolaños Gallego
"""


print('Bienvenido a emparejando.com')
print('\nNecesitamos saber información sobre ti.')
nombre=input('¿Cuál es tu nombre?: ')
año=int(input('Año de nacimiento: '))
actual=int(2020)
taburete=input('¿Te gusta Taburete?: ')
edad=actual - año
print('Te llamas ' + nombre + ' y tienes' ,int(edad),'años')
if taburete in('s','S','si','Si'):
    boomer='\nOK Boomer, lo tuyo va a ser un caso difícil.'
elif taburete in('n','N','no','No'):
    boomer='\nBueno, al menos es un comienzo. Veremos qué se puede hacer contigo.'
print (boomer)
num=1
while (num<edad):
    print('Que no cumple',int(num))
    num=num+1
print('¡Qué sí cumple',int(num),'!')

lista=(nombre,edad,año)
for dato in lista:
    print (dato)