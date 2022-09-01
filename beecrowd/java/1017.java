import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);

	    float h, km, v;
	    
	    h = sc.nextInt();
	    km = sc.nextInt();
	    
	    v = (h*km)/12;
	    
		System.out.printf("%.3f\n", v);
	}
}