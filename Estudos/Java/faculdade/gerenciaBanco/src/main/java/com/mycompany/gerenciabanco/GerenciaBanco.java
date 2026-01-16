/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.gerenciabanco;

/**
 *
 * @author USER
 */
import java.util.Scanner;

class contaBancaria{
    String nome;
    String sobrenome;
    String cpf;
    double saldo;
    
    public contaBancaria(String nome, String sobrenome, String cpf){
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.saldo = 0.0;
    }
    public double consultarSaldo(){
    return saldo;
    }
    
    public void depositar(double valor){
        saldo += valor;
        System.out.println("Depoisto de:" + valor +" Realizado com sucesso");
    }
    
    public void sacar(Double valor){
        if (saldo >= valor){
            saldo -= valor;
            System.out.println("Valor de" + valor +" Sacado com sucesso");
    }else{
            System.out.println("Saldo insuficiente");
        }
    }    public void exibirMenu(){
            Scanner scanner = new Scanner(System.in);
            int alternativa;
            do{
                System.out.println("\nBEM VINDO AO NOSSO BANCO, ESCOLHA O QUE DESEJA FAZER");
                System.out.println("1.Consultar Saldo");
                System.out.println("2.Realizar Depósito");
                System.out.println("3.Realizar Saque");
                System.out.println("4.Encerrar");
                System.out.println("Qual alternativa deseja:");
                alternativa = scanner.nextInt();
                
                switch(alternativa){
                    case 1:
                        System.out.println("Seu saldo é:" +consultarSaldo());
                        break;
                    case 2:
                        System.out.println("Digite valor do depósito");
                        double vDeposito = scanner.nextDouble();
                        depositar(vDeposito);
                        break;
                    case 3:
                        System.out.println("Digite valor que deseja sacar:");
                        double vSacar = scanner.nextDouble();
                        sacar(vSacar);
                        break;
                    case 4:
                        System.out.println("Finalizando Menu");
                        break;
                    default:
                        System.out.println("Valor digitado invalido"); 
                }
                
                
            } while (alternativa !=4);
            scanner.close();
        }
} 
public class GerenciaBanco {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("OLÁ, SEJA BEM VINDO AO NOSSO BANCO");
        System.out.println("Digite seu nome:");
        String nome = scanner.nextLine();
        System.out.println("Digite seu sobrenome");
        String sobrenome = scanner.nextLine();
        System.out.println("Digite seu cpf");
        String cpf = scanner.nextLine();
        
         contaBancaria conta = new contaBancaria(nome,sobrenome,cpf);
         
         conta.exibirMenu();
         
         System.out.println("Muito obrigado por usar nosso serviço");
         
         scanner.close();
       
    }
}
