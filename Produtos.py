class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def exibir_produtos(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Preço do produto: {self.preco}")
        print(f"Quantidade do produto: {self.quantidade}")
