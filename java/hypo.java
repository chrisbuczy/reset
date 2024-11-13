import java.util.Scanner;

public class hypo {
    
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your first side length: ");
        int side1 = scanner.nextInt();
        System.out.println("What is your second side length: ");
        int side2 = scanner.nextInt();

        double hypo = (side1 * side1) + (side2 * side2);
        hypo = Math.sqrt(hypo);

        System.out.println(side1);
        System.out.println(side2);
        System.out.println("your hypo len is " + hypo);

    }
}
