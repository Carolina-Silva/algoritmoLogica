import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Double a, b, c, m;
        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();
        m = (a * 2 + b * 3 + c * 5)/10;
        System.out.printf("MEDIA = %.1f\n", m);
    }
}