# operacao com numeros: prg que pede 2 numeros e apressento soma, subtracao, multiplicacao, 
#divisao inteira e normal e resto do resto, e fazer Exponenciação entre primeiro e segundo numero. 
#E validacao

num1 = int(input(f"Insira o primeiro numero: "))
num2 = int(input(f"Insira o segundo numero: "))

soma = num1 + num2        
subtracao = num1 - num2  
multiplicacao = num1 * num2
divisao = num1 / num2  
diviInteira = num1 // num2 
exponenciacao1 = num1 ** 2
exponenciacao2 = num2 ** 2

print(f"Soma: {soma}\n Subtração: {subtracao}\n Multiplicação: {multiplicacao}\n Divisão Inteira: {diviInteira}\n Divisão: {divisao}\n Exponenciação de {num1}: {exponenciacao1}\n Exponenciação de {num2}: {exponenciacao2}")