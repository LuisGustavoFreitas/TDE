#A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
#máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
#inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
#fornecido.

def calcularAmplitudeAmostral(vetor):
    valorMaximo = max(vetor)
    valorMinimo = min(vetor)
    amplitudeAmostral = valorMaximo - valorMinimo
    return valorMaximo , valorMinimo , amplitudeAmostral

vetor = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)
maximo, minimo, amplitude = calcularAmplitudeAmostral(vetor) 

print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
print("Amplitude amostral:", amplitude)