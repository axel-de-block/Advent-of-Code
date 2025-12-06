package day05;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(5);
//        List<String> lines = List.of("3-5","10-14","16-20","12-18","","1","5","8","11","17","32");

        FreshnessRange range = new FreshnessRange(lines);

        System.out.println("Part 1: " + range.generateListOfFreshIngredients().size());
        System.out.println(range.calculateTotalFreshIngredientIds());
    }
}
