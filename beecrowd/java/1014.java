import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);

	    double x, y, kml;
	    
	    x = sc.nextDouble();
	    y = sc.nextDouble();
	    
	    kml = x/y;
	    
		System.out.printf("%.3f km/l\n", kml);
	}
}