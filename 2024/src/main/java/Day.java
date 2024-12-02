import java.util.ArrayList;

import static helpers.FileHelper.loadInput;

public abstract class Day {
    protected ArrayList<String> input;

    public Day(String day) {
        input = loadInput(day);
    }

    public abstract void solve();
}
