import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;

public class Day02 extends Day {
    private ArrayList<ArrayList<Integer>> dataRows = new ArrayList<>();
    int safeRows;

    public Day02() {
        super("Test");

        for (String row : input) {
            ArrayList<Integer> dataRow = new ArrayList<>();

            for (String num : row.split(" ")) {
                dataRow.add(Integer.parseInt(num));
            }

            dataRows.add(dataRow);
        }
    }

    private boolean isRowSafe(ArrayList<Integer> row) {
        for (int i = 1; i < row.size() - 2; i++) {
            int pivot = row.get(i);

            int leftOperation = pivot - row.get(i-1);
            int rightOperation = row.get(i+1) - pivot;

            if ((Math.abs(leftOperation) > 3 || leftOperation == 0) || (Math.abs(rightOperation) > 3 || rightOperation == 0)) {
                System.out.println(leftOperation + " | " + rightOperation);
                return false;
            }

            if (leftOperation/rightOperation < 0) {
                System.out.println(leftOperation + " | " + rightOperation);
                return false;
            }
        }
        return true;
    }

    private int countSafeRows() {
        safeRows = 0;

        for (ArrayList<Integer> row : dataRows) {
            System.out.println(isRowSafe(row));
            if (isRowSafe(row)) {
                safeRows++;
            }
        }

        return safeRows;
    }

    public void solve() {
        System.out.println(countSafeRows());
    }

    public static void main(String[] args) {
        Instant start = Instant.now();

        Day02 day02 = new Day02();
        day02.solve();

        Instant end = Instant.now();
        System.out.println("Execution time: " + Duration.between(start, end));
    }
}
