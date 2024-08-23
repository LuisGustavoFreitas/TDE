#A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a
#massa em kg de um boxeador e mostre a qual categoria ele pertence. Caso ele não se
#encaixe, informe “Categoria inferior a Super-médio”. Lembrando que 1 quilograma =
#2,20462262 libras

#Entrada
peso=float(input('Digite seu peso: '))

#Desenvolvimento
if peso>=91.1:
    print('Categoria Peso-pesado')
if peso>=79.8 and peso<=90.7:
    print('Categoria Cruzador')
if peso>=76.6 and peso<=79.3:
    print('Categoria Meio-pesado')
if peso>=73.02 and peso<=76.2:
    print('Categoria Super-médio')
if peso<73.02:
    print('Categoria Inferior a Super-médio')
