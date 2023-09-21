import os


def limpar():
    os.system("cls")


def pausar():
    os.system("pause")


class Loja:
    def __init__(self, nome, endereço, cnpj):
        self.nome = nome
        self.endereço = endereço
        self.cnpj = cnpj


class Produtos:
    def AddProduto(self, nome, desc, valor):
        self.nome = nome
        self.valor = valor
        self.desc = desc
        self.descs = []
        self.produtos = []
        self.preco = []
        self.produtos.append(nome)
        self.preco.append(valor)
        self.descs.append(desc)

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
                f" Produto: {self.produtos.index(self.produtos[i])} ----Nome: {self.produtos[i]} -----Desc: {self.descs[i]}----Valor: {self.preco[i]}"
            )
            i += 1

    def RemProdutos(self, produto):
        del self.produtos[produto]
        del self.preco[produto]
        del self.descs[produto]


class Adm:
    def cadAdm(self, nome, senha):
        self.adms = [
            "root",
        ]
        self.adms.append(nome)
        self.admsSenha = [
            "root",
        ]
        self.admsSenha.append(senha)

    def verifyAdm(self, nome, senha):
        if nome in self.adms and senha in self.admsSenha:
            return True
        else:
            return False

    def listarAdm(self):
        i = 0
        for i in range(len(self.adms)):
            print(f" Index: {i} Nome: {self.adms[i]} - Senha: {self.admsSenha[i]}")
            i += 1

    def delAdm(self, adm):
        if adm == 0:
            print("Não é possivel remover o adm root")
        else:
            del self.admsSenha[adm]
            del self.adms[adm]
        if adm >= len(self.adms):
            print("Não existe esse adm")

    def DelCliente(self, cliente):
        del self.clientes[cliente]
        del self.clienteSenha[cliente]
        if cliente >= len(self.clientes):
            print("Não existe esse cliente")
        else:
            print("Cliente removido com sucesso")


class Cliente(Produtos):
    def add_Cliente(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.clientes = []
        self.clienteSenha = []
        self.clientes.append(nome)
        self.clienteSenha.append(senha)

    def listar_Clientes(self):
        self.cont = 0
        for cliente in self.clientes:
            self.cont += 1
            print(f"Nome: {cliente.getNome()} - Senha: {cliente.getSenha()}")

    def logar_Cliente(self, nome, senha):
        if nome in self.clientes and senha in self.clienteSenha:
            return True
        else:
            return False

    def deslogar_Cliente(self):
        for cliente in self.clientes:
            if self.nome == cliente.getNome() and self.senha == cliente.getSenha():
                print("Deslogado com sucesso")
                return True
            else:
                print("Erro ao deslogar")
                return False

    def AddCarrinho(self, produto):
        self.listacarrinho = []
        self.listacarrinho.append(self.produtos[produto])
        self.listacarrinhopreço = []
        self.listacarrinhopreço.append(self.preco[produto])

    def ListCarrinho(self):
        self.cont = 0
        for i in self.listacarrinho:
            self.cont += 1
            print(
                f"Nome: {self.listacarrinho[self.cont]} - Valor: {self.listacarrinhopreço[self.cont]}"
            )

    def RemCarrinho(self, vetor):
        del self.listacarrinho[vetor]
        del self.listacarrinhopreço[vetor]
