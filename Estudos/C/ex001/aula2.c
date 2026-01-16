#include <stdio.h>

int main()
{
    int contador;
    printf("\nDigite umm numero para contagem regressiva: \n\n");
    scanf("%d", &contador);
    
    for (contador; contador >= 1; contador--)
    {
        printf("%d", &contador);
    }
    return (0);
}

