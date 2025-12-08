package day08;

import helpers.FileHelper;

import java.util.List;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(8);
//        List<String> lines = List.of("162,817,812", "57,618,57", "906,360,560", "592,479,940", "352,342,300", "466,668,158", "542,29,236", "431,825,988", "739,650,466", "52,470,668", "216,146,977", "819,987,18", "117,168,530", "805,96,715", "346,949,466", "970,615,88", "941,993,340", "862,61,35", "984,92,344", "425,690,689");
        System.out.println(lines.size());


        Space space = new Space(lines);
        space.connectJunctions((lines.size() > 50 ? 1000 : 10));

        List<Circuit> largestCircuits = space.getLargestCircuits(3);
        List<Integer> largestCircuitsSizes = largestCircuits.stream()
                .map(Circuit::size)
                .toList();
        System.out.println(largestCircuitsSizes);

        int product = largestCircuitsSizes.stream().reduce(1, (a, b) -> a * b);
        System.out.println("Part 1: " + product);
    }
}
