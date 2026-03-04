curso = {
    "nome": "ASIBD",
    "duracao": '3 anos',
    "familia": "industrial",
    "ativo": True
}
print(curso)

# =================================================

modulos = dict([('nome', 'ADGBD'), ('Tipo', 'Tecnico/Tecnológico'), ('duracao', '60 Horas')])
print(modulos)

configuracoes = dict(host='localhost', port=8080, debug=False)
print(configuracoes)

# ==================================================================

# Criar um dicionário com o quadrado dos números de 0 a 4
quadrados = {x: x**2 for x in range(5)}

print(quadrados)
# Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# =================================================================

if "tipo" in curso:
# Usando pop()
tipo_removido = curso.pop("tipo")
print(f"Curso removido: {tipo_removido}")
print(f"{curso}")

# ========================================================
if "tipo" in curso:
    tipo_removido = curso.pop("tipo")
    print(f"Curso removido: {tipo_removido}")
    print(f"{curso}")
else:
    print(f"Esta chave nao existe")

# ================================================

# Iterando sobre as chaves (comportamento padrão)
for chave in curso:
    print(f"{chave}: {curso[chave]}")

# Iterando sobre os valores
for valor in curso.values():
    print(valor)

# Iterando sobre os pares chave-valor
for chave, valor in curso.items():
    print(f"{chave.capitalize()}: {valor}")

# ======================================================
chaves = curso.keys()
valores = curso.values()
itens = curso.items()

print(chaves)   
print(valores)  
print(itens)
