frutas = ['Papaya', 'Banana', 'Maca', 'Uva', 'Pera', 'Morango', 'Papaya']

# list.append(x)
frutas.append(fruta)
print(f"{frutas[0:]}")


# list.extend(iterable)


# list.insert(i, x)
fruta = input("Insira o nomne da fruta que quer adicionar: ")
posicao = int(input("Insira a posicao da fruta que quer adicionar: "))
frutas.insert(posicao, fruta)
print(f"{frutas[0:]}")


# list.remove(x)
print(f"{frutas}")
fruta = input("Insira o nomne da fruta que quer remover: ")
frutas.remove(fruta)
print(f"{frutas[0:]}")


# list.pop([i])
print(f"{frutas}")
fruta = input("Insira o nome da fruta que quer remover: ")
indice = frutas.index(fruta)
frutas.pop(indice)
print(f"{frutas}")


# list.clear()
 frutas.clear()
 print(f"{frutas[0:]}")


# list.index(x[, start[, end]])


# list.count(x)
 papayas = frutas.count('Papaya')
 print(f"{papayas}")


# list.reverse()
frutas.reverse()
print(f"{frutas}")


# list.copy()
novasFrutas = frutas.copy()
print(f"Novas frutas: {novasFrutas}")  
