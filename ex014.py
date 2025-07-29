# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempC = float(input("Digite a temperatura em graus Celsius Cº:\n"))
tempF = (tempC * 9/5) + 32
print("Conversão de Celsius para Fahrenheit:")
print("{:.1f} Cº -> {:.1f} Fº".format(tempC, tempF))