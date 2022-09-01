import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double r, v;
        
        r = sc.nextFloat();
       
        v = 4/3.0 * 3.14159 * Math.pow(r,3);
        
        System.out.printf("VOLUME = %.3f\n", v);
    }
}