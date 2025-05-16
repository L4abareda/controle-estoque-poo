from Produtos import Produto
from ProdutosAli import ProdAlimenticio
prod_ = []
def cad_prod():
    nome = input("Insira o nome do produto: ")
    preco = float(input("Insira o preco do produto: "))
    quantidade = int(input("Insira a quantidade do produto: "))
    return nome, preco, quantidade
def cad_prod_ali():
    nome, preco, quantidade = cad_prod()
    data_validade = input("Insira a data de validade do produto: ")
    return nome, preco, quantidade, data_validade

print("====MENU====")

opcao = int(input("\n 1.Cadastrar produto comum. \n 2.Cadastrar produto alimentício. \n 3.Listar todos os produtos. \n 4.Repor estoque. \n 5.Vender produto. \n 6.Sair : "))
while opcao != 4: 
    if opcao == 1:
        nome, preco, quantidade = cad_prod()
        produto = Produto(nome, preco, quantidade)
        prod_.append(produto)
        print("Produto cadastrado.")
        opcao = int(input("\n 1.Cadastrar produto comum. \n 2.Cadastrar produto alimentício. \n 3.Listar todos os produtos. \n 4.Repor estoque. \n 5.Vender produto. \n 6.Sair : "))    
    elif opcao == 2:
        nome, preco, quantidade, data_validade = cad_prod_ali()
        prod_ali = ProdAlimenticio(nome, preco, quantidade, data_validade)
        prod_.append(prod_ali)
        print("Produto alimentício cadastrado.")
        opcao = int(input("\n 1.Cadastrar produto comum. \n 2.Cadastrar produto alimentício. \n 3.Listar todos os produtos. \n 4.Repor estoque. \n 5.Vender produto. \n 6.Sair : "))
    elif opcao == 3:
        for produto in prod_:
            produto.exibir_produtos()
        opcao = int(input("\n 1.Cadastrar produto comum. \n 2.Cadastrar produto alimentício. \n 3.Listar todos os produtos. \n 4.Repor estoque. \n 5.Vender produto. \n 6.Sair : "))
    elif opcao == 4:
        produto_repor = input("Qual produto deseja repor: ")
        if produto_repor in prod_:
            produto_repor.repor_estoque()
        opcao = int(input("\n 1.Cadastrar produto comum. \n 2.Cadastrar produto alimentício. \n 3.Listar todos os produtos. \n 4.Repor estoque. \n 5.Vender produto. \n 6.Sair : "))
    elif opcao == 5:
        for produto in prod_:
            produto.vender_produto()
        opcao = int(input("\n 1.Cadastrar produto comum. \n 2.Cadastrar produto alimentício. \n 3.Listar todos os produtos. \n 4.Repor estoque. \n 5.Vender produto. \n 6.Sair : "))
    elif opcao == 6:
        print("Saindo...")

