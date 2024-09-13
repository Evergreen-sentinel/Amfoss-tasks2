import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class subtask04 {
    public static String createStarPattern(int n) {
        StringBuilder pattern = new StringBuilder();

        for (int i = 1; i <= n; i += 2) {
            String padding = " ".repeat((n - i) / 2);
            String stars = "*".repeat(i);
            pattern.append(padding).append(stars).append("\n");
        }

        for (int i = n - 2; i >= 1; i -= 2) {
            String padding = " ".repeat((n - i) / 2);
            String stars = "*".repeat(i);
            pattern.append(padding).append(stars).append("\n");
        }

        return pattern.toString();
    }

    public static void main(String[] args) throws IOException {
        String content = new String(Files.readAllBytes(Paths.get("/home/KID6/Desktop/AmFoss S2+/task-03/Java/input2.txt")));
        int n = Integer.parseInt(content.trim());

        String pattern = createStarPattern(n);
        Files.write(Paths.get("/home/KID6/Desktop/AmFoss S2+/task-03/Java/output2.txt"), pattern.getBytes());
    }
}
