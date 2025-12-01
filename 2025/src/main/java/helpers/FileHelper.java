package helpers;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class FileHelper {
    public static List<String> loadInput(int day) {
        try {
            return Files.readAllLines(Path.of(FileHelper.class.getResource("/inputs/day" + String.format("%02d", day) + ".txt").toURI()));
        } catch (Exception e) {
            throw new RuntimeException(e.getMessage());
        }
    }
}
