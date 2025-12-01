package day01;

import lombok.Getter;

public class Dial {
    private int position = 50;

    @Getter
    private int counter = 0;
    @Getter
    private int overflowCounter = 0;

    public int turn(String amount) {
        int sign = amount.charAt(0) == 'L' ? -1 : 1;
        int strength = Integer.parseInt(amount.substring(1));

        int overflow = (int) Math.floor(strength / 100.00);
        if (overflow > 0) {
            System.out.printf("Critical overflow detected: %d with strength %d\n", overflow, strength);
            overflowCounter += overflow;
        }

        int original = position;
        position += sign * (strength % 100);

        // > 100 (not >=) because landing exactly on 0 is handled by the counter++ below
        // want to separate part 1 and 2 results for sanity checks later
        // original != 0 prevents false positive when starting at 0 and moving left
        if ((position > 100 || position < 0) && original != 0) {
            System.out.printf("Overflow detected at position %d with strength %s from %d\n", position, amount, Math.floorMod(position - sign * (strength % 100), 100));
            overflowCounter++;
        }

        position = Math.floorMod(position, 100);

        if (position == 0) {
            counter++;
        }

        System.out.println("New position @ " + position + " with movement " + amount);

        return position;
    }
}
