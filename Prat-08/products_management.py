import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="asibd",
        password="asibd#12",
        database="emp_management_db"
    )

# ====================================
# 1. Pesquisa
# ====================================
def search_products():
    conexao = connect_db()
    cursor = conexao.cursor()

    product_id = int(input(f"Id do produto: "))

    sql_query = "SELECT * FROM products WHERE id = %s"
    cursor.execute(sql_query, (product_id,))

    result = cursor.fetchone()

    if result:
        print(f"Produto encontrado: {result}")
    else:
        print(f"Produto nao encontrado.")

    conexao.close()


# ====================================
# 2. Listar
# ====================================
def list_products():
    conexao = connect_db()
    cursor = conexao.cursor()

    sql_query = "SELECT * FROM products"
    cursor.execute(sql_query)

    products_datas = cursor.fetchall()

    products_list = []

    for each_line in products_datas:
        product = {
            "id": each_line[0],
            "product_name": each_line[1],
            "price": each_line[2],
            "stock": each_line[3],
        }

        products_list.append(product)

    for product in products_list:
        print(f"{product}")

    conexao.close()


# ====================================
# 3. Registrar
# ====================================
def regist_products():
    conexao = connect_db()
    cursor = conexao.cursor()

    product_name = input(f"Nome do produto: ")
    price = float(input(f"Preco: "))
    stock = int(input(f"Quantidade em stock: "))

    sql_query = "INSERT INTO products (product_name, price, stock) VALUES (%s, %s, %s)"
    values = (product_name, price, stock)

    cursor.execute(sql_query, values)
    conexao.commit()

    print("Produto registado.")

    conexao.close()


# ====================================
# 4. Atualizar
# ====================================
def update_products():
    conexao = connect_db()
    cursor = conexao.cursor()

    product_id = int(input(f"Id do produto: "))
    product_name = input(f"Novo nome do produto: ")

    sql_query = "UPDATE products SET product_name = %s WHERE id = %s"
    cursor.execute(sql_query, (product_name, product_id))
    conexao.commit()

    print(f"Produto atualizado: {product_name}")

    conexao.close()


# ====================================
# 5. Eliminar
# ====================================
def delete_products():
    conexao = connect_db()
    cursor = conexao.cursor()

    product_id = int(input(f"Id do produto: "))

    sql_query = "DELETE FROM products WHERE id = %s"
    cursor.execute(sql_query, (product_id,))
    conexao.commit()

    print(f"Produto eliminado.")

    conexao.close()