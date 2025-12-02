package day02;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static long counter;
    public static long indefiniteCounter;

    public static void main(String[] args) {
        List<String> lines = List.of(FileHelper.loadInput(2).getFirst().split(","));
//        List<String> lines = List.of("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(","));

        for (String line : lines) {
            Range range = Range.build(line);

            parseRange(range);
            generateRepeatedNumbers(range);
        }

        System.out.println("Part 1: " + counter);
        System.out.println("Part 2: " + indefiniteCounter);
    }

    public static boolean isNumberRepeated(long number) {
        String numb = String.valueOf(number);

        if (numb.length() % 2 != 0) {
            return false;
        }

        int halfLength = numb.length() / 2;

        String left = numb.substring(0, halfLength);
        String right = numb.substring(halfLength);

        return left.equals(right);
    }

    public static void parseRange(Range range) {
        for (long i = range.low(); i <= range.high(); i++) {
            if (isNumberRepeated(i)) {
                counter += i;
            }
        }
    }

    public static void generateRepeatedNumbers(Range range) {
        for (long i = range.low(); i <= range.high(); i++) {

            if (i < 10) {
                continue;
            }

            String number = String.valueOf(i);

            // only need half the length, a pattern can't repeat if it's already longer than half the whole string
            for (int x = 1; x <= (int) Math.ceil(number.length() / 2.0); x++) {
                if (number.length() % x != 0) {
                    continue;
                }

                String subsection = number.substring(0, x);

                if (number.charAt(number.length() - 1) != subsection.charAt(subsection.length() - 1)) {
                    continue;
                }

                String repeatedSubsection = subsection.repeat(number.length() / x);

                if (repeatedSubsection.equals(number)) {
                    indefiniteCounter += i;
                    break;
                }
            }
        }
    }
}
