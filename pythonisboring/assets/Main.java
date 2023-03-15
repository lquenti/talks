import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.ArrayList;

class Main {
  public static void main(String[] args) throws IOException {
    // Read first line
    var line = Files.readAllLines(Paths.get("nummern.txt")).get(0);

    // split into array
    String[] words = line.split(",");

    // cast array to numbers
    ArrayList<Integer> numbers = new ArrayList<Integer>();
    for (int i=0; i<words.length; i++) {
      numbers.add(Integer.parseInt(words[i].trim()));
    }

    // create sum
    int sum = 0;
    for (int i=0; i<numbers.size(); i++) {
      sum += numbers.get(i);
    }

    // Return mean
    System.out.println(sum/numbers.size());
  }
}
