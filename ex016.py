# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

v = float(input("Digite um valor:\n"))
vInt = int(v)
print("O valor {} tem a parte inteira {}.".format(v,vInt))