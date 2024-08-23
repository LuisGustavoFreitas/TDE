print()
print("="*28)
print(' Seja bem vindo ao meu quiz ')
print('='*28)
print()
playing= input(' Você quer jogar? ')

if playing.lower() != 'sim':
    quit()

print('Ok,vamos jogar')
score=0

resposta= input(' Quanto é 2 X 2? ')
if resposta.lower() == '4':
    print('Certa resposta')
    score += 1
else:
    print('Resposta incorreta')

resposta= input(' Quanto è 5 X 5? ')
if resposta.lower() == '25':
    print('Certa resposta')
    score += 1
else:
    print('Resposta incorreta')

resposta= input(' Qual a raiz quadrada de 4? ')
if resposta.lower() == '2':
    print('Certa resposta')
    score += 1
else:
    print('Resposta incorreta')
print('Você acertou ' + str(score) + ' perguntas!')
print('Você acertou ' + str((score / 3) * 100) + ' %  das perguntas!')


