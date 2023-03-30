#solicita dois números inteiros de um ou dois algarismos
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

#checa o primeiro algarismo do número digitado e se for subtrai 7 unidades, assim deixando somente o segundo algarismo
if num1 // 10 == 7:
    num1 -= 70

#checa o segundo algarismo do número digitado e se for 7 subtrai 7 dezenas, fazendo com que o número termine em zero ao ínves de 7
if num1 % 10 == 7:
    num1 -=  7

#repetindo o processo com o segundo número
if num2 // 10 == 7:
    num2 -= 70
if num2 % 10 == 7:
    num2 -= 7

#cacula a soma dos números substituindo o 7 por 0 no resultado
soma = num1 + num2

#faz um processo igual ao feito no num1 e no num2
if soma // 10 == 7:
    soma -= 70
if soma % 10 == 7:
    soma -= 7   

print(soma)    

