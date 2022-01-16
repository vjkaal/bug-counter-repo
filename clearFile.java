import java.io.*;

public class clearFile{
  private static String clearFile(){
    String res = new String();
    try{
      FileWriter fw = new FileWriter("bugs.txt");
      fw.write("");
      fw.close();
      res = "cleared successfully";
    }
    catch(IOException e){
      e.printStackTrace();
      res = e.toString();
    }
    return res;
  }

  public static void main(String[] args) {
    System.out.println(clearFile());
  }
}
