import java.io.File; // Import the File class
import java.util.Scanner;
import java.io.FileWriter;

public class Pizzeria {

        public static void main(String[] args){
                try{
                        File myObj=new File("a_example");
                        Scanner myReader=new Scanner(myObj);
                        while(myReader.hasNextLine()){
                                String data=myReader.nextLine();
                                System.out.println(data);
                        }
                        myReader.close();
                        FileWriter myWriter = new FileWriter("filename.txt");
                        myWriter.write("Files in Java might be tricky, but it is fun enough!");
                        myWriter.close();
                } catch(Exception e){
                        System.out.println("An error occurred.");
                        e.printStackTrace();
                }
        }
}