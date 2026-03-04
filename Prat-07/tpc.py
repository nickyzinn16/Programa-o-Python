# 1 - Crie um dicionario para representar as informações dos cursos (dois cursos) da eicm-gdc

cursos = [
    {
        "nome": "ASIBD",
        "descricao": "ASIBD é um curso de Administração de Sistemas Informáticos e Base de Dados.",
        "duracao": "3 anos",
        "familia": "Informática",
        "tipo": "Profissional",
        "lema": "Tecnologia e Informatica",
        "perfil_entrada": [
            "Positiva em Matemática",
            "Interesse por TICs",
            "Raciocínio lógico"
        ],
        "perfil_saida": [
            "Trabalhar em departamentos de informática",
            "Administrador de Base de Dados",
            "Técnico de Sistemas Informáticos"
        ],
        "unidades_competencias": [
            "Instalar e configurar sistemas",
            "Gerir bases de dados",
            "Administrar redes"
        ],
        "modulos": [
            {
                "nome": "Gestão de Redes",
                "abbv": "GR",
                "duracao": "60 H",
                "objetivo": "Compreender e aplicar conceitos de redes de computadores.",
                "descricao": "Configuração e administração de redes locais.",
                "competencias": "Configurar, manter e solucionar problemas em redes.",
                "data_inicio": "01-10-2025",
                "data_fim": "30-11-2025",
            },
            {
                "nome": "Programação",
                "abbv": "PRG",
                "duracao": "90 H",
                "objetivo": "Compreender e aplicar conceitos de programação",
                "descricao": "Aprender a programar em linguagens como Python e Java.",
                "competencias": "Parte prática de programação, desenvolvimento de projetos e resolução de problemas.",
                "data_inicio": "6-02-2026",
                "data_fim": "04-06-2026",  
            }
        ],
    },
    {
        "nome": "Construção Civil",
        "descricao": "Curso de Construção Civil, focado em técnicas e práticas de construção.",
        "duracao": "3 anos",
        "familia": "Construção",
        "tipo": "Profissional",
        "lema": "Construção e Engenharia",
        "perfil_entrada": [
            "Positiva em Matemática",
            "Criatividade",
            "Interesse por Construção"
        ],
        "perfil_saida": [
            "Engenheiro Civil",
            "Arquiteto",
            "Técnico de Construção"
        ],
        "unidades_competencias": [
            "Planejar e executar projetos de construção",
            "Gerir obras e equipes",
            "Aplicar normas de segurança na construção"
        ],
        "disciplinas": [
            {
                "nome": "Conceitos Básicos de Construção",
                "abbv": "CBC",
                "duracao": "3 trimestres",
                "objetivo": "Aprender os fundamentos da construção civil.",
                "descricao": "Introdução aos materiais de construção, técnicas de construção e segurança.",
                "competencias": "Conhecimento dos materiais, técnicas de construção e normas de segurança.",
                "data_inicio": "01-10-2025",
                "data_fim": "10-06-2026",
            }
        ],
    },
]

# 2 - Crie um dicionário com informações de produto, pretende-se adicionar novos produtos com novas configurações de chaves
let produtos = [
    {
        id: 1,
        nome: "Laptop HP",
        preco: 85000,
        stock: 10,
        categoria: "Informática",
        marca: "HP",
        desconto: 10
    }
]

console.log(produtos)

let id_produto = prompt("Insira o ID do novo produto: ")
let nome = prompt("Insira o nome do novo produto: ")
let preco = prompt("Insira o preço do novo produto: ")
let stock = prompt("Insira a quantidade em stock: ")
let categoria = prompt("Insira a categoria do produto: ")
let marca = prompt("Insira a marca do produto: ")
let desconto = prompt("Digite o desconto (%): ")

let novo_produto = {
    id: id_produto,
    nome: nome,
    preco: preco,
    stock: stock,
    categoria: categoria,
    marca: marca,
    desconto: desconto
}

produtos.push(novo_produto)

console.log("Lista atualizada de produtos:")
console.log(produtos)


# 3 - Escreva uma função que recebe uma listas de palavras e retorna um dicionário onde as chaves são as 
# palavras dessa lista e os valores são o número de vezes que essa palavra aparece na lista 
# (dicionário não pode ter chave repetida)


# 4 - Criar dois exercícios é criar mais dois enunciados a partir do anterior
Crie um programa que receba do usuário uma lista de pelo menos 5 palavras. O programa deve: 
Armazenar apenas as palavras que possuem pelo menos 4 letras “a”.
Organizar essas palavras em ordem decrescente, do maior número de letras “a” para o menor.
Exibir a lista final para o usuário.

Crie um programa que possui um dicionário com uma palavra-chave, que é de extrema importância. O usuário tentará descobrir essa palavra-chave através de dicas fornecidas. O programa deve funcionar da seguinte forma:
- A cada tentativa do usuário:
- Se ele acertar, o programa parabeniza o usuário e termina.
- Se ele errar, o programa fornece uma nova dica sobre a palavra-chave (uma nova letra da palavra)
- O usuário terá um número limitado de tentativas, sendo 5 vezes
- Se o usuário não descobrir a palavra-chave após o número máximo de tentativas, o programa revela a palavra correta.
