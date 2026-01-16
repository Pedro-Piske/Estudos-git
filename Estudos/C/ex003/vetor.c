#include <stdio.h>

int main(){
    int num, ordem[8];
//definir 8 numero
    for(num = 0; num < 8; num++){
        printf("Digite para definir um numero nessa posição %d: ",num);
        scanf("%d", &ordem[num]);
    }
//imprime ao contrario
    for(num = 7; num >= 0; num--){
        printf("%d", ordem[num]);

    }
    printf("\n\n\n");
    return 0;
}