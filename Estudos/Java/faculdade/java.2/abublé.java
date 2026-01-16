class Carro {
    String marca;
    String cor;

    void ligar() {
        System.out.println("O carro esta ligado, mas nem tanto");
    }
}

public class abublé {

    public static void main(String[] args) {
        Carro meuCarro = new Carro();
        meuCarro.marca = "Fiat";
        meuCarro.cor = "Branco";
        meuCarro.ligar();
        System.out.println(meuCarro);
    }
}