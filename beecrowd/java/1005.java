import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Double a, b, m;
        a = sc.nextDouble();
        b = sc.nextDouble();
        m = (a * 3.5 + b * 7.5)/11;
        System.out.printf("MEDIA = %.5f\n", m);
    }
}