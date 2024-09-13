import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class subtask02 {
    public static void main(String[] args) throws IOException {

        String input = new String(Files.readAllBytes(Paths.get("/home/KID6/Desktop/AmFoss S2+/task-03/Java/input.txt")));
        Files.write(Paths.get("/home/KID6/Desktop/AmFoss S2+/task-03/Java/output.txt"), input.getBytes());
    }
}
