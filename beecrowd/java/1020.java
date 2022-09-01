import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, a, m, d;
        x = sc.nextInt();
        a = x / 365;
        x = x % 365;
        m = x / 30;
        x = x % 30;
        d = x / 1;
        System.out.printf("%d ano(s)\n", a);
        System.out.printf("%d mes(es)\n", m);
        System.out.printf("%d dia(s)\n", d);
    }
}