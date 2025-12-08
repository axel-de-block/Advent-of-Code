package day08;

import lombok.Getter;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Space {
    private final List<Junction> junctions;
    private List<Circuit> circuits = new ArrayList<>();

    @Getter
    private Long productOfLargestCircuitsAtLimit;

    @Getter
    private Long productOfCoordinatesAtFinalMerge;

    public Space(List<String> input) {
        junctions = input.stream()
                .map(Junction::new)
                .toList();

        for (Junction junction : junctions) {
            circuits.add(new Circuit(junction));
        }
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

        for (PossibleConnection possibleConnection : possibleConnections) {
            if (circuits.size() == 1) {
                break;
            }

            Junction source = possibleConnection.source();
            Junction target = possibleConnection.target();

            if (source.getCircuit() == target.getCircuit()) {
                System.out.printf("Same circuit, skipping: '%s' and '%s'\n", source, target);
            } else {
                System.out.printf("Merging circuit %s with another circuit %s\n", source.getCircuit(), target.getCircuit());
                circuits.remove(target.getCircuit());
                source.getCircuit().merge(target.getCircuit());

                if (circuits.size() == 1) {
                    productOfCoordinatesAtFinalMerge = (long) source.getX() * target.getX();
                }
            }
            limit--;

            if (limit == 0) {
                List<Circuit> largest = getLargestCircuits(3);
                productOfLargestCircuitsAtLimit = largest.stream()
                        .mapToLong(Circuit::size)
                        .reduce(1L, (a, b) -> a * b);
            }
        }
    }

    private List<Circuit> getLargestCircuits(int range) {
        List<Circuit> sortedCircuits = new ArrayList<>(circuits);
        sortedCircuits.sort(Comparator.comparing(Circuit::size).reversed());

        return new ArrayList<>(sortedCircuits.subList(0, Math.min(range, sortedCircuits.size())));
    }
}
