package day02;


public record Range (long low, long high) {

    public static Range build(String range) {
        String[] split = range.split("-");

        return new Range(Long.parseLong(split[0]), Long.parseLong(split[1]));
    }
}
