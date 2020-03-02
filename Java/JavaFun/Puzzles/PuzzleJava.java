import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;

public class PuzzleJava {

    public static void main(String[] args) {
        ArrayList<Integer> intList = new ArrayList<Integer>();
        intList = createArrayInt();
        Integer total = printSum(intList);
        intList = returnGreaterInt(intList, 10);
        System.out.println(intList);
        ArrayList<String> strList = new ArrayList<String>();
        strList = createArrayString();
        strList = shuffleNames(strList);
        System.out.println(strList);
        alphabetShuffle();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr = createArrayRandInt();
        System.out.println(arr);
        arr = sortRandIntArray(arr);
        System.out.println(arr);
        printMinMax(arr);
        String str = createRandString();
        System.out.println(str);
        ArrayList<String> randStrList = new ArrayList<String>();
        randStrList = createArrayRandStr();
        System.out.println(randStrList);
    }

    public static ArrayList<Integer> createArrayInt() {
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(3);
        list.add(5);
        list.add(1);
        list.add(2);
        list.add(7);
        list.add(9);
        list.add(8);
        list.add(13);
        list.add(25);
        list.add(32);
        return list;
    }

    public static Integer printSum(ArrayList<Integer> list) {
        Integer total =0;
        for (int i = 0; i < list.size(); i++) {
            total += list.get(i);
            System.out.println(total);
        }
        return total;
    }

    public static ArrayList<Integer> returnGreaterInt(ArrayList<Integer> list, Integer greater) {
        ArrayList newList = new ArrayList<Integer>();
        for (int i = 0; i < list.size(); i++) {
            if (greater < list.get(i)) {
                newList.add(list.get(i));
            }
        }
        return newList;
    }

    public static ArrayList<String> createArrayString() {
        ArrayList list = new ArrayList<String>();
        list.add("Nancy");
        list.add("Jinichi");
        list.add("Fujibayashi");
        list.add("Momochi");
        list.add("Ishikawa");
        return list;
    }

    public static ArrayList<String> shuffleNames(ArrayList<String> list) {
        Collections.shuffle(list);
        System.out.println(list);
        list = returnGreaterString(list);
        return list;
    }

    public static ArrayList<String> returnGreaterString(ArrayList<String> list) {
        ArrayList<String> newList = new ArrayList<String>();
        for (String val: list) {
            if (val.length() > 5) {
                newList.add(val);
            }
        }
        return newList;
    }

    public static void alphabetShuffle() {
        ArrayList<Character> alphabet = new ArrayList<Character>();
        alphabet.add('a');
        for (int i = 1; i < 26; i++) {
            char temp = alphabet.get(i-1);
            temp++;
            alphabet.add(temp);
        }
        Collections.shuffle(alphabet);
        System.out.println(alphabet.get(alphabet.size() - 1));
        System.out.println(alphabet.get(0));
        if (alphabet.get(0) == 'a' || alphabet.get(0) == 'e' || alphabet.get(0) == 'i' || alphabet.get(0) == 'o' || alphabet.get(0) == 'u') {
            System.out.println("first letter is a vowel");
        }
    }

    public static ArrayList<Integer> createArrayRandInt() {
        ArrayList<Integer> arr = new ArrayList<Integer>(); 
        Random rnd = new Random();
        for (int i = 0; i < 10; i++) {
            arr.add(rnd.nextInt(45) + 55);
        }
        return arr;
    }

    public static ArrayList<Integer> sortRandIntArray(ArrayList<Integer> arr) {
        Collections.sort(arr);
        return arr;
    }

    public static void printMinMax(ArrayList<Integer> arr) {
        arr = sortRandIntArray(arr);
        System.out.println("min: " + arr.get(0));
        System.out.println("max: " + arr.get(arr.size() - 1));
    }

    public static String createRandString() {
        String str = "";
        Random rnd = new Random();
        for (int i  = 0; i < 5; i++) {
            str += ((char) (rnd.nextInt(26) + 97));
        }
        return str;
    }

    public static ArrayList<String> createArrayRandStr() {
        ArrayList<String> list = new ArrayList<String>();
        for (int i = 0; i < 10; i++) {
            list.add((String) createRandString());
        }
        return list;
    }
}