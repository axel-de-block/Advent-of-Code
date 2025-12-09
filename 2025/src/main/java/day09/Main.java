package day09;

import helpers.FileHelper;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> lines = FileHelper.loadInput(9);
//        List<String> lines = List.of("7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3");

        Field field = new Field(lines);

        Area furthest = field.getBiggestAreaBetweenTiles();
        System.out.println("Part 1: " + furthest.area());

        Area furthestWithTiles = field.getBiggestAreaBetweenTilesThatContainsColouredTiles();
        System.out.println("Part 2: " + furthestWithTiles.area());
    }
}
