#Entrada
valortinta=  50
capacidadetinta= 5
pinturalitro= 3
alturacilindro= float(input("Qual a altura do cilindro:"))
raiocilindro= float(input("Qual o raio do cilindro:"))
umlitro= 3

#Desenvolvimento
areacilindro= 2 * 3.14 * raiocilindro * (alturacilindro + raiocilindro)
litrospintados= areacilindro / umlitro
quantidadelatas= litrospintados/capacidadetinta
valorreais= quantidadelatas * valortinta



print('A area do cilindro è:', areacilindro)
print('A quantidade de litros usados:' , litrospintados)
print('A quantidade de latas usadas:' , quantidadelatas)
print('O valor a pagar é:' , valorreais)



