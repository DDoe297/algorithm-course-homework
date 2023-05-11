import java.util.Scanner;

public class PairSumToK {

    public static void swap(long array[], int i, int j) {
        long temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void quickSort(long[] array, int start, int end) {
        if (end <= start) {
            return;
        }
        int middle = (end - start) / 2 + start;
        long pivot = array[middle];
        int i = start, j = end;
        while (i <= j) {
            while (array[i] < pivot) {
                i++;
            }
            while (array[j] > pivot) {
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

    static int binarySearch(long[] array, int start, int end, long target) {
        int first = 0;
        int last = array.length - 1;
        int middle = (first + last) / 2;
        while (first <= last) {
            if (array[middle] < target) {
                first = middle + 1;
            } else if (array[middle] == target) {
                return middle;
            } else {
                last = middle - 1;
            }
            middle = (first + last) / 2;
        }
        return -1;
    }

    static boolean doesPairExist(long[] prices, long targetSum) {
        quickSort(prices, 0, prices.length - 1);
        for (long item : prices) {
            if (binarySearch(prices, 0, prices.length, targetSum - item) != -1) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n;
        long k;
        n = input.nextInt();
        k = input.nextLong();
        long[] prices = new long[n];
        for (int i = 0; i < n; i++) {
            prices[i] = input.nextLong();
        }
        if (doesPairExist(prices, k)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        input.close();
    }
}