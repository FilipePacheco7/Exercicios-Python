# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Digite a largura da parede em metros:\n"))
h = float(input("Digite a altura da parede em metros:\n"))
area = l * h
rendTinta = 2
quantTinta = area / rendTinta
print("Com base na área de {:.2f} m². Será necessário {:.2f} litro(s) de tinta para pintar a parede.".format(area, quantTinta))

