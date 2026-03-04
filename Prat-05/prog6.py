# Programa que o utilizador escolhe oque remover da lista
print(f"Frutas: Papaya, Banana, Maca, Uva, Pera, Morango")

fruta = input("Insira o nomne da fruta que quer remover: ")
frutas = ['Papaya', 'Banana', 'Maca', 'Uva', 'Pera', 'Morango']

# Remove a fruta da lista
frutas.remove(fruta)

print(f"{frutas[0:]}")