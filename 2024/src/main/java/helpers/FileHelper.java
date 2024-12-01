package helpers;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class FileHelper {
    public static ArrayList<String> loadInput(String day) {
        ArrayList<String> input = new ArrayList<>();
        String inputPath = FileHelper.class.getResource("/inputs/day" + day + ".txt")
                .toString().replace("file:/", "");

        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputPath));

            while (reader.ready()) {
                input.add(reader.readLine());
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("No such file or directory");
            return null;
        }

        return input;
    }
}
