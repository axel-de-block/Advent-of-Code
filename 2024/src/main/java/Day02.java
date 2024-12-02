import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;

public class Day02 extends Day {
    private final ArrayList<ArrayList<Integer>> dataRows = new ArrayList<>();
    int safeRows;

    public Day02() {
        super("2");

        for (String row : input) {
            ArrayList<Integer> dataRow = new ArrayList<>();

            for (String num : row.split(" ")) {
                dataRow.add(Integer.parseInt(num));
            }

            dataRows.add(dataRow);
        }
    }

    private boolean outOfBounds(int left, int right) {
        return Math.abs(left-right) > 3 || Math.abs(left-right) < 1;
    }

    private boolean isRowSafe(ArrayList<Integer> row, Boolean dampened) {
        boolean baseDirection = row.get(0) < row.get(1);

        for (int i = 0; i <= row.size() - 2; i++) {
            int left = row.get(i);
            int right = row.get(i + 1);

            if (outOfBounds(left, right)) {
//                if (!dampened) {
//                    row.remove(i);
//                    System.out.println("Retrying with " + row);
//                    return isRowSafe(row, true);
//                }
                return false;
            }

            if (baseDirection != left < right) {
//                if (!dampened) {
//                    if (i == 1) {
//                        if (baseDirection != row.get(row.size() - 2) < row.get(row.size() - 1)) {
//                            row.remove(0);
//                        } else {
//                            row.remove(1);
//                        }
//                    } else {
//                        row.remove(i);
//                    }
//
//                    System.out.println("Retrying with " + row);
//                    return isRowSafe(row, true);
//                }
                return false;
            }
        }

        return true;
    }

    private int countSafeRows() {
        safeRows = 0;

        for (ArrayList<Integer> row : dataRows) {
            System.out.println("Verifying " + row);
            if (isRowSafe(row, false)) {
                System.out.println(row + " is considered safe");
                safeRows++;
            }
        }

        return safeRows;
    }

    public void solve() {
        System.out.println("Part 1: " + countSafeRows());
    }

    public static void main(String[] args) {
        Instant start = Instant.now();

        Day02 day02 = new Day02();
        day02.solve();

        Instant end = Instant.now();
        System.out.println("Execution time: " + Duration.between(start, end));
    }
}
