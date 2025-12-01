package day01;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(1);
//        List<String> lines = List.of("L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82");

        Dial dial = new Dial();

        for (String line : lines) {
            dial.turn(line);
        }

        System.out.println(dial.getCounter());
        System.out.println(dial.getCounter() + dial.getOverflowCounter());
    }
}
