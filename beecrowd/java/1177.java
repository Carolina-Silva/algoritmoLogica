import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n[] = new int[1000];
        
        for (int i = 0; i<1000; i++){
            n[i]=i%t;
            System.out.printf("N[%d] = %d\n", i, n[i]);
        }
    }
}