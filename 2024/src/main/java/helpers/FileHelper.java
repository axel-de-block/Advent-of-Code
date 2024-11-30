package helpers;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringJoiner;

public class FileHelper {
    public static List<String> loadInput(String day) throws IOException {
        ArrayList<String> input = new ArrayList<>();
        String inputPath = FileHelper.class.getResource("/inputs/day" + day + ".txt")
                .toString().replace("file:/", "");

        BufferedReader reader = new BufferedReader(new FileReader(inputPath));

        while (reader.ready()) {
            input.add(reader.readLine());
        }
        reader.close();

        return input;
    }
}
