texto = "Ola mundo dos desafiadores"
resultado = ""

for letraA in texto:
    if letraA == "a" or letraA== "A":
        resultado += "_"
    else:
        resultado += letraA

print(f"{resultado}")
