class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def exibir_produtos(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Preço do produto: {self.preco}")
        print(f"Quantidade do produto: {self.quantidade}")
    def vender_produto(self, quantidade_vender):
        if quantidade_vender <= 0:
            print("A quantidade para venda deve ser maior que zero.")
        if self.quantidade >= quantidade_vender:
            self.quantidade -= quantidade_vender
            print(f"{quantidade_vender} unidades de '{self.nome}' vendidas.")
            print(f"Estoque restante de '{self.nome}': {self.quantidade}")
        else:
            print(f"Estoque insuficiente de '{self.nome}'. Disponível: {self.quantidade}")

    def repor_estoque(self, quantidade_adicionar):
        quantidade_adicionar = int(input("Quanto deseja adicionar?: "))
        if quantidade_adicionar > 0:
            self.quantidade += quantidade_adicionar
            print(f"{quantidade_adicionar} unidades de '{self.nome}' adicionadas ao estoque.")
            print(f"Novo estoque de '{self.nome}': {self.quantidade}")
        else:
            print("A quantidade para reposição deve ser maior que zero.")
