package day08;

import lombok.Getter;
import lombok.Setter;

import java.util.StringJoiner;

@Getter
public class Junction {
    private final int x;
    private final int y;
    private final int z;

    @Setter
    private Circuit circuit = null;

    public Junction(String input) {
        String[] splitInput = input.split(",");

        x = Integer.parseInt(splitInput[0]);
        y = Integer.parseInt(splitInput[1]);
        z = Integer.parseInt(splitInput[2]);
    }

    public double calculateDistance(Junction other) {
        long dx = this.x - other.x;
        long dy = this.y - other.y;
        long dz = this.z - other.z;

        return dx * dx + dy * dy + dz * dz;
    }

    @Override
    public String toString() {
        StringJoiner joiner = new StringJoiner(",");

        joiner.add(Integer.toString(x));
        joiner.add(Integer.toString(y));
        joiner.add(Integer.toString(z));

        return joiner.toString();
    }
}
