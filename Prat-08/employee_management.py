# ====================================
#           1. Pesquisar
# ====================================
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "asibd",
    password = "asibd#12",
    database = "emp_management_db",
)

cursor = conexao.cursor()

employee_id = int(input("Id do funcionario: "))

sql_query = "DELETE FROM employees SET WHERE id = %s"

cursor.execute(sql_query, (employee_id,))
conexao.commit()



# ====================================
#           2. Listar
# ====================================
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "asibd",
    password = "asibd#12",
    database = "emp_management_db",
)

cursor = conexao.cursor()

sql_query = 'SELECT * FROM employees'
cursor.execute(sql_query)

employees_datas = cursor.fetchall()
print(f'{employees_datas}')

employees_list = []

for each_line in employees_datas:
    employee = {
        "id": each_line[0],
        "first_name": each_line[1],
        "last_name": each_line[2],
        "email": each_line[3],
        "phone": each_line[4],
    }

    employees_list.append(employee)

    print(f'{employees_list}')



# ====================================
#           3. Registrar
# ====================================
 import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "asibd",
    password = "asibd#12",
    database = "emp_management_db",
)

cursor = conexao.cursor()

first_name = input("Insira o primeiro nome: ")
last_name = input("Insira o ultimo nome: ")
email = input("Insira o email: ")
phone_number = input("Insira o numero de telefone: ")

sql_query = "INSERT INTO employees (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
values = (first_name, last_name, email, phone_number)
cursor.execute(sql_query, values)
conexao.commit()



# ====================================
#           4. Atualizar
# ====================================
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "asibd",
    password = "asibd#12",
    database = "emp_management_db",
)

cursor = conexao.cursor()

employee_id = int(input("Id do funcionario: "))
first_name = input("Insira o nome a atualizar: ")

sql_query = "UPDATE employees SET first_name = %s WHERE id = %s"

cursor.execute(sql_query, (first_name, employee_id))
conexao.commit()



# ====================================
#           5. Elminar
# ====================================
import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "asibd",
    password = "asibd#12",
    database = "emp_management_db",
)

cursor = conexao.cursor()

employee_id = int(input("Id do funcionario: "))

sql_query = "DELETE FROM employees SET WHERE id = %s"

cursor.execute(sql_query, (employee_id,))
conexao.commit()