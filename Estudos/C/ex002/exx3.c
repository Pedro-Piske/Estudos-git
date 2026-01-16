#include <stdio.h>
// calculador ai de expoente zé, x é base, z é expoente
int main(){
    int x, z;
    long int res = 1;

    printf("Digite x: ");
    scanf("%d", &x);

    printf("Digite z: ");
    scanf("%d", &z);

    for(int k = 0; k < z; k++){
        res = res * x; 
    }
    printf("%d elevado a %d é igual a %d\n", x, z, res);

    return 0;
}