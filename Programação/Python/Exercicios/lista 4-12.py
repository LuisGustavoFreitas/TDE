#Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente,utilizando a seguinte estratégia de ordenação:
#  • selecione o elemento do vetor de 20 posições que apresenta o menor valor;
#  • troque este elemento pelo primeiro;
#  • repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de menor valor com a segunda posição), depois os 18 elementos (trocando o de menor valor com a
#terceira posição), depois os 17, 16 e assim por diante, até restar um único elemento, o maior deles.

v= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(20):
    v[i] = int(input('Digite um numero: '))
v.sort
print(v)