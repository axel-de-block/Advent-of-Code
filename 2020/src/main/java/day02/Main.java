package day02;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static helpers.FileHelper.readDailyInput;

public class Main {
    public static void main(String[] args) {
        List<String> input = readDailyInput(2);

        System.out.println("Part one: " + part_one(input));
        System.out.println("Part two: " + part_two(input));
    }

    public static int part_one(List<String> policies) {
        int validPasswords = 0;

        for (String policy : policies) {
            List<String> splitPolicy = List.of(policy.split("[\\s:-]+"));

            int minCount = Integer.parseInt(splitPolicy.get(0));
            int maxCount = Integer.parseInt(splitPolicy.get(1));
            char expectedChar = splitPolicy.get(2).charAt(0);
            String password = splitPolicy.get(3);

            int charCount = 0;
            for (int i = 0; i < password.length(); i++) {
                if (password.charAt(i) == expectedChar) {
                    charCount++;

                    if (charCount > maxCount) {
                        break;
                    }
                }
            }

            if (charCount >= minCount && charCount <= maxCount) {
                validPasswords++;
            }
        }

        return validPasswords;
    }

    public static int part_two(List<String> policies) {
        int validPasswords = 0;

        for (String policy : policies) {
            List<String> splitPolicy = List.of(policy.split("[\\s:-]+"));

            char expectedChar = splitPolicy.get(2).charAt(0);
            String password = splitPolicy.get(3);

            char firstOccurrence = password.charAt(Integer.parseInt(splitPolicy.get(0)) - 1);
            char secondOccurrence = password.charAt(Integer.parseInt(splitPolicy.get(1)) - 1);

            if (firstOccurrence != secondOccurrence && (firstOccurrence == expectedChar || secondOccurrence == expectedChar)) {
                validPasswords++;
            }
        }

        return validPasswords;
    }
}
