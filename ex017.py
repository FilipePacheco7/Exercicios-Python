# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo. Calcule
# e mostre o comprimento da hipotenusa.

import math

oposto = float(input("Digite o comprimento do cateto oposto:\n"))
adjacente = float(input("Digite o comprimento do cateto adjacente:\n"))
hipotenusa = (adjacente**2 + oposto**2) ** (1/2)
print("O comprimento da hipotenusa é de {:.2f}".format(hipotenusa))