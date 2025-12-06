package day03;


import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class Bank {
    private final List<Integer> batteries;

    private int largestLeft;
    private int leftIndex;

    private int largestRight;

    public Bank(String batteryBank) {
        batteries = new ArrayList<>(Stream.of(batteryBank.split(""))
                .map(Integer::parseInt)
                .toList());
        largestLeft = batteries.getFirst();
        largestRight = batteries.getLast();
    }

    public void findLeft() {
        if (largestLeft == 9) {
            return;
        }

        for (int i = 1; i < batteries.size() - 1; i++) {
            int numb = batteries.get(i);

            if (numb == 9) {
                largestLeft = numb;
                leftIndex = i;

                return;
            }

            if (largestLeft < numb) {
                largestLeft = numb;
                leftIndex = i;
            }
        }
    }

    public void findRight() {
        if (largestRight == 9) {
            return;
        }

        for (int i = batteries.size() - 2; i > leftIndex; i--) {
            int numb = batteries.get(i);

            if (numb == 9) {
                largestRight = numb;

                return;
            }

            if (largestRight < numb) {
                largestRight = numb;
            }
        }
    }

    public int getPower() {
        return Integer.parseInt(largestLeft + "" + largestRight);
    }

    public void trim() {
        while (batteries.size() > 12) {
            loop :
                for (int floor = 1; floor < 10; floor++) {
                    for (int i = 0; i < batteries.size(); i++) {
                        if (floor == batteries.get(i)) {
                            batteries.remove(i);
                            break loop;
                        }
                    }
                }
        }
    }

    public Long getOverriddenPower() {
        StringBuilder output = new StringBuilder();

        for (Integer numb : batteries) {
            output.append(numb);
        }

        System.out.println(output);
        return Long.parseLong(output.toString());
    }
}
