li=int(input('Digite o limite inicial:'))
lf=int(input('Digite o limite final:'))
print(f'Números múltiplos de 3 entre {li} e {lf} são:')

if li >= lf:
    print('Está dando erro, o limite inicial deve ser menor que o limite final!')
else:
    for i in range(li+1 , lf):
        if i % 3 == 0:
            print( i , end=',')
