import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int y = 0;
        double x;
        x = sc.nextDouble();
        
        y = (int) x / 100;
        
        
        System.out.println("NOTAS:");
        System.out.printf("%d nota(s) de R$ 100,00\n", cem);
        System.out.printf("%d nota(s) de R$ 50,00\n", cinq);
        System.out.printf("%d nota(s) de R$ 20,00\n", vin);
        System.out.printf("%d nota(s) de R$ 10,00\n", dez);
        System.out.printf("%d nota(s) de R$ 5,00\n", cin);
        System.out.printf("%d nota(s) de R$ 2,00\n", dois);
        
        System.out.println("MOEDAS:");
        System.out.printf("%d moeda(s) de R$ 1.00\n", um);
        System.out.printf("%d moeda(s) de R$ 0.50\n", moeda_cinq);
        System.out.printf("%d moeda(s) de R$ 0.25\n", moeda_vincinco);
        System.out.printf("%d moeda(s) de R$ 0.10\n", moeda_dez);
        System.out.printf("%d moeda(s) de R$ 0.05\n", moeda_cin);
        System.out.printf("%d moeda(s) de R$ 0.01\n", x);
        
    }
}


//nao terminado