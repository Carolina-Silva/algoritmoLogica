import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String nome;
    double sal, ven, t;
    nome = sc.nextLine();
    sal = sc.nextDouble();
    ven = sc.nextDouble();
    
    t = ven * 0.15 + sal;
    System.out.printf("TOTAL = R$ %.2f\n", t);
  }
}