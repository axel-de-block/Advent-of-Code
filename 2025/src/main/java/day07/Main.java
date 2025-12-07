package day07;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(7);
//        List<String> lines = List.of(".......S.......", "...............", ".......^.......", "...............", "......^.^......", "...............", ".....^.^.^.....", "...............", "....^.^...^....", "...............", "...^.^...^.^...", "...............", "..^...^.....^..", "...............", ".^.^.^.^.^...^.", "...............");

        Manifold manifold = new Manifold(lines);

        manifold.drawBeamPath();
        System.out.println("Part 1: " + manifold.getTotalSplits());

        manifold.simulateSinglePath();
        System.out.println("Part 2: " + manifold.getTotalTimelines());
    }
}
