from random import randint
from time import sleep
pontos_player_1 = 0
pontos_player_2 = 0
pontos_player = 0
pontos_computador = 0
pontos_computador_1=0
pontos_computador_2=0

print()
print('Seja Bem-vindo ao Jokenpô!!')
print()
print('Escolha o modo de jogo.')
print("""
[1] - Player X Player
[2] - Player X Computador
[3] - Computador X Computador
""")
modo_de_jogo = int(input('Qual o modo de jogo você deseja: '))
jogar_denovo = 'sim'
while jogar_denovo == 'sim':
    if modo_de_jogo == 1:
        print("""Jogadas possíveis: 
[1] - Pedra
[2] - Papel
[3] - Tesoura
""")
        player_1 = int(input('Escolha sua jogada player 1: '))
        print("\n" * 130) 
        print("""Jogadas possíveis: 
[1] - Pedra
[2] - Papel
[3] - Tesoura
""")
        player_2 = int(input('Escolha sua jogada player 2: '))
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('pô')
        print('jogada do player 1:', player_1)
        print('jogada do player 2:', player_2)
        if player_1 == player_2 :
                print('Empate!')
        elif player_1 == 1:
            if player_2 == 2:
                print('Player 2 ganhou!')
                pontos_player_2 += 1
            elif player_2 == 3:
                print('Player 1 ganhou!')
                pontos_player_1 += 1
        elif player_1 == 2:
            if player_2 == 1:
                print('Player 1 ganhou!')
                pontos_player_1 += 1
        elif player_2 == 3:
            print('Player 2 ganhou!')
            pontos_player_2 += 1
        elif player_1 == 3:
            if player_2 == 1:
                print('Player 2 ganhou!')
                pontos_player_2 += 1
        elif player_2 == 2:
            print('Player 1 ganhou!')
            pontos_player_1 += 1
        elif player_1 and player_2 != '1' '2' '3':
            print('Jogada inválida!Jogue novamente')
        jogar_denovo = input('Querem jogar denovo? ')
        if jogar_denovo.lower == 'sim':
            print('Ok!')
            print('Os pontos do player 1 foram:  {}'.format(pontos_player_1))
            print('Os pontos do player 2 foram:  {}'.format(pontos_player_2))
    if modo_de_jogo == 2:
        opcoes= ['pedra' , 'papel' ,'tesoura']
        computador= randint(1 , 3 )
        print('''Jogadas possíveis:
[1] Pedra
[2] Papel
[3] Tesoura
''')
        player=int(input('Digite sua jogada player: '))
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('pô')
        print('jogada do player:', player,)
        print('jogada do computador', computador)
        if computador == player:
            print('Empate!')
        elif computador == 1:
            if player == 2:
                print('Player ganhou!')
                pontos_player += 1
            elif player ==3:
                print('Computador ganhou!')
            pontos_computador += 1
        elif computador == 2:
            if player == 1:
                print('Computador ganhou!')
                pontos_computador += 1
            elif player == 3:
                print('Player ganhou!')
            pontos_player += 1
        elif computador == 3:
            if player == 1:
                print('Player ganhou!')
                pontos_player += 1
            elif player == 2:
                print('Computador ganhou!')
            pontos_computador += 1
        elif player and computador != '1' '2' '3':
            print('Jogada inválida!Jogue novamente')
        jogar_denovo = input('Querem jogar denovo? ')
        if jogar_denovo.lower == 'sim':
            print('Ok!')
            print('Os pontos do player foram:  {}'.format(pontos_player))
            print('Os pontos do computador foram:  {}'.format(pontos_computador))
    if modo_de_jogo == 3:
        opcoes= ['pedra' , 'papel' ,'tesoura']
        computador_1= randint (1 , 3 )
        computador_2= randint ( 1 ,3 )
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('pô')
        print('Jogada do computador 1:', computador_1)
        print('Jogada do computador 2:', computador_2)
        if computador_1 == computador_2:
            print('Empate!')
        elif computador_1 == 1:
            if computador_2 == 2:
                print('Computador 2 ganhou!')
                pontos_computador_2+= 1
            elif computador_2 ==3:
                print('Computador 1 ganhou!')
            pontos_computador_1 += 1
        elif computador_1 == 2:
            if computador_2 == 1:
                print('Computador 1 ganhou!')
                pontos_computador_1 += 1
            elif computador_2 == 3:
                print('Computador 2 ganhou!')
            pontos_computador_2 += 1
        elif computador_1 == 3:
            if computador_2 == 1:
                print('Computador 2 ganhou!')
                pontos_computador_2 += 1
            elif computador_2 == 2:
                print('Computador 1 ganhou!')
            pontos_computador_1 += 1 
        jogar_denovo = input('Querem jogar denovo? ')
        if jogar_denovo.lower == 'sim':
            print('Ok!')
            print('Os pontos do computador 1 foram:  {}'.format(pontos_computador_1))
            print('Os pontos do computador 2 foram:  {}'.format(pontos_computador_2))