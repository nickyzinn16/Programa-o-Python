# crie uma funcao que recebe dois numeros e retorne: a soma, subtracao e multiplicacao desses
def operacoes(a, b):
    return a + b, a - b, a * b

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = operacoes(num1, num2)
lista = list(resultado)

# usando o resultado da funcao operacoes, quero converter os valores recebidos como tuplo em lista

print(f"{resultado}")
print(f"{lista}")





