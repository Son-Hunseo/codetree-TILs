import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("-");
        String month = sc.next();
        String day = sc.next();
        String year = sc.next();

        System.out.printf("%s.%s.%s", year, month, day);
    }
}