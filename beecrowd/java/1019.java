import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
        
        int n, h, m;
        
        n = sc.nextInt();
        
        h = n / 3600;
        n = n % 3600;
        m = n / 60;
        n = n % 60;
	   
		System.out.printf("%d:%d:%d\n", h,m,n);
	}
}