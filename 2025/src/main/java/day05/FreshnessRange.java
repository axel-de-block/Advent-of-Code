package day05;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FreshnessRange {
    private final List<Long> windowStarts = new ArrayList<>();
    private final Map<Long, Long> windows = new HashMap<>();

    private final List<Long> ingredients;

    public FreshnessRange(List<String> lines) {
        Map<String, List<String>> split = splitRangesFromIngredients(lines);

        for (String range : split.get("ranges")) {
            String[] splitRange = range.split("-");

            Long start = Long.parseLong(splitRange[0]);
            Long end = Long.parseLong(splitRange[1]);


            if (!windows.containsKey(start)) {
                windowStarts.add(start);
            }
            windows.merge(start, end, Math::max);
        }

        ingredients = split.get("ingredients").stream()
                .map(Long::parseLong)
                .toList();

        Collections.sort(windowStarts);
        System.out.println(windows);
//        System.out.println(windowStarts);
        System.out.println();
    }

    private Map<String, List<String>> splitRangesFromIngredients(List<String> lines) {
        int indexSplit = lines.indexOf("");

        return new HashMap<>(){{
            put("ranges", lines.subList(0, indexSplit));
            put("ingredients", lines.subList(indexSplit + 1, lines.size()));
        }};
    }

    public List<Long> generateListOfFreshIngredients() {
        List<Long> freshIngredients = new ArrayList<>();

        for (Long ingredient : ingredients) {
            for (Long start : windowStarts) {
                if (ingredient >= start) {
                    if (windows.get(start) >= ingredient) {
                        freshIngredients.add(ingredient);

//                        System.out.println("Ingredient: " + ingredient);
//                        System.out.printf("Window: %d-%d\n\n", start, windows.get(start));
                        break;
                    }
                }
            }
        }

        return freshIngredients;
    }

    public Long calculateTotalFreshIngredientIds() {
        long counter = 0L;

        Map<Long, Long> mergedWindows = new HashMap<>();

        int position = 0;
        while (position < windowStarts.size()) {
            Long start = windowStarts.get(position);
            Long end = windows.get(start);

            // keep looking forward
            while (position + 1 < windowStarts.size()) {
                if (windowStarts.get(position + 1) <= end) {
//                    System.out.printf("Overlap detected with the following ranges: %d-%d and %d-%d\n", start, end, windowStarts.get(position + 1), windows.get(windowStarts.get(position + 1)));
                    end = Math.max(end, windows.get(windowStarts.get(position + 1)));

                    position++;
                    continue;
                }
                break;
            }

            counter += end - start + 1;
            mergedWindows.put(start, end);

            position++;
        }

        System.out.println(mergedWindows);

        return counter;
    }
}
