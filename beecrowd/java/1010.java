import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int c1, q1, c2, q2;
        float v1, v2, valor;
        c1 = sc.nextInt();
        q1 = sc.nextInt();
        v1 = sc.nextFloat();
        
        c2 = sc.nextInt();
        q2 = sc.nextInt();
        v2 = sc.nextFloat();
        
        valor = v1*q1 + v2*q2;
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", valor);
    }
}