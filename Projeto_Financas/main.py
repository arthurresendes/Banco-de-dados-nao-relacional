from querys import insercao,deletar,atualizar,valores_salario,ver_info_or,maior,menor
import sys

def menu():
    print("1 - Inserir")
    print("2 - Visualizar")
    print("3 - Deletar")
    print("4 - Atualizar")
    print("5 - Sair")

def submenu_insercao():
    print("1 - Inserir um só")
    print("2 - Inserir Muitos")

def submenu_deletar():
    print("1 - Deletar um só")
    print("2 - Deletar Muitos")
    
def submenu_atualizar():
    print("1 - Atualizar um só")
    print("2 - Atualizar Muitos")

def submenu_buscar():
    print("1 - Ver de salario X até Y (EX: 100 ate 2000)")
    print("2 - Ver informações de uma ou outra pessoa (Ex: Arthur ou Maria)")
    print("3 - Pessoa com maior aporte de investimento")
    print("4 - Pessoa com menor aporte de investimento")

def main():
    print("="*50)
    print("--- Bem vindo ao controle de finanças ---")
    print("="*50)
    
    menu()
    while True:
        try:
            escolha_opcao = int(input(": "))
            if escolha_opcao > 0 and escolha_opcao < 6:
                break
            else:
                print("Escolha um numero de 1 até 4")
        except:
            print("Erro encontrado, digite numeros validos")
    
    # ==================== INSERIR =======================
    if escolha_opcao == 1:
        submenu_insercao()
        while True:
            try:
                escolha_insercao = int(input(": "))
                if escolha_insercao > 0 and escolha_insercao < 3:
                    break
                else:
                    print("Escolha 1 ou 2")
            except:
                print("Erro encontrado, digite numeros validos")
        
        if escolha_insercao == 1:
            nome = input("Digite o nome da pessoa: ")
            while True:
                try:
                    salario  = float(input("Digite o salario da pessoa: "))
                    if isinstance(salario,float):
                        break
                except:
                    print("Digite um salario valido")
            insercao(nome,salario)
            print("Pessoa cadastrada com sucesso !!")
            main()
        
        elif escolha_insercao == 2:
            while True:
                try:
                    quantidade = int(input("Quantas pessoas quer adicionar: "))
                    if isinstance(quantidade,int):
                        break
                except:
                    print("Digite um numero inteiro valido!!")
            for i in range(quantidade):
                nome = input(f"Digite o nome da {i+1} pessoa: ")
                try:
                    salario  = float(input("Digite o salario da pessoa: "))
                except:
                    print("Digite um salario valido")
                insercao(nome,salario)
                print("Pessoa cadastrada com sucesso !!")
            main()

    # ============= BUSCA ======================
    elif escolha_opcao == 2:
        submenu_buscar()
        while True:
            try:
                escolha_busca = int(input(": "))
                if escolha_busca > 0 and escolha_busca < 5:
                    break
                else:
                    print("Escolha 1 até 4")
            except:
                print("Erro encontrado, digite numeros validos")
        
        if escolha_busca == 1:
            while True:
                try:
                    salario1  = float(input("Digite o salario minimo: "))
                    salario2  = float(input("Digite o salario maximo: "))
                    if isinstance(salario1,float) and isinstance(salario2, float):
                        break
                except:
                    print("Digite um valores validos")
            print(valores_salario(salario1,salario2))
            main()
        
        elif escolha_busca == 2:
            nome1 = input(f"Digite o nome da 1 pessoa: ")
            nome2 = input(f"Digite o nome da 2 pessoa: ")
            print(ver_info_or(nome1,nome2))
            main()
    
        elif escolha_busca == 3:
            print(maior())
            main()

        elif escolha_busca == 4:
            print(menor())
            main()

    # ========================== Deletar ==============================
    elif escolha_opcao == 3:
        submenu_deletar()
        while True:
            try:
                escolha_deletar = int(input(": "))
                if escolha_deletar > 0 and escolha_deletar < 3:
                    break
                else:
                    print("Escolha 1 ou 2")
            except:
                print("Erro encontrado, digite numeros validos")
        
        if escolha_deletar == 1:
            nome = input("Digite o nome da pessoa: ")
            print(deletar(nome))
            main()
        
        elif escolha_deletar == 2:
            while True:
                try:
                    quantidade = int(input("Quantas pessoas quer deletar: "))
                    if isinstance(quantidade,int):
                        break
                except:
                    print("Digite um numero inteiro valido!!")
            for i in range(quantidade):
                nome = input(f"Digite o nome da {i+1} pessoa: ")
                deletar(nome)
            main()
    
    # =============================== Atualizar =============================
    elif escolha_opcao == 4:
        submenu_atualizar()
        while True:
            try:
                escolha_atualizar = int(input(": "))
                if escolha_atualizar > 0 and escolha_atualizar < 3:
                    break
                else:
                    print("Escolha 1 ou 2")
            except:
                print("Erro encontrado, digite numeros validos")
        
        if escolha_atualizar == 1:
            nome = input("Digite o nome da pessoa a atualizar: ")
            while True:
                try:
                    salario  = float(input("Digite o salario da pessoa: "))
                    if isinstance(salario,float):
                        break
                except:
                    print("Digite um salario valido")
            print(atualizar(nome,salario))
            main()
        
        elif escolha_atualizar == 2:
            while True:
                try:
                    quantidade = int(input("Quantas pessoas quer atualizar: "))
                    if isinstance(quantidade,int):
                        break
                except:
                    print("Digite um numero inteiro valido!!")
            for i in range(quantidade):
                nome = input(f"Digite o nome da {i+1} pessoa: ")
                try:
                    salario  = float(input("Digite o salario da pessoa: "))
                except:
                    print("Digite um salario valido")
                print(atualizar(nome,salario))
            main()

    else:
        print("=== Saindo ===")
        sys.exit(0)


main()