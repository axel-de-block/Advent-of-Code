package day06;

import lombok.Getter;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Calculator {
    private final Map<Integer, Character> rangeStarts = new HashMap<>();
    private final List<String> numberLines;

    @Getter
    private long horizontalNumbersTotal = 0L;
    @Getter
    private long verticalNumbersTotal = 0L;

    public Calculator(List<String> lines) {
        numberLines = lines.subList(0, lines.size() - 1);
        System.out.println(numberLines);

        String lastLine = lines.getLast();
        for (int i = 0; i < lastLine.length(); i++) {
            char character = lastLine.charAt(i);
            if (character != ' ') {
                rangeStarts.put(i, character);
            }
        }
        rangeStarts.put(calculateMaxLengthLines(lines) + 1, ' ');

        System.out.println(rangeStarts);
        System.out.println();
    }

    private int calculateMaxLengthLines(List<String> lines) {
        int length = 0;

        for (String line : lines) {
            length = Math.max(length, line.length());
        }

        return length;
    }

    public void calculateTotals() {
        List<Long> partOneTotals = new ArrayList<>();
        List<Long> partTwoTotals = new ArrayList<>();

        List<Integer> rangeIndexes = new ArrayList<>(rangeStarts.keySet().stream().toList());
        Collections.sort(rangeIndexes);

        for (int i = 0; i < rangeIndexes.size() - 1; i++) {
            int start = rangeIndexes.get(i);
            int end = rangeIndexes.get(i + 1) - 1;

            List<Long> horizontalNumbers = new ArrayList<>();
            Map<Integer, String> verticalNumbers = new HashMap<>();

            for (String line : numberLines) {
                //part 1
                String number = line.substring(start, end);
                System.out.printf("'%s'\n", number);
                if (number.isBlank()) {
                    continue;
                }

                horizontalNumbers.add(Long.parseLong(number.trim()));

                //part 2
                for (int x = 0; x < end - start; x++) {
                    verticalNumbers.merge(x, String.valueOf(line.charAt(start + x)), String::concat);
                }
            }

            partOneTotals.add(rangeStarts.get(start) == '+' ? sum(horizontalNumbers) : product(horizontalNumbers));
            System.out.println(partOneTotals.getLast());
            System.out.println();

            List<Long> verticalNumberList = verticalNumbers.values().stream().map(numb -> Long.parseLong(numb.trim())).toList();
            partTwoTotals.add(rangeStarts.get(start) == '+' ? sum(verticalNumberList) : product(verticalNumberList));
        }

        System.out.println(partOneTotals);
        horizontalNumbersTotal = sum(partOneTotals);
        verticalNumbersTotal = sum(partTwoTotals);
    }

    private Long sum(List<Long> numbs) {
        return numbs.stream().mapToLong(Long::longValue).sum();
    }

    private Long product(List<Long> numbs) {
        return numbs.stream().mapToLong(Long::longValue).reduce(1L, (a, b) -> a * b);
    }
}
