hora1 = int (input("Me informa o primeiro horário:"))
min1 = int(input("Me informe os minutos:"))
hora2 = int (input ("Me informe o segundo horário:"))
min2 = int(input (" Me informe os minutos:"))

soma1= hora1 + hora2
soma2= min1 + min2

if soma2 >=60:
    soma1=soma1+1
    soma2 = soma2-60
if soma1 >12:
    soma1= soma1-12
if soma1>24:
    soma1=soma1-24

print ("A saida é igual a:",soma1, soma2)








