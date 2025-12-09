package day09;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Field {
    private final List<Tile> tiles;

    private List<Area> areas;

    public Field(List<String> lines) {
        tiles = lines.stream()
                .map(Tile::new)
                .toList();
    }

    private List<Area> getAllDistances() {
        List<Area> areas = new ArrayList<>();

        for (int i = 0; i < tiles.size() - 1; i++) {
            for (int j = i + 1; j < tiles.size(); j++) {
                Tile source = tiles.get(i);
                Tile target = tiles.get(j);

                Area area = new Area(source, target, source.calculateArea(target));
                areas.add(area);
            }
        }

        this.areas = areas;
        return areas;
    }

    public Area getBiggestAreaBetweenTiles() {
        List<Area> areas = getAllDistances();

        areas.sort(Comparator.comparing(Area::area).reversed());

        return areas.getFirst();
    }

    private boolean isPointInPolygon(long px, long py) {
        boolean inside = false;
        int n = tiles.size();

        for (int i = 0, j = n - 1; i < n; j = i++) {
            double yi = tiles.get(i).getY();
            double xi = tiles.get(i).getX();
            double yj = tiles.get(j).getY();
            double xj = tiles.get(j).getX();

            if ((yi > py) != (yj > py) &&
                    (px < (xj - xi) * (py - yi) / (yj - yi) + xi)) {
                inside = !inside;
            }
        }

        return inside;
    }

    private boolean areaLiesInsideChain(Area area) {
        long minX = Math.min(area.source().getX(), area.target().getX());
        long maxX = Math.max(area.source().getX(), area.target().getX());
        long minY = Math.min(area.source().getY(), area.target().getY());
        long maxY = Math.max(area.source().getY(), area.target().getY());

        // First check: at least one corner must be inside
        if (!isPointInPolygon(minX, minY)) {
            return false;
        }

        // Second check: no polygon edge can pass through the rectangle's interior
        int n = tiles.size();
        for (int i = 0, j = n - 1; i < n; j = i++) {
            long x1 = tiles.get(j).getX();
            long y1 = tiles.get(j).getY();
            long x2 = tiles.get(i).getX();
            long y2 = tiles.get(i).getY();

            if (edgeIntersectsRectangleInterior(x1, y1, x2, y2, minX, maxX, minY, maxY)) {
                return false;
            }
        }

        return true;
    }

    private boolean edgeIntersectsRectangleInterior(long x1, long y1, long x2, long y2,
                                                    long minX, long maxX, long minY, long maxY) {
        // Horizontal edge
        if (y1 == y2) {
            long edgeMinX = Math.min(x1, x2);
            long edgeMaxX = Math.max(x1, x2);

            // Edge must be at a Y level strictly inside the rectangle
            // and the edge's X range must overlap with the rectangle's interior
            if (y1 > minY && y1 < maxY) {
                if (edgeMinX < maxX && edgeMaxX > minX) {
                    return true;
                }
            }
        }

        // Vertical edge
        if (x1 == x2) {
            long edgeMinY = Math.min(y1, y2);
            long edgeMaxY = Math.max(y1, y2);

            // Edge must be at an X level strictly inside the rectangle
            // and the edge's Y range must overlap with the rectangle's interior
            if (x1 > minX && x1 < maxX) {
                if (edgeMinY < maxY && edgeMaxY > minY) {
                    return true;
                }
            }
        }

        return false;
    }

    public Area getBiggestAreaBetweenTilesThatContainsColouredTiles() {
        for (Area area : areas) {
            if (areaLiesInsideChain(area)) {
                return area;
            }
        }

        throw new RuntimeException("Unable to find largest area");
    }
}