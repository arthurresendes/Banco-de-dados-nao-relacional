from querys import insercao
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
        
        if escolha_insercao == 2:
            while True:
                try:
                    quantidade = int(input("Quantas pessoas quer adicionar: "))
                    if isinstance(quantidade,int):
                        break
                except:
                    print("Digite um numero inteiro valido!!")
            for _ in range(quantidade):
                nome = input("Digite o nome da pessoa: ")
                try:
                    salario  = float(input("Digite o salario da pessoa: "))
                except:
                    print("Digite um salario valido")
                insercao(nome,salario)
                print("Pessoa cadastrada com sucesso !!")
            main()
    elif escolha_opcao == 2:
        pass
    elif escolha_opcao == 5:
        print("=== Saindo ===")
        sys.exit(0)


main()