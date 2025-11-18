package day01;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

import static helpers.FileHelper.readDailyInput;

public class Main {
    public static void main(String[] args) throws URISyntaxException, IOException {
        List<String> input = readDailyInput(1);

        System.out.println("Sum two: " + sumTwo(input));
        System.out.println("Three sum: " + sumThree(input));
    }

    public static int sumTwo(List<String> input) {
        for (int i = 0; i < input.size() - 1; i++) {
            for (int j = i; j < input.size(); j++) {
                if (i == j) {
                    continue;
                }

                int val_one = Integer.parseInt(input.get(i));
                int val_two = Integer.parseInt(input.get(j));

                if (val_one + val_two == 2020) {
                    return val_one * val_two;
                }
            }
        }

        throw new RuntimeException("No two sum value");
    }

    public static int sumThree(List<String> input) {
        for (int i = 0; i < input.size() - 2; i++) {
            for (int j = i + 1; j < input.size() - 1; j++) {
                for (int n = j + 1; n < input.size(); n++) {
                    int val_one = Integer.parseInt(input.get(i));
                    int val_two = Integer.parseInt(input.get(j));
                    int val_three = Integer.parseInt(input.get(n));

                    if (val_one + val_two + val_three == 2020) {
                        return val_one * val_two * val_three;
                    }
                }
            }
        }

        throw new RuntimeException("No three sum value");
    }
}
