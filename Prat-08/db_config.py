# Crie um arquivo chamado dbconfig.py que contém o nome da base de dados, 
# o host ,nome do utilizador a utilizar e a palavra-passe do mesmo, 
# e disponibiliza uma função initConnection que inicia a conexão com a base de dados.

import mysql.connector

db_host = "localhost"
db_user = "asibd"
db_password = "asibd#12"
db_name = "emp_management_db"

def connection():
    return 
        conexao = mysql.connector.connect(
            host = db_host
            user = db_user,
            password = db_password,
            database = db_name
        )
    )

cursor = conexao.cursor()