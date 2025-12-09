package day09;

import lombok.Getter;

@Getter
public class Tile {
    private final long x;
    private final long y;

    public Tile(String input) {
        String[] splitInput = input.split(",");

        x = Long.parseLong(splitInput[0]);
        y = Long.parseLong(splitInput[1]);
    }

    public Long calculateArea(Tile other) {
        if (other == this) {
            return 0L;
        }

        long width = Math.abs(this.x - other.x) + 1;
        long height = Math.abs(this.y - other.y) + 1;

        return width * height;
    }

    @Override
    public String toString() {
        return String.format("[%d, %d]", x, y);
    }
}
