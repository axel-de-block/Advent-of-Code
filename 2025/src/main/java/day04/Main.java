package day04;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(4);
//        List<String> lines = List.of("..@@.@@@@.", "@@@.@.@.@@", "@@@@@.@.@@", "@.@@@@..@.", "@@.@@@@.@@", ".@@@@@@@.@", ".@.@.@.@@@", "@.@@@.@@@@", ".@@@@@@@@.", "@.@.@@@.@.");

        Grid grid = new Grid(lines);

        List<Integer> movables = grid.generateMovables();
        System.out.println("Part 1: " + movables.size());
        int counter = 0;

        while (!movables.isEmpty()) {
            counter += movables.size();
            grid.removeMovables(movables);
            movables = grid.generateMovables();
        }

        System.out.println("Part 2: " + counter);
    }
}
