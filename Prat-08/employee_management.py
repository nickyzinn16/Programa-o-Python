import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="asibd",
        password="asibd#12",
        database="emp_management_db"
    )

# ====================================
#           1. Pesquisar
# ====================================
def search_employee():
    conexao = connect_db()
    cursor = conexao.cursor()

    employee_id = int(input("Id do funcionario: "))

    sql_query = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(sql_query, (employee_id,))

    result = cursor.fetchone()

    if result:
        print("Funcionario encontrado:")
        print(result)
    else:
        print("Funcionario nao encontrado.")

    conexao.close()


# ====================================
#           2. Listar
# ====================================
def list_employees():
    conexao = connect_db()
    cursor = conexao.cursor()

    sql_query = "SELECT * FROM employees"
    cursor.execute(sql_query)

    employees_datas = cursor.fetchall()

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

    for employee in employees_list:
        print(employee)

    conexao.close()

# ====================================
#           3. Registrar
# ====================================
def regist_employee():
    conexao = connect_db()
    cursor = conexao.cursor()

    first_name = input("Insira o primeiro nome: ")
    last_name = input("Insira o ultimo nome: ")
    email = input("Insira o email: ")
    phone = input("Insira o numero de telefone: ")

    sql_query = "INSERT INTO employees (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, email, phone)
    cursor.execute(sql_query, values)
    conexao.commit()

    print("Funcionario registrado.")

    conexao.close()


# ====================================
#           4. Atualizar
# ====================================
def update_employee():
    conexao = connect_db()
    cursor = conexao.cursor()

    employee_id = int(input("Id do funcionario: "))
    first_name = input("Insira o nome a atualizar: ")

    sql_query = "UPDATE employees SET first_name = %s WHERE id = %s"
    cursor.execute(sql_query, (first_name, employee_id))
    conexao.commit()

    print("Funcionario atualizado.")

    conexao.close()


# ====================================
#           5. Elminar
# ====================================
def delete_employee():
    conexao = connect_db()
    cursor = conexao.cursor()

    employee_id = int(input("Id do funcionario: "))

    sql_query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(sql_query, (employee_id,))
    conexao.commit()

    print("Funcionario eliminado.")

    conexao.close()