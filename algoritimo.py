import os
from classe import *


def voltar():
    limpar()
    print("Voltando...")
    pausar()


# --|Função dos menus|--////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def menucliente():
    limpar()
    print("[1] - Ver Produtos")
    print("[2] - Adicionar ao Carrinho")
    print("[3] - Ver Carrinho")
    print("[4] - Voltar")


def menuadm():
    limpar()
    print("[7] - Ver Produtos")
    print("[8] - Adicionar Produto")
    print("[9] - Remover Produto")
    print("[10] - Voltar")


def menuprincipal():
    limpar()
    print("Bem vindo a Loja do Cacique")
    print("[1] - Cadastro")
    print("[2] - Login")
    print("[3] - Sair")
    print("Digite o numero equivalente a opção que deseja")


def addProdutos():
    limpar()
    print("Adicionando Produtos")
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    produto = (nome, valor)
    produto.addProduto(produto)
    print("Produto adicionado com sucesso")
    pausar()


def verProdutos():
    limpar()
    print("Produtos")
    print(f"Nome: {Produtos.getNome()} - Valor: {Produtos.getValor()}")
    pausar()


def removerProdutos():
    limpar()
    print("Removendo Produtos")
    print("Produtos")
    print(f"Nome: {Produtos.getNome()} - Valor: {Produtos.getValor()}")
    produto = input("Digite o nome do produto que deseja remover: ")
    produto.removerProduto(Produtos)
    print("Produto removido com sucesso")
    pausar()


def addCarrinho():
    limpar()
    print("Adicionando ao Carrinho")
    print("Produtos")
    print(f"Nome: {Produtos.getNome()} - Valor: {Produtos.getValor()}")
    produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
    produto.addCarrinho(Produtos)
    print("Produto adicionado ao carrinho com sucesso")
    pausar()


def verCarrinho():
    limpar()
    print("Carrinho")
    print(f"Nome: {Produtos.getNome()} - Valor: {Produtos.getValor()}")
    pausar()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def main():
    while True:
        try:
            limpar()
            menuprincipal()
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
                        while True:
                            menucliente()
                            menu2 = int(input(">>"))
                            match menu2:
                                case 1:
                                    verProdutos()

                                case 2:
                                    addCarrinho()

                                case 3:
                                    verCarrinho()

                                case 4:
                                    voltar()
                                    break

                    elif cliente.nome == "adm" and cliente.senha == "adm":
                        while True:
                            menuadm()
                            menu2 = int(input(">>"))
                            match menu2:
                                case 7:
                                    verProdutos()

                                case 8:
                                    addProdutos()

                                case 9:
                                    removerProdutos()

                                case 10:
                                    voltar()
                                    break
                    else:
                        print("Valor invalido")
                        pausar()

                case 3:
                    voltar()
                    break

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            pausar()
