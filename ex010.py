# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# ATENÇÃO: No momento qu estou realizando esse exercício, um dólar está valendo R$ 5,48

s = float(input("Digite o valor do seu saldo em Reais:\nR$ "))
d = 5.48
quantD = s / d
print("Com seu saldo de R$ {:.2f} reais, você pode comprar US$ {:.2f} dólares".format(s, quantD))
