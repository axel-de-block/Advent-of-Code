import lombok.Getter;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashSet;

import static helpers.FileHelper.loadInput;

public class Day01 {
    ArrayList<String> input;

    ArrayList<Integer> leftLocationIds = new ArrayList<>();
    ArrayList<Integer> rightLocationIds = new ArrayList<>();

    @Getter
    private int totalDistance;
    @Getter
    private int similarity;

    public Day01(String day) {
        input = loadInput(day);

        for (String line : input) {
            String leftId = line.substring(0, line.indexOf("   "));
            String rightId = line.substring(line.indexOf("   ") + 3);

            leftLocationIds.add(Integer.parseInt(leftId));
            rightLocationIds.add(Integer.parseInt(rightId));
        }
    }

    /**
     * Part 1: Not very difficult, sort both lists and just compare same index
     */
    public int calculateTotalDistance() {
        totalDistance = 0;
        leftLocationIds.sort(Integer::compareTo);
        rightLocationIds.sort(Integer::compareTo);

        for (int i = 0; i < leftLocationIds.size(); i++) {
            totalDistance += Math.abs(leftLocationIds.get(i) - rightLocationIds.get(i));
        }

        return totalDistance;
    }

    public HashMap<Integer, Integer> createMultiplierList() {
        HashMap<Integer, Integer> output = new HashMap<>();

        for (int num: leftLocationIds) {
            output.put(num, output.getOrDefault(num, 0) + 1);
        }

        return output;
    }

    /**
     * Part 2: We rely on the sorted lists from part 1.
     * We count the occurrences of each number in the left list and add it to a hashmap (easier to get the info out later)
     * Then convert the left list into a sorted set so we can iterate over it
     * We use a single downwards moving pointer as to not have to start from index = 0 for every iteration as the loop is sorted
     * Then count all occurrences of the set number in the list
     */
    public int calculateSimilarity() {
        int pointer = 0;

        similarity = 0;
        HashMap<Integer, Integer> multiplierList = createMultiplierList();

        for (int comparator : new LinkedHashSet<>(leftLocationIds)) {
            int occurrence = 0;

            while (rightLocationIds.get(pointer) <= comparator && pointer <= rightLocationIds.size() - 2) {
                if (rightLocationIds.get(pointer) == comparator) {
                    occurrence++;
                }
                pointer++;
            }

            similarity += occurrence * comparator * multiplierList.get(comparator);
        }

        return similarity;
    }

    public static void main(String[] args) {
        Instant start = Instant.now();

        Day01 day01 = new Day01("1");

        System.out.println("Part 1: " + day01.calculateTotalDistance());
        System.out.println("Part 2: " + day01.calculateSimilarity());

        Instant end = Instant.now();

        System.out.println("Execution time: " + Duration.between(start, end));
    }
}
