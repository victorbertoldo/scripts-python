'''
    Exemplo de uso de funções:
    A primeira possui parametro obrigatório e outra não.

    Parâmetros obrigatórios são aqueles que são esperados entre parenteses nas funções.

'''

produtos = [] # lista vazia, será preenchida com todos os itens

# Função para cadastrar produtos na lista 'produtos'

def cadastrarProduto(produto):
    global produtos
    produtos.append(produto)

# Função que mostra os produtos na lista 'produtos'
def listarProdutos():
    global produtos
    for p in produtos: # iteração para percorrer toda a lista de produtos
        print(p)

produto = ""   # variavel, não confundir com a lista

while produto != "sair":
    produto = input("Digite o nome do produto para cadastrar:")
    cadastrarProduto(produto)
    print("Produtos cadastrados com sucesso.")
    listarProdutos()
