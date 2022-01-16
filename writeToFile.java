import java.io.FileWriter;
import java.io.IOException;

public class file{

  private static String writeToFile(int number){
    String res = new String();
    try{
      // String text = number.toString();
      FileWriter fw = new FileWriter("bugs.txt");
      fw.write("");
      fw.append(number+"\n");
      fw.close();
      res = "writen successfully";
    }
    catch(IOException e){
      e.printStackTrace();
      res = e.toString();
    }
    return res;
  }

  public static void main(String[] args) {
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int a = Integer.parseInt(args[0]);
    String writeStatus = writeToFile(a);
    System.out.println(writeStatus);
  }
}
