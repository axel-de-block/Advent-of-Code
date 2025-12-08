package day08;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(8);
//        List<String> lines = List.of("162,817,812", "57,618,57", "906,360,560", "592,479,940", "352,342,300", "466,668,158", "542,29,236", "431,825,988", "739,650,466", "52,470,668", "216,146,977", "819,987,18", "117,168,530", "805,96,715", "346,949,466", "970,615,88", "941,993,340", "862,61,35", "984,92,344", "425,690,689");

        Space space = new Space(lines);
        space.connectJunctions((lines.size() > 50 ? 1000 : 10));

        System.out.println("Part 1: " + space.getProductOfLargestCircuitsAtLimit());
        System.out.println("Part 2: " + space.getProductOfCoordinatesAtFinalMerge());
    }
}
