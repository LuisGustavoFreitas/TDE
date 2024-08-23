nota= float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota+nota2)/2
if media >= 6:
    print('Voce foi aprovado. Sua media foi de: ' ,media)
if media < 6:
    print('Voce foi reprovado. Sua media foi de:' , media)
