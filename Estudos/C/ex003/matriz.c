#include<stdio.h>
//faz matriz 5x5 utlizando matrizes, troquei pra 5x6, trocar todos os 6 pra 5 se quiser
int main(){

    int i, j; 
    int matriz[5][6];    

    for(i=0; i<5; i++){
        for(j=0; j<6; j++){
            if(i == j){
                matriz[i][j] = 1;
            }
            else{
                matriz[i][j] = 0;
            }
        }
    }
        printf("Matriz identidade 5x6:\n");
    for(i=0; i<5; i++){
        for(j=0; j<6; j++){
            printf("%d", matriz[i][j]);
        }
        printf("\n");
    }

}

1D
2C
3A


1D
2
3
4if e else
5