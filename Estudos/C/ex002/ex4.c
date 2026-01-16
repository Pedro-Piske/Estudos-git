#include <stdio.h>

int main(){

    int idade, soma = 0, contpessoa = 0;
    
    while(1){
        printf("Digite sua idade, zero vai encerrar: ");
        scanf("%d", &idade);

        if (idade == 0){
        break;
    }
    if (idade < 0) {
        printf("idade inserida invalidad, tente uma idade real seu mentiroso de uma figa \n");
        continue;
    }
    soma += idade;
    contpessoa++;
    }
    if (contpessoa > 0){
        float media = (float) soma / contpessoa;
        printf("Idade média é: %.2f\n", media);
    } else {
        printf("cade as idade zé\n");
    }

    return 0;
}