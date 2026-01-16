#include <stdio.h>
#include <string.h>

    struct Aluno{
        char nome[50];
        int matricula;
        float notas[2];
    };
    struct Turma{
        int Nturma;
        struct Aluno alunos[30];
        int Total_Alunos;
    };

int main(){

    struct Aluno alunos[5];
    struct Turma turmas[10]; 
    int op;
    //matriculas
    strcpy(alunos[0].nome, "Rogerin da dozé");
    alunos[0].matricula = 14;
    alunos[0].notas[0] = 5.6;
    alunos[0].notas[1] = 10;

    strcpy(alunos[1].nome, "Pedrada esmaga rato");
    alunos[1].matricula = 91;
    alunos[1].notas[0] = 2.1;
    alunos[1].notas[1] = 9.8;

    strcpy(alunos[2].nome, "Macacão do molho");
    alunos[2].matricula = 2014;
    alunos[2].notas[0] = 10;
    alunos[2].notas[1] = 10;

    strcpy(alunos[3].nome, "Joaozin do 38");
    alunos[3].matricula = 2;
    alunos[3].notas[0] = 5.6;
    alunos[3].notas[0] = 10;

    strcpy(alunos[4].nome, "O Salvador");
    alunos[4].matricula = 100;
    alunos[4].notas[0] = 1;
    alunos[4].notas[1] = 1;

//turma 1
    turmas[0].Total_Alunos = 0;
    turmas[0].Nturma = 5;
//turma 2
    turmas[1].Total_Alunos = 0;
    turmas[1].Nturma = 6;

    int a, t; 
    // a de aluno, t de turma
    float media_da_Turma = 0.0;

    do{
        printf("\n 1 - cadastrar aluno na turma\n");
        printf("2 - lançar notas de aluno\n");
        printf("3 - media da turma\n");
        printf("4 -relatorio da turma\n");
        printf("5 - encerrar\n");
        printf("opção: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
        
        printf("Escolha o aluno: ");
        scanf("%d", &a);
        printf("Escolha a turma: ");
        scanf("%d", &t);

        if(turmas[t].Total_Alunos < 30){
            turmas[t].alunos[turmas[t].Total_Alunos] = alunos[a];
            turmas[t].Total_Alunos++;
        } else {
            printf("A turme encheu já zé.\n");
        } 
        break;

        case 2:

        printf("Escolha o aluno: ");
        scanf("%d", &a);
        for (int i = 0; i < 2; i ++){
            printf("Nota %d: ", i+1);
            scanf("%f", &alunos[a].notas[i]);
        }
        break;

        case 3: 
        printf("Escolha a turma: ");
        scanf("%d", &t);
        media_da_Turma = 0.0;
        for (int i = 0; i < turmas[t].Total_Alunos; i++){
            float somaNotas = 0.0;
            for (int j = 0; j < 5; j++){
                somaNotas += turmas[t].alunos[i].notas[j];
            }
            media_da_Turma += somaNotas / 2;
        }
        printf("\n Media: %f", media_da_Turma / turmas[t].Total_Alunos);

        break;

        case 4:
        printf("Escolha a turma: ");
        scanf("%d", &t);
        printf("\n Turma %d\n", turmas[t].Nturma);
        for (int i = 0; i < turmas[t].Total_Alunos; i++){
            printf("Aluno: %s\n", turmas[t].alunos[i].nome);
            printf("Matrícula: %d\n", turmas[t].alunos[i].matricula);
            printf("Notas: ");
            for(int j = 0; j < 2; j++){
                printf("%.2f", turmas[t].alunos[i].notas[j]);
            }
            printf("\n");
        } 
        break;  

        default:
        printf("programa encerrado\n\n");
        break;

        }
    }while(op !=5);


    


    return 0;
}