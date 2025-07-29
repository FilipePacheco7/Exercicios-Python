# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário do funcionário:\nR$ "))
aumentoS = salario*(15/100)
salarioN = salario+aumentoS
print("O salário do funcionário que recebia R$ {:.2f}, com o aumento de 15%, passa a receber R$ {:.2f}".format(salario, salarioN))