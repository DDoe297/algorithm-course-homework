import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Toy {
    public int weight;
    public int strength;

    public Toy(int w, int l) {
        weight = w;
        strength = l;
    }
}

class ToyStacking {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int w, l;
        ArrayList<Toy> toys = new ArrayList<Toy>();
        int numberOfToys = input.nextInt();
        while (numberOfToys != 0) {
            while (numberOfToys-- != 0) {
                w = input.nextInt();
                l = input.nextInt();
                toys.add(new Toy(w, l));
            }
            solve(toys);
            numberOfToys = input.nextInt();
            toys.clear();
        }
        input.close();
    }

    private static void solve(ArrayList<Toy> toys) {
        int length = toys.size();
        int[][] solveArray = new int[length][length];
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                solveArray[i][j] = Integer.MIN_VALUE;
            }
        }
        solveArray[0][0] = toys.get(0).strength;
        for (int i = 1; i < length; i++) {
            for (int j = 0; j <= i; j++) {
                solveArray[i][j] = Math.max(
                        (j == 0 ? toys.get(i).strength
                                : Math.min(toys.get(i).strength, solveArray[i - 1][j - 1] - toys.get(i).weight)),
                        solveArray[i - 1][j]);
            }
        }
        for (int i = length - 1; i > 0; i--) {
            if (solveArray[length - 1][i - 1] >= 0) {
                System.out.println(i);
                return;
            }
        }
        System.out.println(0);
    }
}
