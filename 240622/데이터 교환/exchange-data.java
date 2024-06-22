public class Main {
    public static void main(String[] args) {
        int a = 5, b = 6, c = 7;
        int temp = c;

        b = a;
        c = b;
        a = temp;

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}