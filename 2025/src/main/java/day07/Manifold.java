package day07;

import lombok.Getter;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringJoiner;

public class Manifold {
    private final int width;
    private final int height;

    private final List<Type> grid = new ArrayList<>();

    // position -> number of timelines at that position
    private Map<Integer, Long> timelineCounts = new HashMap<>();

    @Getter
    private int totalSplits = 0;

    public Manifold(List<String> lines) {
        width = lines.getFirst().length();
        height = lines.size();

        loadGrid(lines);
    }

    private void loadGrid(List<String> lines) {
        for (String line : lines) {
            String[] lineArray = line.split("");

            for (String entry : lineArray) {
                if (entry.equals("S")) {
                    grid.add(Type.SOURCE);
                    continue;
                }

                grid.add(entry.equals(".") ? Type.EMPTY : Type.SPLITTER);
            }
        }
    }

    public long getTotalTimelines() {
        return timelineCounts.values().stream().mapToLong(Long::longValue).sum();
    }

    private void initPart1() {
        int startPoint = grid.indexOf(Type.SOURCE);
        grid.set(startPoint + width, Type.BEAM);
    }

    public void drawBeamPath() {
        initPart1();

        for (int currentLine = 1; currentLine < height - 1; currentLine++) {
            for (int i = currentLine * width; i < (currentLine + 1) * width; i++) {
                if (grid.get(i) == Type.BEAM) {
                    int indexBelow = i + width;

                    if (i >= width * height) {
                        continue;
                    }

                    if (grid.get(indexBelow) == Type.SPLITTER) {
                        totalSplits++;

                        grid.set(indexBelow - 1, Type.BEAM);
                        grid.set(indexBelow + 1, Type.BEAM);
                    } else {
                        grid.set(indexBelow, Type.BEAM);
                    }
                }
            }
        }
    }

    private void initPart2() {
        timelineCounts.clear();

        int startPoint = grid.indexOf(Type.SOURCE);
        int startX = startPoint % width;

        timelineCounts.put(startX, 1L);
    }

    public void simulateSinglePath() {
        initPart2();

        int currentLine = 1;

        while (currentLine < height - 1) {
            Map<Integer, Long> newTimelineCounts = new HashMap<>();

            for (var entry : timelineCounts.entrySet()) {
                int x = entry.getKey();
                long count = entry.getValue();

                List<Integer> nextLocations = generateNextBeamLocations(x, currentLine);

                for (Integer nextX : nextLocations) {
                    newTimelineCounts.merge(nextX, count, Long::sum);
                }
            }

            timelineCounts = newTimelineCounts;
            currentLine++;
        }
    }

    public List<Integer> generateNextBeamLocations(int x, int currentLine) {
        List<Integer> nextLocations = new ArrayList<>();

        int indexBelow = (currentLine + 1) * width + x;

        if (indexBelow >= width * height) {
            return nextLocations;
        }

        if (grid.get(indexBelow) == Type.SPLITTER) {
            nextLocations.add(x - 1);  // left
            nextLocations.add(x + 1);  // right
        } else {
            nextLocations.add(x);      // continue straight
        }

        return nextLocations;
    }

    // debug tool for visual representation
    private void gridToString(List<Type> grid) {
        StringJoiner linesJoiner = new StringJoiner("\n");

        for (int y = 0; y < height; y++) {
            StringJoiner positionJoiner = new StringJoiner("");

            for (int x = 0; x < width; x++) {
                int position = y * width + x;

                String repr = switch (grid.get(position)) {
                    case SOURCE -> "S";
                    case BEAM -> "|";
                    case SPLITTER -> "^";
                    case EMPTY -> ".";
                };

                positionJoiner.add(repr);
            }

            linesJoiner.add(positionJoiner.toString());
        }

        System.out.println(linesJoiner);
        try { Thread.sleep(500); } catch (InterruptedException _) {}
    }
}