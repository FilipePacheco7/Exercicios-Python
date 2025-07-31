# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na
# tela o nome do escolhido.

import random

alunos = []

for i in range (4):
    aluno = input("Digite o nome do {}º aluno:\n".format(i+1))
    alunos.append(aluno)
sorteado = random.choice(alunos)
print("O aluno escolhido para apagar o quadro foi: {}".format(sorteado))
