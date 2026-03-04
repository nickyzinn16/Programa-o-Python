# Crie um programa que pede a data de nascimento do usuario, 
# e apartir dessa data, calcule a idade do usuario.
import datetime
dataatual = datetime.date.today()

ano2 = dataatual.year
nascim = input("Insira a sua data de nascimento (Exemplo 90/12/2008): ")
nascim = datetime.datetime.strptime(nascim, "%d/%m/%Y")

anoAtual = datetime.datetime.now().year

ano = nascim.year

idade = ano2 - ano

print(f"Voce tem {idade} anos.")
