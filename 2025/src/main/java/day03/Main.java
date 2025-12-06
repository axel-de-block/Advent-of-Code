package day03;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
//        List<String> lines = FileHelper.loadInput(3);
        List<String> lines = List.of("987654321111111", "811111111111119", "234234234234278", "818181911112111");

        int counter = 0;
        Long overPoweredCounter = 0L;
        Long bruteforceCounter = 0L;

        int iter = 0;

        for (String line : lines) {
            System.out.println(iter);
            Bank bank = new Bank(line);

            bank.findLeft();
            bank.findRight();

            counter += bank.getPower();

            bank.trim();

            overPoweredCounter += bank.getOverriddenPower();
        }

        System.out.println("Part 1: " + counter);
        System.out.println("Part 2: " + overPoweredCounter);
    }
}
