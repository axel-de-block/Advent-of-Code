package day04;

import java.util.ArrayList;
import java.util.List;
import java.util.StringJoiner;

public class Grid {
    private static final int NEIGHBOUR_LIMIT = 4;

    private final int width;
    private final int height;

    private List<Type> grid;

    public Grid(List<String> lines) {
        this.width = lines.getFirst().length();
        this.height = lines.size();

        loadGrid(lines);
    }

    // using a 1D array to represent the positions, similar to binary, instead of a 2D array, makes most operations easier
    // inspired by an 8-BIT minecraft recreation
    private void loadGrid(List<String> lines) {
        grid = new ArrayList<>();

        for (String line : lines) {
            String[] lineArray = line.split("");

            for (String entry : lineArray) {
                grid.add(entry.equals("@") ? Type.PAPER : Type.EMPTY);
            }
        }
    }

    private static final int[][] DIRECTIONS = {
            {-1, -1}, {0, -1}, {1, -1},
            {-1,  0},          {1,  0},
            {-1,  1}, {0,  1}, {1,  1}
    };

    private List<Integer> generateNeighbourPositions(int position) {
        List<Integer> neighbourPositions = new ArrayList<>();

        int x = position % width;
        int y = position / width;

        for (int[] dir : DIRECTIONS) {
            int nx = x + dir[0];
            int ny = y + dir[1];

            // Bounds check - this naturally prevents wrapping
            if (nx >= 0 && nx < width && ny >= 0 && ny < height) {
                neighbourPositions.add(ny * width + nx);
            }
        }

        return neighbourPositions;
    }

    private int countNeighboursForPosition(int position) {
        List<Integer> neighbourPositions = generateNeighbourPositions(position);
        int counter = 0;

        for (Integer neighbourPosition : neighbourPositions) {
            if (grid.get(neighbourPosition) == Type.PAPER) {
                counter++;

                if (counter >= NEIGHBOUR_LIMIT) {
                    return counter;
                }
            }
        }

        return counter;
    }

    public List<Integer> generateMovables() {
        List<Integer> moveablePositions = new ArrayList<>();

        for (int position = 0; position < grid.size(); position++) {
            if (!(grid.get(position) == Type.PAPER)) {
                continue;
            }

            if (countNeighboursForPosition(position) < NEIGHBOUR_LIMIT) {
                moveablePositions.add(position);
            }
        }

        return moveablePositions;
    }

    public void removeMovables(List<Integer> positions) {
        for (int position : positions) {
            grid.set(position, Type.CLEARED);
        }
    }

    // debug tool for visual representation
    public void printGrid() {
        StringJoiner linesJoiner = new StringJoiner("\n");

        for (int y = 0; y < height; y++) {
            StringJoiner positionJoiner = new StringJoiner("");

            for (int x = 0; x < width; x++) {
                int position = y * width + x;

                String repr = switch (grid.get(position)) {
                    case PAPER -> "@";
                    case CLEARED -> "X";
                    case EMPTY -> ".";
                };

                positionJoiner.add(repr);
            }

            linesJoiner.add(positionJoiner.toString());
        }

        System.out.println(linesJoiner);
    }
}
