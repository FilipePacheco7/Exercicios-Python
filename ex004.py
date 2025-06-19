# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input('Digite algo:\n')

print('Tipo primitivo da variável: {}'.format((type(var))))
print('Variável fornecida contém apenas espaços: {}'.format(var.isspace()))
print('Variável fornecida é um número: {}'.format(var.isnumeric()))
print('Variável fornecida é alfabética: {}'.format(var.isalpha()))
print('Variável fornecida é alfanumérica: {}'.format(var.isalnum()))
print('Variável fornecida está em maiúsculas: {}'.format(var.isupper()))
print('Variável fornecida está em minúsculas: {}'.format(var.islower()))
print('Variável fornecida está capitalizada: {}'.format(var.istitle()))
