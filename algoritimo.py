import os
from classe import *

def main():
    while True:
        try:
            os.system("cls")
            print("Bem vindo")
            print("[1] - ")
            print("[2] - ")
            print("[3] - ")
            print("[4] - ")
            print("Digite o numero equivalente a opção que deseja")
            menu = int(input(">> "))

            match menu:
                case 1:
                    os.system("cls")
                    os.system("pause")

                case 2:
                    pass

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
    