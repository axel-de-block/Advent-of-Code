package day06;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(6);
//        List<String> lines = List.of("123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +  ");

        Calculator calc = new Calculator(lines);

        calc.calculateTotals();
        System.out.println("Part 1: " + calc.getHorizontalNumbersTotal());
        System.out.println("Part 2: " + calc.getVerticalNumbersTotal());
    }
}
