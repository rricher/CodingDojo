import java.util.ArrayList;
import java.util.Arrays;

public class BasicJava {

    public static void main(String[] args) {
        printAll();
        printOdds();
        printSum();
        iterate(new int[]{1, 3, 5, 7, 9, 13});
        findMax(new int[]{-3, -5, -7});
        getAvrg(new int[]{2, 10, 3});
        int[] y = oddArray();
        System.out.println(Arrays.toString(y));
        System.out.println(greaterThan(new int[]{1, 3, 5, 7}, 3));
        int[] newArr1 = sqrVals(new int[]{1, 5, 10, -2});
        System.out.println(Arrays.toString(newArr1));
        int[] newArr2 = elimNegt(new int[]{1, 5, 10, -2});
        System.out.println(Arrays.toString(newArr2));
        ArrayList<Object> list = minMaxAvrg(new int[]{1, 5, 10, -2});
        System.out.println(list);
        int[] newarr3 = shiftValues(new int[]{1, 5, 10, 7, -2});
        System.out.println(Arrays.toString(newarr3));
    }

    public static void printAll() {
        for(int i = 0; i <= 255; i++) {
            System.out.println(i);
        }
    }

    public static void printOdds() {
        for(int i = 1; i <= 255; i += 2) {
            System.out.println(i);
        }
    }

    public static void printSum() {
        int sum = 0;
        for (int i = 0; i <= 255; i++) {
            sum += i;
            System.out.println("New number: " + i + " Sum: " + sum);
        }
    }

    public static void iterate(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        } 
    }

    public static void findMax(int[] arr) {
        if (arr.length == 0) {
            System.out.println("Please pass something in");
        } else {
            int max = arr[0];
            for (int i = 0; i < arr.length; i++) {
                if (max < arr[i]) {
                    max = arr[i];
                }
            }
            System.out.println(max);
        }
    }

    public static void getAvrg(int[] arr) {
        if (arr.length == 0) {
            System.out.println("Please pass something in");
        } else {
            int total = 0;
            for (int i = 0; i < arr.length; i++) {
                total += arr[i];
            }
            System.out.println((double) total / (double) arr.length);
        }
    }

    public static int[] oddArray() {
        int[] y;
        y = new int[(int) 255/2 + 1];
        int j = 0;
        for (int i = 1; i <= 255; i += 2) {
            y[j] = i;
            j++;
        }
        return y;
    }

    public static int greaterThan(int[] arr, int y) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > y) {
                count ++;
            }
        }
        return count;
    }

    public static int[] sqrVals(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i] * arr[i];
        }
        return arr;
    }

    public static int[] elimNegt(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < 0) {
                arr[i] = 0;
            }
        }
        return arr;
    }

    public static ArrayList<Object> minMaxAvrg(int[] arr) {
        if (arr.length == 0) {
            return null;
        } else {
            int max = arr[0];
            int min = arr[0];
            int total = 0;
            for (int i = 0; i < arr.length; i++) {
                if (max < arr[i]) {
                    max = arr[i];
                }
                if (min > arr[i]) {
                    min = arr[i];
                }
                total += arr[i];
            }
            double avrg = (double) total / (double) arr.length;
            ArrayList<Object> y = new ArrayList<Object>();
            y.add(max);
            y.add(min);
            y.add(avrg);
            return y;
        }
    }

    public static int[] shiftValues(int[] arr) {
        for (int i = 0; i < arr.length -1; i++) {
            arr[i] = arr[i+1];
        }
        arr[arr.length-1] = 0;
        return arr;
    }
}