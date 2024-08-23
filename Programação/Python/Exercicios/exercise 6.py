#endo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2 -
#feminino) elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as
#seguintes fórmulas:
#a. para homens: p = (72.7 * h) - 58
#b. para mulheres: p = (62.1 * h) - 44.7

#Entrada

print("="*20)
print("    PESO IDEAL")
print("="*20)
print()
altura=float(input('Digite sua altura:'))
print("""Você é:
[1] Homem
[2] Mulher
""")
opcao=int(input('Informe a opção:'))

#Desenvolvimento

if opcao == 1:
    pesoidealh=(72.7*altura)-58
    print('Seu peso ideal é:',pesoidealh)
if opcao == 2:
    pesoidealm=(62.1*altura)-44.7
    print('Seu peso ideal é:' , pesoidealm)