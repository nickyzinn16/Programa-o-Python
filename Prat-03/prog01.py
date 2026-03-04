# prog que pede dois numers e presenta a potencia do primeiro para o segundo
import math

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

potencia = math.pow(num1, num2)
raiz1 = math.sqrt(num1)
raiz2 = math.sqrt(num2)

print(f"A potência eh: ", potencia)
print(f"A raiz quadrada do 1 nuemros eh: ", raiz1)
print(f"A raiz quadrada do 2 nuemros eh: ", raiz2)