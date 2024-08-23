#Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra
#um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
#usuário (sem repetição) e indique quantos acertos ele teve
from random import randint
acertos = 0
result = []
while len(result) != 6:
    r = randint(1, 60)
    if r not in result:
        result.append(r)
vu = []
while len(vu) != 6:
    r =int(input('Digite um numero: '))
    if r not in vu and r >= 0 and r <= 60:
        vu.append(r)
    for j in range(len(result)):
        if r == result[j]:
            acertos += 1
print('Resultado: ' , result)
print('Jogada do usuário: ' , vu)
print('Quantidade de acertos: ' , acertos)