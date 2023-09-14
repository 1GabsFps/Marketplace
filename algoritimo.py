import os
from classes import *

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
                    pausar()

                case 2:
                    limpar()
                    print("Area de fazer o login, o yuri faz depois")
                    print("[1] - Ver Produtos")
                    print("[2] - Adicionar ao Carrinho")
                    print("[3] - Ver Carrinho")
                    print("[4] - Voltar")
                    menu2 = int(input(">>"))

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

                        case 4:
                            limpar()
                            print("Voltando...")
                            pausar()
                            main()

                    pausar()

                case 3:
                    limpar()
                    print("Saindo...")
                    pausar()
                    break

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
    
