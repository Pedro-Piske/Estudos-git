produtos = []
categoria = []
movimentacoes = []

def cp(id, nome, categoria, quantidade, preco, localizacao):
    nproduto = {
        'id': id,
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco,
        'localizacao': localizacao
    }
    produtos.append(cp)
    print("Produto cadastrado com sucesso")

cp(1, 'peruca', 'acessorios', 4, 1000, 'estoque')

def cc(eletrodomesticos,)