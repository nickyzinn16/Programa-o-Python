# Area de solicitacacao de dados dos users
#============================================
nome = input("Insira seu nome: ") #nome
idade = int(input("Insira sua idade: ")) #idade
altura = float(input("Insira sua altura: ")) #altura
morada = input("Insira sua morada: ") #morada
#===========================================

# Apresentacao do tipo de dados de cada variavel!!
#===========================================

#print(type(nome))
#print(type(idade))
#print(type(altura))
#print(type(morada))

#print(f"O nome inserido foi: {nome}\n Idade foi: {idade}\n Altura foi: {altura}\n Morada: {morada}")
#print("Nome: {} - Idade: {} - Altura: {} - Morada: {}". format(nome, idade, altura, morada))
print("Idade: {1} - Nome: {0} - Altura: {2} - Morada: {3}". format(nome, idade, altura, morada))
#print("Nome: %d - Idade: %s - Altura: %f - Morada: %s". format(nome, idade, altura, morada)) -- nao usar
