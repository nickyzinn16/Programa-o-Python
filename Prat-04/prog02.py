import os 

# Apresentar o caminho onde o utilizador esta
print(os.getcwd())

# Listagem de todos os diretorios na pasta atual
print(f"{os.listdir()}")

# Criar uma nova pasta
print(f"{os.mkdir("demo")}")

# se trata do processo de verificacao de existencia de um arquivo
if os.path.exists("test.txt"):
    print(f"O arquivo existe")

# os.path.isdir("")
# os.path.isfile("")

os.system("") 
#serve para executar arquivos ou gerir modulois. 

