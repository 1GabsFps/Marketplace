import os
from classe import *

def main():
    while True:
        try:
            limpar()
            print("Bem vindo a Loja do Cacique")
            print("[1] - Cadastro")
            print("[2] - Login")
            print("[3] - Sair")
            print("Digite o numero equivalente a opção que deseja")
            menu = int(input(">> "))

            match menu:
                case 1:
                    limpar()
                    print("--|Cadastrar Cliente|--")
                    nome = input("Nome: ")
                    senha = input("Senha: ")
                    cliente = Cliente(nome, senha)
                    cliente.add_Cliente(cliente)
                    print("Cliente cadastrado com sucesso")
                    pausar()

                case 2:
                    limpar()
                    print("--|Login|--")
                    nome = input("Nome: ")
                    senha = input("Senha: ")
                    cliente = Cliente(nome, senha)
                    cliente.logar_Cliente()
                    if cliente.logar_Cliente() == True:
                        while  True:
                            print("[1] - Ver Produtos")
                            print("[2] - Adicionar ao Carrinho")
                            print("[3] - Ver Carrinho")
                            print("[4] - Voltar")
                            menu2 = int(input(">>"))
                            match menu2:
                                case 4:
                                    limpar()
                                    print("Voltando...")
                                    pausar()
                                    break
                            while True:
                                match menu2:
                                    case 1:
                                        limpar()
                                        pausar()
                            
                                    case 2:
                                        limpar()
                                        pausar()

                                    case 3:
                                        limpar()
                                        pausar()
                    else:
                        print("Valor invalido")
                        pausar()

                case 3:
                    limpar()
                    print("Saindo...")
                    pausar()
                    break

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            pausar()