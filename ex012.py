# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input("Digite o preço do produto:\nR$ "))
desconto = valor * 0.05
valorFinal = valor - desconto
print("O valor do produto com 5% de desconto vai custar R$ {:.2f}".format(valorFinal))