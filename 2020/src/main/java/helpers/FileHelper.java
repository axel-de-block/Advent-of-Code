package helpers;

import day01.Main;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FileHelper {
    public static List<String> readDailyInput(int day) {
        if (day < 1 || day > 25) {
            throw new RuntimeException("Cannot load input for day " + day);
        }

        try {
            return Files.readAllLines(Path.of(Main.class.getResource(String.format("/day%02d/input.txt", day)).toURI()));
        } catch (IOException | URISyntaxException | NullPointerException e) {
            throw new RuntimeException(e);
        }
    }
}
