# Armazenamento de dados
produtos = {}           # Dicionário para armazenar produtos pelo código
movimentacoes = []      # Lista para armazenar movimentações

# Função para cadastrar produto
def cadastrar_produto(codigo, nome, categoria, preco, quantidade=0, preco_desconto=0):
    if codigo in produtos:
        print(f"Produto com código {codigo} já existe.")
    else:
        produto = {
            "codigo": codigo,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "preco_desconto": preco_desconto,
            "quantidade": quantidade
        }
        produtos[codigo] = produto
        print(f"Produto {nome} cadastrado com sucesso.")

# Função para consultar produto
def consultar_produto(codigo):
    produto = produtos.get(codigo)
    if produto:
        return {
            "Código": produto["codigo"],
            "Nome": produto["nome"],
            "Categoria": produto["categoria"],
            "Preço": produto["preco"],
            "Preço com Desconto": produto["preco_desconto"],
            "Quantidade em Estoque": produto["quantidade"]
        }
    else:
        return "Produto não encontrado."

# Função para obter o preço de venda (considerando o desconto)
def obter_preco(produto):
    return produto["preco_desconto"] if produto["preco_desconto"] > 0 else produto["preco"]

# Função para registrar venda
def vender_produto(codigo, quantidade):
    produto = produtos.get(codigo)
    if not produto:
        print("Produto não encontrado.")
        return

    if produto["quantidade"] >= quantidade:
        produto["quantidade"] -= quantidade
        movimentacao = {
            "tipo": "venda",
            "produto_codigo": produto["codigo"],
            "produto_nome": produto["nome"],
            "quantidade": quantidade,
            "descricao": "Venda para cliente"
        }
        movimentacoes.append(movimentacao)
        print(f"Venda de {quantidade} unidades do produto {produto['nome']} realizada com sucesso.")
    else:
        print("Quantidade insuficiente no estoque para atender o pedido.")

# Função para movimentar estoque (entrada e saída)
def movimentar_estoque(codigo, quantidade, tipo, descricao=""):
    produto = produtos.get(codigo)
    if not produto:
        print("Produto não encontrado.")
        return

    if tipo == "entrada":
        produto["quantidade"] += quantidade
        print(f"Entrada de {quantidade} unidades do produto {produto['nome']} realizada.")
    elif tipo == "saida" and produto["quantidade"] >= quantidade:
        produto["quantidade"] -= quantidade
        print(f"Saída de {quantidade} unidades do produto {produto['nome']} realizada.")
    else:
        print("Quantidade insuficiente no estoque.")
        return

    # Registro da movimentação
    movimentacao = {
        "tipo": tipo,
        "produto_codigo": produto["codigo"],
        "produto_nome": produto["nome"],
        "quantidade": quantidade,
        "descricao": descricao
    }
    movimentacoes.append(movimentacao)

# Função para gerar relatório de produtos em estoque
def relatorio_estoque():
    for produto in produtos.values():
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")

# Função para gerar relatório de movimentações
def relatorio_movimentacoes():
    for mov in movimentacoes:
        print(f"{mov['tipo'].capitalize()} - Produto: {mov['produto_nome']}, Quantidade: {mov['quantidade']}, Descrição: {mov['descricao']}")

# Exemplo de uso
cadastrar_produto("001", "Notebook", "Eletrônicos", 3500.00, 50, 3200.00)
cadastrar_produto("002", "Smartphone", "Eletrônicos", 2500.00, 100)

# Consultar um produto
print(consultar_produto("001"))

# Movimentação e venda de produtos
movimentar_estoque("001", 10, "entrada", "Reposição de estoque")
vender_produto("001", 3)  # Venda para cliente

# Relatórios
relatorio_estoque()
relatorio_movimentacoes()
