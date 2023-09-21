import os


def limpar():
    os.system("cls")


def pausar():
    os.system("pause")


class Carrinho_Compras:
    lista_compra = []

    def AddCarrinho(self, produto):
        self.produto = produto
        self.lista_compra.append(produto)

    def ListCarrinho(self):
        self.cont = 0
        for produto in self.lista_compra:
            self.cont += 1
            print(f"Nome: {produto.getNome()} - Valor: {produto.getValor()}")

    def getLista(self, vetor):
        return self.lista_compra(vetor)

    def RemCarrinho(self, vetor):
        self.vetor = vetor - 1
        self.lista_compra.pop(vetor)


class Produtos:
    def AddProduto(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.produtos = []
        self.preco = []
        self.produtos.append(nome)
        self.preco.append(valor)

    def getNome(self):
        return self.nome

    def getValor(self):
        return self.valor

    def getProdutos(self):
        return self.produtos

    def ListarProdutos(self):
        i = 0
        for i in range(len(self.produtos)):
            print(
                f" Produto: {self.produtos.index(self.produtos[i])} ----Nome: {self.produtos[i]} ----Valor: {self.preco[i]}"
            )
            i += 1

    def RemProdutos(self, produto):
        self.produto = produto
        del self.produtos[produto]
        del self.preco[produto]


class Cliente(Produtos, Carrinho_Compras):
    def add_Cliente(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.clientes = []
        self.clienteSenha = []
        self.clientes.append(nome)
        self.clienteSenha.append(senha)

    def getNome(self):
        return self.nome

    def getSenha(self):
        return self.senha

    def listar_Clientes(self):
        self.cont = 0
        for cliente in self.clientes:
            self.cont += 1
            print(f"Nome: {cliente.getNome()} - Senha: {cliente.getSenha()}")

    def logar_Cliente(self):
        for cliente in self.clientes:
            if self.nome == cliente.getNome() and self.senha == cliente.getSenha():
                print("Logado com sucesso")
                return True
            else:
                print("Erro ao logar")
                return False

    def deslogar_Cliente(self):
        for cliente in self.clientes:
            if self.nome == cliente.getNome() and self.senha == cliente.getSenha():
                print("Deslogado com sucesso")
                return True
            else:
                print("Erro ao deslogar")
                return False


class Adm:
    def __init__(self, user, senha):
        self.user = user
        self.senha = senha

    def cadCliente(self, cliente):
        pass

    def cadProduto(self, produto):
        pass

    def cadAdm(self, nome, senha):
        self.adms = []
        self.adms.append(nome)
        self.admsSenha = []
        self.admsSenha.append(senha)

    def verifyAdm(self, nome, senha):
        for i in range(len(self.adms)):
            if nome == self.adms[i] and senha == self.admsSenha[i]:
                return True
            else:
                return False

    def listarAdm(self):
        i = 0
        for i in range(len(self.adms)):
            print(f" Index: {i} Nome: {self.adms[i]} - Senha: {self.admsSenha[i]}")
            i += 1

    def delAdm(self, adm):
        del self.adms[adm]
        del self.admsSenha[adm]
