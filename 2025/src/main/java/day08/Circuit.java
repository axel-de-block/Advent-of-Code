package day08;

import java.util.ArrayList;
import java.util.List;

public class Circuit {
    private final List<Junction> junctions = new ArrayList<>();

    public Circuit(Junction... junctions) {
        for (Junction junction : junctions) {
            this.junctions.add(junction);
            junction.setCircuit(this);
        }
    }

    public void addJunction(Junction junction) {
        junctions.add(junction);
        junction.setCircuit(this);
    }

    public void merge(Circuit circuit) {
        for (Junction junction : circuit.junctions) {
            addJunction(junction);
        }
    }

    public int size() {
        return junctions.size();
    }

    @Override
    public String toString() {
        return junctions.toString();
    }
}
