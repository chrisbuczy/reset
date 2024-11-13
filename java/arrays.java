public class arrays {
    
    public static void main(String[] args) {

        String[] cars = {"Camaro", "Corvette", "Tesla"};

        System.out.println(cars[0]);

        cars[0] = "Ford";
        System.out.println(cars[0]);

        String[] cars2 = new String[3];

        cars2[0] = "Camaro";
        cars2[1] = "Corvette";
        cars2[2] = "Tesla";

        System.out.println(cars2[2]);

        for(int x = 0; x < 3; x++) {
            System.out.println(cars2[x]);
        }

    }
}
