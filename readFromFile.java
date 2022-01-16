import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class readFromFile{

  private static String readFromFile(){
    String res = new String();
    try{
      FileReader fr = new FileReader("bugs.txt");
      BufferedReader br = new BufferedReader(fr);
      String line = new String();
      while ((line = br.readLine()) != null) {
        // System.out.println(line);
        res = line;
      }
    }
    catch(IOException e){
      e.printStackTrace();
      res = e.toString();
    }
    return res;
  }

  public static void main(String[] args) {
    String readStatus = readFromFile();
    System.out.println(readStatus);
  }
}
