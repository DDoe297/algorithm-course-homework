import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
class Exam {
    public static void swap(ArrayList<Integer> array, int i, int j) {
        int temp = array.get(i);
        array.set(array.get(j), i);
        array.set(temp, j);
    }
    public static void quickSort(ArrayList<Integer> array, int start, int end) {
        if (end <= start) {
            return;
        }
        int middle = (end - start) / 2 + start;
        long pivot = array.get(middle);
        int i = start, j = end;
        while (i <= j) {
            while (array.get(i) < pivot) {
                i++;
            }
            while (array.get(j) > pivot) {
                j--;
            }
            if (i <= j) {
                swap(array, i, j);
                i++;
                j--;
            }
        }
        if (start < j) {
            quickSort(array, start, j);
        }
        if (end > i) {
            quickSort(array, i, end);
        }
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n, x;
        int passed = 0;
        ArrayList<Integer> midterm_marks = new ArrayList<Integer>();
        ArrayList<Integer> final_marks = new ArrayList<Integer>();
        n = input.nextInt();
        x = input.nextInt();
        for(int i = 0; i<n; i++){
            midterm_marks.add(input.nextInt());
        }
        for(int i = 0; i<n; i++){
            final_marks.add(input.nextInt());
        }
        Collections.sort(midterm_marks);
        Collections.sort(final_marks);
        for(int i = 0,j=n-1; i<n; i++){
            if(midterm_marks.get(i)+final_marks.get(j)>=x){
                passed++;
                j--;
            }
        }
        System.out.println(passed);
        input.close();
    }
}
