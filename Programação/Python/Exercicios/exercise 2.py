#A partir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe
#a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer a carteira
#de motorista ou não, informando sua situação.

#Entrada
anonascimento = int(input('Digite seu ano de nascimento:'))
ano=2023

#Desenvolvimento
idade=ano - anonascimento
print('Sua idade é:' , idade)
if idade >= 18:
    print('Voce tem 18 anos e pode tirar a carteira!!')
if idade < 18:
    print('Voce não tem 18 anos e não pode tirar a carteira!!')
