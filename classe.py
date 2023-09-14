class Carrinho_Compras:
    lista_compra = []
    def inserir_produto(self, produto):
        self.produto = produto
        self.lista_compra.append(self.produto)

    def listar_produtos(self):
        for produto in self.lista_compra:
            print(f"Nome: {produto.getNome()} - Valor: {produto.getValor()}")

    def getLista(self, vetor):
        return self.lista_compra[vetor]
    
    def delProduto(self, vetor):
        self.lista_compra.pop(vetor)

class Produtos:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def getNome(self):
        return self.nome
    
    def getValor(self):
        return self.valor
