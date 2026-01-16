class carro {
    String marca;
    String cor;
    String modelo;
    void ligar(){
        System.out.println("O carro está ligado!");
    
    }
}

public class main {
    public static void main(String[] args) {
        carro meucarro = new carro();
        meucarro.marca = "Fiat";
        meucarro.cor = "Branco";
        meucarro.modelo = "Palio";
        meucarro.ligar();
    }
    
}
