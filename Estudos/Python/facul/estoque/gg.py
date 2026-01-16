from datetime import datetime
from typing import List, Dict

# Estrutura de dados para Categorias
class Categoria:
    def __init__(self, nome: str):
        self.nome = nome

# Estrutura de dados para Produtos
class Produto:
    def __init__(self, codigo: str, nome: str, categoria: Categoria, preco: float, quantidade: int = 0):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

# Estrutura de dados para Movimentações
class Movimentacao:
    def __init__(self, tipo: str, produto: Produto, quantidade: int, data: datetime = None):
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.produto = produto
        self.quantidade = quantidade
        self.data = data if data else datetime.now()

# Classe principal para Gerenciamento de Estoque
class GerenciadorEstoque:
    def __init__(self):
        self.produtos: Dict[str, Produto] = {}  # Dicionário para armazenar produtos
        self.movimentacoes: List[Movimentacao] = []  # Lista para armazenar movimentações

    # Algoritmo de Cadastro de Produto
    def cadastrar_produto(self, codigo: str, nome: str, categoria: Categoria, preco: float, quantidade: int = 0):
        if codigo in self.produtos:
            print(f"Produto com código {codigo} já existe.")
        else:
            produto = Produto(codigo, nome, categoria, preco, quantidade)
            self.produtos[codigo] = produto
            print(f"Produto {nome} cadastrado com sucesso.")

    # Algoritmo de Consulta de Produto
    def consultar_produto(self, codigo: str):
        produto = self.produtos.get(codigo)
        if produto:
            return {
                "Código": produto.codigo,
                "Nome": produto.nome,
                "Categoria": produto.categoria.nome,
                "Preço": produto.preco,
                "Quantidade em Estoque": produto.quantidade
            }
        else:
            print("Produto não encontrado.")
            return None

    # Algoritmo de Movimentação de Estoque (Entrada e Saída)
    def movimentar_estoque(self, codigo: str, quantidade: int, tipo: str):
        produto = self.produtos.get(codigo)
        if not produto:
            print("Produto não encontrado.")
            return

        if tipo == "entrada":
            produto.quantidade += quantidade
            print(f"Entrada de {quantidade} unidades do produto {produto.nome} realizada.")
        elif tipo == "saida":
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                print(f"Saída de {quantidade} unidades do produto {produto.nome} realizada.")
            else:
                print(f"Quantidade insuficiente no estoque para o produto {produto.nome}.")
                return
        else:
            print("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")
            return

        # Registro da movimentação
        movimentacao = Movimentacao(tipo, produto, quantidade)
        self.movimentacoes.append(movimentacao)

    # Relatório de Produtos em Estoque
    def relatorio_estoque(self):
        print("Relatório de Estoque:")
        for produto in self.produtos.values():
            print(f"Código: {produto.codigo}, Nome: {produto.nome}, Quantidade: {produto.quantidade}")

    # Relatório de Movimentações
    def relatorio_movimentacoes(self):
        print("Histórico de Movimentações:")
        for mov in self.movimentacoes:
            print(f"{mov.data} - {mov.tipo.capitalize()} - Produto: {mov.produto.nome}, Quantidade: {mov.quantidade}")

# Exemplo de uso
categoria_bebidas = Categoria("Bebidas")
categoria_comidas = Categoria("Comidas")

# Instanciando o gerenciador de estoque
estoque = GerenciadorEstoque()

# Cadastro de produtos
estoque.cadastrar_produto("001", "Água", categoria_bebidas, 1.50, 100)
estoque.cadastrar_produto("002", "Suco", categoria_bebidas, 2.50, 50)
estoque.cadastrar_produto("003", "Pão", categoria_comidas, 3.00, 200)

# Consulta de produto
print(estoque.consultar_produto("001"))

# Movimentação de produtos
estoque.movimentar_estoque("001", 10, "entrada")  # Entrada
estoque.movimentar_estoque("002", 5, "saida")     # Saída

# Relatórios
estoque.relatorio_estoque()
estoque.relatorio_movimentacoes()
