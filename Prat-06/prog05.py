tupla_dos_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

def operations(tupla_dos_numeros):
    pares = [n for n in tupla if n % 2 == 0]   
    soma = sum(pares)

return soma 

operacoes = operations(tupla_dos_numeros)

print(f"Soma dos pares: {operacoes[0]}")
print(f"Multiplicacao dos pares: {operacoes[1]}")
print(f"Subtracao dos pares: {operacoes[2]}")