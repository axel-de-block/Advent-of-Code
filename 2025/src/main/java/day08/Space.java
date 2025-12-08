package day08;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Space {
    private final List<Junction> junctions;
    private List<Circuit> circuits = new ArrayList<>();

    public Space(List<String> input) {
        junctions = input.stream()
                .map(Junction::new)
                .toList();
    }

    private List<PossibleConnection> getAllPossibleConnections() {
        List<PossibleConnection> pairs = new ArrayList<>();

        for (int i = 0; i < junctions.size(); i++) {
            for (int j = i + 1; j < junctions.size(); j++) {
                Junction a = junctions.get(i);
                Junction b = junctions.get(j);
                pairs.add(new PossibleConnection(a.calculateDistance(b), a, b));
            }
        }

        pairs.sort(Comparator.comparing(PossibleConnection::distance));
        return pairs;
    }

    public void connectJunctions(int limit) {
        List<PossibleConnection> possibleConnections = getAllPossibleConnections();

        int actualConnections = 0;
        int skippedSameCircuit = 0;
        int merges = 0;

        for (PossibleConnection possibleConnection : possibleConnections) {
            if (limit <= 0) {
                break;
            }

            Junction source = possibleConnection.source();
            Junction target = possibleConnection.target();

            if (source.getCircuit() != null) {
                // if source is already in a circuit, but target isn't
                if (target.getCircuit() == null) {
//                    System.out.printf("Connecting unconnected target '%s' to existing circuit %s\n", target, source.getCircuit());
                    source.getCircuit().addJunction(target);
                    actualConnections++;
                // if they're already in the same circuit, nothing needs to happen
                } else if (source.getCircuit() == target.getCircuit()) {
//                    System.out.printf("Same circuit, skipping: '%s' and '%s'\n", source, target);
                    skippedSameCircuit++;
                // if source is already in a circuit, but so is target
                } else {
//                    System.out.printf("Merging circuit %s with another circuit %s\n", source.getCircuit(), target.getCircuit());
                    circuits.remove(target.getCircuit());
                    source.getCircuit().merge(target.getCircuit());
                    merges++;
                }
            } else {
                // if source isn't in a circuit, but target is
                if (target.getCircuit() != null) {
//                    System.out.printf("Connecting unconnected target '%s' to existing circuit %s\n", source, target.getCircuit());
                    target.getCircuit().addJunction(source);
                    actualConnections++;
                // if source isn't in a circuit, and neither is target
                } else {
//                    System.out.printf("Connecting unconnected junctions to each other '%s' -> '%s'\n", source, target);
                    circuits.add(new Circuit(source, target));
                    actualConnections++;
                }
            }

            limit--;
        }

        System.out.println("Connections processed: " + actualConnections);
        System.out.println("Same-circuit skips: " + skippedSameCircuit);
        System.out.println("Merges: " + merges);
        System.out.println("Total circuits: " + circuits.size());
        System.out.println("Total junctions in circuits: " + circuits.stream().mapToInt(Circuit::size).sum());
    }

    public List<Circuit> getLargestCircuits(int range) {
        circuits.sort(Comparator.comparing(Circuit::size).reversed());

        return circuits.subList(0, Math.min(range, circuits.size()));
    }
}
