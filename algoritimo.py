from classe import *

produtos = Produtos()
adm = Adm()
cliente = Cliente()
loja = Loja("LOJA DO CACIQUE", "Ácre", "11091945")


def voltar():
    limpar()
    print("Voltando...")
    pausar()


# --|Função dos menus|--////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def menucliente():
    limpar()
    print(f"---| BEM VINDO A {loja.nome} |---")
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
    print(f"---| BEM VINDO A {loja.nome} |---")
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
    adm.cadAdm("root", "root")
    while True:
        try:
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
                                    adm.cadAdm(nome, senha)
                                    print("Adm cadastrado com sucesso")
                                case 3:
                                    limpar()
                                    print("Adicionar Produto")
                                    nome = input("Nome do produto: ")
                                    valor = float(input("Valor do produto: "))
                                    descricao = input("Descrição do produto: ")
                                    produtos.AddProduto(nome, descricao, valor)
                                    print("Produto adicionado com sucesso")
                                    pausar()

                                case 4:
                                    limpar()
                                    print("Remover Produto")
                                    produtos.ListarProdutos()
                                    produtoRem = int(
                                        input(
                                            "Digite o numero do produto que deseja remover: "
                                        )
                                    )
                                    produtos.RemProdutos(produtoRem)
                                case 5:
                                    limpar()
                                    print("Remover Cliente")
                                    cliente.listar_Clientes()
                                    clienterem = int(
                                        (
                                            input(
                                                "Digite o numero do cliente que deseja remover: "
                                            )
                                        )
                                    )
                                    adm.DelCliente(clienterem)

                                case 6:
                                    limpar()
                                    print("Remover Adm")
                                    adm.listarAdm
                                    admrem = int(
                                        input(
                                            "Digite o numero do adm que deseja remover: "
                                        )
                                    )
                                    adm.delAdm(admrem)
                                    print("Adm removido com sucesso")
                                    pausar()
                                case 7:
                                    limpar()
                                    print("Listar Produtos")
                                    produtos.ListarProdutos()
                                    pausar()
                                case 8:
                                    limpar()
                                    print("Listar Clientes")
                                    cliente.listar_Clientes()
                                    pausar()
                                case 9:
                                    limpar()
                                    print("Listar Adms")
                                    adm.listarAdm()
                                    pausar()

                                case 10:
                                    voltar()
                                    break
                    elif cliente.logar_Cliente(nome, senha) == True:
                        while True:
                            menucliente()
                            opcCliente = int(input(">> "))
                            match opcCliente:
                                case 1:
                                    limpar()
                                    print("Produtos")
                                    produtos.ListarProdutos()
                                    pausar()
                                case 2:
                                    limpar()
                                    print("Adicionar ao Carrinho")
                                    print("Produtos")
                                    produtos.ListarProdutos()
                                    produto = int(
                                        input(
                                            "Digite o numero do produto que deseja adicionar ao carrinho: "
                                        )
                                    )
                                    cliente.AddCarrinho(produto)
                                    print("Produto adicionado ao carrinho com sucesso")
                                    pausar()
                                case 3:
                                    limpar()
                                    print("Ver Carrinho")
                                    cliente.ListCarrinho()
                                    pausar()
                                case 4:
                                    limpar()
                                    print("Excluir do Carrinho")
                                    cliente.ListCarrinho()
                                    produto = int(
                                        input(
                                            "Digite o numero do produto que deseja remover do carrinho: "
                                        )
                                    )
                                    cliente.RemCarrinho(produto)
                                    print("Produto removido do carrinho com sucesso")
                                    pausar()
                                case 5:
                                    voltar()
                                    break

                    else:
                        print("Nome ou senha incorretos")
                        pausar()
                case 2:
                    limpar()
                    print("Saindo....")
                    pausar()
                    exit()
        except Exception as e:
            print("erro")
