# prog que pede data nascimento e apresenta o dia, mes e ano separado
import datetime

nascim = input("Insira a sua data de nascimento (Exemplo 90/12/2008): ")

data = datetime.datetime.strptime(nascim, "%d/%m/%Y")

dia = data.day
mes = data.month
ano = data.year

print("dia:", dia)
print("mes:", mes)
print("ano:", ano)

