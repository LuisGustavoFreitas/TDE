soma= 0

# 10 primeiros numeros e a soma
for i in range(10):
    n = int(input(f'Digite o {i + 1}º número inteiro: '))
    soma+=n

# A media aritmetica
media= soma/10

print(f'A soma dos valores é: {soma}')
print(f'A media dos valores é: {media}')
