from Classe import *

produtos = Produtos()
cliente = Cliente()
adm = Adm("root", "root")


def voltar():
    limpar()
    print("Voltando...")
    pausar()


# --|Função dos menus|--////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def menucliente():
    limpar()
    print("---| BEM VINDO A LOJA DO CACIQUE |---")
    print(" [1] - Ver Produtos")
    print(" [2] - Adicionar ao Carrinho")
    print(" [3] - Ver Carrinho")
    print(" [4] - Excluir do Carrinho")
    print(" [5] - Voltar")


def menuadm():
    limpar()
    print("---| OPÇÕES DE GERENCIAMENTO ADM |---")
    print(" [1] - Cadastrar Cliente")
    print(" [2] - Cadastrar Adm")
    print(" [3] - Adicionar Produto")
    print(" [4] - Remove Produto")
    print(" [5] - Remover Cliente")
    print(" [6] - Remover Adm")
    print(" [7] - Listar Produto")
    print(" [8] - Listar Clientes")
    print(" [9] - Litar Adms")
    print(" [10] - Voltar")


def menuprincipal():
    limpar()
    print("---| BEM VINDO A LOJA DO CACIQUE |---")
    print(" [1] - Login")
    print(" [2] - Sair")
    print("Digite o numero equivalente a opção que deseja")


def addProdutos():
    limpar()
    print("Adicionando Produtos")
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    produtos.AddProduto(nome, valor)
    print("Produto adicionado com sucesso")
    pausar()
    limpar()


def verProdutos():
    limpar()
    print("Produtos")
    produtos.ListarProdutos()
    pausar()


def removerProdutos():
    limpar()
    print("Removendo Produtos")
    print("Produtos")
    produtos.ListarProdutos()
    produtoRem = int(input("Digite o numero do produto que deseja remover: "))
    produtos.RemProdutos(produtoRem)
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
        limpar()
        menuprincipal()
        menu = int(input(">> "))

        match menu:
            case 1:
                limpar()
                print("Login")
                nome = input("Nome: ")
                senha = input("Senha: ")
                if adm.verifyAdm(nome, senha) == True:
                    while True:
                        menuadm()
                        opcao = int(input(">> "))
                        match opcao:
                            case 1:
                                limpar()
                                print("Cadastrar Cliente")
                                nome = input("Nome: ")
                                senha = input("Senha: ")
                                cliente.add_Cliente(nome, senha)
                            case 2:
                                limpar()
                                print("Cadastrar Adm")
                                nome = input("Nome: ")
                                senha = input("Senha: ")

                elif cliente.logar_Cliente() == True:
                    while True:
                        menucliente()
                else:
                    print("Login invalido")
                    pausar()
                    limpar
            case 2:
                limpar()
                print("Saindo....")
                pausar()
                exit()
