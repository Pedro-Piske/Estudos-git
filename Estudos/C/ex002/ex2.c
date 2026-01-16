#include <stdio.h>
// laço simples pra calcular tabuada de 2
int main(){
    int res, x = 1;

    while(x <= 10){
        res = 2 * x ;
        printf("%d \n", res);
        x = x + 1;
    }


    return 0;
}