import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    int n, h;
	    float vh, sal;
	    
	    n = sc.nextInt();
	    h = sc.nextInt();
	    vh = sc.nextFloat();
	   
	    sal = h * vh;
	    
		System.out.printf("NUMBER = %d\n", n);
		System.out.printf("SALARY = U$ %.2f\n",sal);
	}
}