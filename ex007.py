# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a primeira nota:\n"))
n2 = float(input("Digite a segunda nota:\n"))
m = (n1+n2) / 2
print("Média do aluno: {:.2f}".format(m))