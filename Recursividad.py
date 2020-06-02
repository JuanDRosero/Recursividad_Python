# -*- coding: utf-8 -*-
"""
Codigo calculo cesantias
Created on Tue Jun  2 13:40:15 2020

@author: Juan David Rosero Torres - 20181020071
"""

valorCesantias = lambda x,y : 0.0 if(y==0) else (float(100/12) *x) + valorCesantias(x, y-1)

print("Bienvenido al programa para calcular el valor de las cesantias disponibles")
salario= input("Ingrese el salario que usted posee ")
mes= input("Ingrese los meses que ha trabajado ")
print("Su valor de sesantias es $"+str(valorCesantias(float(salario), int(mes))))  