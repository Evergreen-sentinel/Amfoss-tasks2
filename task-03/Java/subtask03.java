
    import java.util.Scanner;

public class subtask03 {
    public static void printStarPattern(int n) {
        for (int i = 1; i <= n; i += 2) {
            String padding = " ".repeat((n - i) / 2);
            String stars = "*".repeat(i);
            System.out.println(padding + stars);
        }

        for (int i = n - 2; i >= 1; i -= 2) {
            String padding = " ".repeat((n - i) / 2);
            String stars = "*".repeat(i);
            System.out.println(padding + stars);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        printStarPattern(n);
        scanner.close();
    }
}
