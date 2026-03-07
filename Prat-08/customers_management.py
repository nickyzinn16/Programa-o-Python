import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="asibd",
        password="asibd#12",
        database="emp_management_db"
    )

# ====================================
# 1. Pesquisar
# ====================================
def search_customers():
    conexao = connect_db()
    cursor = conexao.cursor()

    customer_id = int(input(f"Id do cliente: "))

    sql_query = "SELECT * FROM customers WHERE id = %s"
    cursor.execute(sql_query, (customer_id,))

    result = cursor.fetchone()

    if result:
        print(f"Cliente encontrado: {result}")
    else:
        print(f"Cliente nao encontrado.")

    conexao.close()


# ====================================
# 2. Listar
# ====================================
def list_customers():
    conexao = connect_db()
    cursor = conexao.cursor()

    sql_query = "SELECT * FROM customers"
    cursor.execute(sql_query)

    customers_datas = cursor.fetchall()

    customers_list = []

    for each_line in customers_datas:
        customer = {
            "id": each_line[0],
            "first_name": each_line[1],
            "last_name": each_line[2],
            "email": each_line[3],
            "phone": each_line[4],
        }

        customers_list.append(customer)

    for customer in customers_list:
        print(f"Cliente: {customer}")

    conexao.close()


# ====================================
# 3. Registrar
# ====================================
def regist_customers():
    conexao = connect_db()
    cursor = conexao.cursor()

    first_name = input(f"Insira o primeiro nome: ")
    last_name = input(f"Insira o ultimo nome: ")
    email = input(f"Insira o email: ")
    phone = input(f"Insira o numero de telefone: ")

    sql_query = "INSERT INTO customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, email, phone)

    cursor.execute(sql_query, values)
    conexao.commit()

    print(f"Cliente registrado.")

    conexao.close()


# ====================================
# 4. Atualizar
# ====================================
def update_customers():
    conexao = connect_db()
    cursor = conexao.cursor()

    customer_id = int(input(f"Id do cliente: "))
    first_name = input(f"Insira o novo nome: ")

    sql_query = "UPDATE customers SET first_name = %s WHERE id = %s"
    cursor.execute(sql_query, (first_name, customer_id))
    conexao.commit()

    print(f"Cliente atualizado.")

    conexao.close()


# ====================================
# 5. Eliminar
# ====================================
def delete_customers():
    conexao = connect_db()
    cursor = conexao.cursor()

    customer_id = int(input(f"Id do cliente: "))

    sql_query = "DELETE FROM customers WHERE id = %s"
    cursor.execute(sql_query, (customer_id,))
    conexao.commit()

    print("Cliente eliminado.")

    conexao.close()