import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c, ab, m;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        
        ab = (a + b + Math.abs(a-b)) / 2;
        m = (ab + c + Math.abs(ab - c)) / 2;
        
        System.out.printf("%d eh o maior\n", m);
    }
}