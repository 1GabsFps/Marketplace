import os

def parar():
    os.system('pause')

def limpar():
    os.system('cls')

class Carrinho_Compras:
    lista_Compra = []

    def add_Produtos(self, produto):
        self.produto = produto
        self.lista_Compra.append(produto)

    def getLista(self, vetor):
        return self.lista_Compra(vetor)
    
    def remover_Produtos(self, vetor):
        self.vetor = vetor - 1
        self.add_Produtos.pop(vetor)

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def getNome(self):
        return self.nome
    
    def getPreco(self):
        return self.preco
    
class Clientes(Produto, Carrinho_Compras):
    clientes = []
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def add_Cliente(self, cliente):
        self.cliente = cliente
        self.cliente.append(cliente)

    def remover_cliente(self, vetor):
        self.vetor = vetor - 1
        self.clientes.pop(vetor)

    def getNome(self):
        return self.nome
    
    def getSenha(self):
        return self.senha
    
    def setNome(self):
        self.nome = nome

    def setSenha(self):
        self.senha = senha
