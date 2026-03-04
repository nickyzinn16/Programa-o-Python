import customers_management
import employee_management
import sales_management
import products_management

# ==============================================================
# ==================== Menu Principal ==========================
# ==============================================================

def main_menu():
    while True:
        print("\nProntiFika - Menu Principal")
        print("1 - Gestao de Colaboradores")
        print("2 - Gestao de Clientes")
        print("3 - Gestao de Produtos")
        print("4 - Gestao de Vendas")
        print("0 - Sair do Programa")

        option = input("Por favor escolha uma opcao: ")

        if option == "1":
            employee_menu()
        elif option == "2":
            customers_menu()
        elif option == "3":
            products_menu()
        elif option == "4":
            sales_menu()
        elif option == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opcao inserida eh invalida")


# ==============================================================
# ===================== Colaboradores ==========================
# ==============================================================

def employee_menu():
    while True:
        print("\nProntiFika - Menu Colaboradores")
        print("1 - Pesquisar")
        print("2 - Listar Colaboradores")
        print("3 - Registrar Colaborador")
        print("4 - Atualizar Colaboradores")
        print("5 - Eliminar Colaboradores")
        print("0 - Voltar")

        option = input("Por favor escolha uma opcao do SubMenu: ")

        if option == "1":
            employee_management.search_employee()
        elif option == "2":
            employee_management.list_employees()
        elif option == "3":
            employee_management.regist_employee()
        elif option == "4":
            employee_management.update_employee()
        elif option == "5":
            employee_management.delete_employee()
        elif option == "0":
            break
        else:
            print("Opcao inserida eh invalida")


# ==============================================================
# ===================== Clientes ===============================
# ==============================================================

def customers_menu():
    while True:
        print("\nProntiFika - Menu Clientes")
        print("1 - Pesquisar Cliente")
        print("2 - Listar Cliente")
        print("3 - Registrar Cliente")
        print("4 - Atualizar Cliente")
        print("5 - Eliminar Cliente")
        print("0 - Voltar")

        option = input("Por favor escolha uma opcao do SubMenu: ")

        if option == "1":
            customers_management.search_customers()
        elif option == "2":
            customers_management.list_customers()
        elif option == "3":
            customers_management.regist_customers()
        elif option == "4":
            customers_management.update_customers()
        elif option == "5":
            customers_management.delete_customers()
        elif option == "0":
            break
        else:
            print("Opcao inserida eh invalida")


# ==============================================================
# ===================== Produtos ===============================
# ==============================================================

def products_menu():
    while True:
        print("\nProntiFika - Menu Produtos")
        print("1 - Pesquisar Produto")
        print("2 - Listar Produtos")
        print("3 - Registrar Produtos")
        print("4 - Atualizar Produtos")
        print("5 - Eliminar Produtos")
        print("0 - Voltar")

        option = input("Por favor escolha uma opcao do SubMenu: ")

        if option == "1":
            products_management.search_products()
        elif option == "2":
            products_management.list_products()
        elif option == "3":
            products_management.regist_products()
        elif option == "4":
            products_management.update_products()
        elif option == "5":
            products_management.delete_products()
        elif option == "0":
            break
        else:
            print("Opcao inserida eh invalida")


# ==============================================================
# ==================== Vendas =================================
# ==============================================================

def sales_menu():
    while True:
        print("\nProntiFika - Menu Vendas")
        print("1 - Pesquisar Vendas")
        print("2 - Listar Vendas")
        print("3 - Registrar Vendas")
        print("4 - Atualizar Venda")
        print("5 - Eliminar Registro Venda")
        print("0 - Voltar")

        option = input("Por favor escolha uma opcao do SubMenu: ")

        if option == "1":
            sales_management.search_sales()
        elif option == "2":
            sales_management.list_sales()
        elif option == "3":
            sales_management.regist_sales()
        elif option == "4":
            sales_management.update_sales()
        elif option == "5":
            sales_management.delete_sales()
        elif option == "0":
            break
        else:
            print("Opcao inserida eh invalida")


# ==============================================================
# ===================== Execucao ===============================
# ==============================================================

if __name__ == "__main__":
    main_menu()

# enunciado sobre autenticacao