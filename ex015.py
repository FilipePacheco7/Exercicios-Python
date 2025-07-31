# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

carroKm = float(input("Digite a quilometragem percorrida:\n"))
carroDia = int(input("Digite a quantidade de dias alugados:\n"))

valorF = (60 * carroDia) + (0.15 * carroKm)

print("O valor do aluguel do carro vai custar R$ {:.2f}".format(valorF))