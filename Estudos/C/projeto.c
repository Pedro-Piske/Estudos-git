#include <stdio.h>
#include <string.h>

// Estruturas de Dados
typedef struct {
    int id;
    char nome[50];
    int categoriaId;
    int quantidade;
    double preco;
} Produto;

typedef struct {
    int id;
    char nome[50];
} Categoria;

typedef struct {
    int id;
    int produtoId;
    int quantidade;
    char tipoMovimentacao; // 'E' para entrada, 'S' para saída
    char data[11]; // formato DD/MM/AAAA
} Movimentacao;

// Função para cadastrar um produto
void cadastrarProduto(Produto produtos[], int *contadorProdutos) {
    Produto p;
    p.id = *contadorProdutos + 1;

    printf("Nome do Produto: ");
    scanf(" %49[^\n]", p.nome);
    printf("ID da Categoria: ");
    scanf("%d", &p.categoriaId);
    printf("Quantidade: ");
    scanf("%d", &p.quantidade);
    printf("Preço: ");
    scanf("%lf", &p.preco);

    produtos[*contadorProdutos] = p;
    (*contadorProdutos)++;
    printf("Produto cadastrado com sucesso!\n");
}

// Função para consultar produto por ID
void consultarProdutoPorId(Produto produtos[], int contadorProdutos, int id) {
    for (int i = 0; i < contadorProdutos; i++) {
        if (produtos[i].id == id) {
            printf("ID: %d, Nome: %s, Categoria ID: %d, Quantidade: %d, Preço: %.2f\n",
                   produtos[i].id, produtos[i].nome, produtos[i].categoriaId,
                   produtos[i].quantidade, produtos[i].preco);
            return;
        }
    }
    printf("Produto não encontrado!\n");
}

// Função para registrar movimentação
void registrarMovimentacao(Movimentacao movimentacoes[], int *contadorMovimentacoes, Produto produtos[], int contadorProdutos) {
    Movimentacao m;
    m.id = *contadorMovimentacoes + 1;

    printf("ID do Produto: ");
    scanf("%d", &m.produtoId);
    printf("Quantidade: ");
    scanf("%d", &m.quantidade);
    printf("Tipo de Movimentação (E para entrada, S para saída): ");
    scanf(" %c", &m.tipoMovimentacao);
    printf("Data (DD/MM/AAAA): ");
    scanf(" %10[^\n]", m.data);

    for (int i = 0; i < contadorProdutos; i++) {
        if (produtos[i].id == m.produtoId) {
            if (m.tipoMovimentacao == 'E') {
                produtos[i].quantidade += m.quantidade;
            } else if (m.tipoMovimentacao == 'S') {
                if (produtos[i].quantidade >= m.quantidade) {
                    produtos[i].quantidade -= m.quantidade;
                } else {
                    printf("Quantidade insuficiente no estoque!\n");
                    return;
                }
            }
            movimentacoes[*contadorMovimentacoes] = m;
            (*contadorMovimentacoes)++;
            printf("Movimentação registrada com sucesso!\n");
            return;
        }
    }
    printf("Produto não encontrado!\n");
}

// Função para gerar relatório de estoque
void gerarRelatorioEstoque(Produto produtos[], int contadorProdutos) {
    printf("Relatório de Estoque:\n");
    for (int i = 0; i < contadorProdutos; i++) {
        printf("ID: %d, Nome: %s, Quantidade: %d, Preço: %.2f\n",
               produtos[i].id, produtos[i].nome, produtos[i].quantidade, produtos[i].preco);
    }
}

// Função para consultar movimentações por produto
void consultarMovimentacoes(Movimentacao movimentacoes[], int contadorMovimentacoes, int produtoId) {
    printf("Movimentações do Produto ID %d:\n", produtoId);
    for (int i = 0; i < contadorMovimentacoes; i++) {
        if (movimentacoes[i].produtoId == produtoId) {
            printf("ID: %d, Quantidade: %d, Tipo: %c, Data: %s\n",
                   movimentacoes[i].id, movimentacoes[i].quantidade,
                   movimentacoes[i].tipoMovimentacao, movimentacoes[i].data);
        }
    }
}
