from Produtos import Produto
class ProdAlimenticio(Produto):
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.__data_validade = data_validade
    def exibir_produtos(self):
        super().exibir_produtos()
        print(f"Data de validade do produto: {self.__data_validade}")

