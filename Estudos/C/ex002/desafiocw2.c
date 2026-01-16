#include <stdio.h>
// forma terrivel de usar fibonacci, ta errada, n sei corrigir
int main(){
    int num;
    int primeiro = 0, segundo = 1;
    int proximo;
    printf("Digite um digito: ");
    scanf("%d",&num);
    printf("sequencia de fibofodase até %d:\n", num);
    

    for(int num2 = 0; num2 < num; num2++){
        if(num2 <= 1){
            proximo = num2;
        } else{
            proximo = primeiro + segundo;
            primeiro = segundo;
            segundo = proximo;

        }
        printf("%d", proximo);
    }


    return 0;
}