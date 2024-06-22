import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        float ft = 30.48f;

        Scanner sc = new Scanner(System.in);
        float n = sc.nextFloat();

        System.out.printf("%.1f", n*ft);

    }
}