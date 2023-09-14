import os
from classe import *

def main():
    while True:
        try:
            os.system("cls")
            print("Bem vindo a Loja do Cacique")
            print("[1] - Cadastro")
            print("[2] - Ver Produtos")
            print("[3] - Ver Carrinho")
            print("[4] - Sair")
            print("Digite o numero equivalente a opção que deseja")
            menu = int(input(">> "))

            match menu:
                case 1:
                    os.system("cls")
                    os.system("pause")  

                case 2:
                    os.system("cls")
                    os.system("pause")

                case 3:
                    os.system("cls")
                    os.system("pause")

                case 4:
                    os.system("cls")
                    print("Saindo...")
                    os.system("pause")
                    break

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
    
