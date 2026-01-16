class Produto: 
    def __init__(self, id, nome, categoria, quantidade, preco):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco

class Movimentacao:
    def __init__(self, id, produto_id, quantidade, tipo, data):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.tipo = tipo  # 'E' para entrada, 'S' para saída
        self.data = data

def consultar_produto(produtos, id):  # Corrigido nível de indentação
    for produto in produtos:
        if produto.id == id:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Categoria: {produto.categoria}, "
                  f"Quantidade: {produto.quantidade}, Preço: {produto.preco:.2f}")
            return
    print("Produto não encontrado!")

def registrar_movimentacao(movimentacoes, produtos, contador):
    id = contador + 1
    produto_id = int(input("ID do Produto: "))
    quantidade = int(input("Quantidade: "))
    tipo = input("Tipo de Movimentação (E/S): ").upper()
    data = input("Data (DD/MM/AAAA): ")
    
    for produto in produtos:
        if produto.id == produto_id:
            if tipo == 'E':
                produto.quantidade += quantidade
            elif tipo == 'S':
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                else:
                    print("Estoque insuficiente!")
                    return
            movimentacoes.append(Movimentacao(id, produto_id, quantidade, tipo, data))
            print("Movimentação registrada com sucesso!")
            return contador + 1  # Incrementa o contador após o registro
    print("Produto não encontrado!")
    return contador  # Retorna o mesmo contador se a movimentação falhar

def gerar_relatorio(produtos):
    print("Relatório de Estoque:")
    for produto in produtos:
        print(f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}, Preço: {produto.preco:.2f}")

