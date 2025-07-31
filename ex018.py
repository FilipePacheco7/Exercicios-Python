# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angGraus = int(input("Digite um ângulo:\n"))
angRadiano = math.radians(angGraus)



print("Seno de {}º -> {:.2f}".format(angGraus, math.sin(angRadiano)))
print("Cosseno de {}º -> {:.2f}".format(angGraus, math.cos(angRadiano)))
print("Tangente de {}º -> {:.2f}".format(angGraus, math.tan(angRadiano)))
