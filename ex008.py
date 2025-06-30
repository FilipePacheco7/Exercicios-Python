# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medMetros = float(input("Digite a medida em metros:\n"))
medMili = medMetros * 1000
medCent = medMetros * 100
medDeci = medMetros * 10
medDeca = medMetros / 10
medHect = medMetros / 100
medQuil = medMetros / 1000

print("A Conversão da {} metros equivale a:".format(medMetros))
print("{} milímetros".format(medMili))
print("{} centímetros".format(medCent))
print("{} decímetros".format(medDeci))
print("{} decâmetros".format(medDeca))
print("{} hectômetros".format(medHect))
print("{} quilômetros".format(medQuil))