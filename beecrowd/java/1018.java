import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, cem,cinq,vin,dez,cin,dois;
        x = sc.nextInt();
        System.out.printf("%d\n", x);
        cem = x / 100;
        x = x % 100;
        cinq = x / 50;
        x = x % 50;
        vin = x / 20;
        x = x % 20;
        dez = x / 10;
        x = x % 10;
        cin = x / 5;
        x = x % 5;
        dois = x/2;
        x = x % 2;
        System.out.printf("%d nota(s) de R$ 100,00\n", cem);
        System.out.printf("%d nota(s) de R$ 50,00\n", cinq);
        System.out.printf("%d nota(s) de R$ 20,00\n", vin);
        System.out.printf("%d nota(s) de R$ 10,00\n", dez);
        System.out.printf("%d nota(s) de R$ 5,00\n", cin);
        System.out.printf("%d nota(s) de R$ 2,00\n", dois);
        System.out.printf("%d nota(s) de R$ 1,00\n", x);
    }
}