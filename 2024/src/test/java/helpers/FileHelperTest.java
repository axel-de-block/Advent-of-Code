package helpers;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static helpers.FileHelper.loadInput;
import static org.junit.jupiter.api.Assertions.*;

class FileHelperTest {
    @Test
    public void inputLoading() throws IOException {
        List<String> testArray = loadInput("Test");

        Assertions.assertEquals(5, testArray.size());
        Assertions.assertEquals(new ArrayList<>(Arrays.asList("1", "2", "3", "4", "5")), testArray);
    }
}