#Entrada
a=float(input('Digite o primeiro numero:'))
b=float(input('Digite o segundo numero:'))
c=float(input('Digite o terceiro numero:'))

#Desenvolvimento
if a >= b and a >= c and b >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
if a >= b and a >=c and c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
if b >= a and b >= c and a >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
if b >= a and b >= c and c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
if c >= a and c >= b and a >=b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
if c >= a and c >= b and b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')