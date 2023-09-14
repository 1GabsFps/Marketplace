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

