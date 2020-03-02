import java.util.ArrayList;
public class ArraysDemo {
    public static void main(String[] args) {
        int[] myArray; // declare that myArray is an array of ints
        myArray = new int[5]; // initialize the array and asssign how long it is after initilization we can no longer adjust the length of this array
        myArray[0] = 4;
        myArray[1] = 8;
        myArray[2] = 8;
        myArray[3] = 5;
        myArray[4] = 9;
        // or all at once int[] myArray = {4, 8, 8, 5, 9}; here we assign the size by putting in however many ellements we want this array to have

        ArrayList<Integer> myArrayList = new ArrayList<Integer>();// an ArrayList is an object that does not have a fixed size meaning we can add and remove items from it
        // the <interger> part is called a generic and it defines what is allowed to go in the ArrayList
        myArrayList.add(10); // this is how you add items to an ArrayList
        int num = myArrayList.get(0); // and this is how you access items in an ArrayList

        ArrayList<Object> list = new ArrayList<Object>(); // if you would like to add items of different types you would have to pass it <objects> generic witch accepts all objects types
        list.add(10); // add an int with a value of 10
        list.add("Hello"); // add a string with a value of "Hello"
        list.add(new ArrayList<Integer>()); // add a new ArrayList object that accepts integers
        list.add(new Double(12.0)); // adding a Double of value 12.0
                
        System.out.println(list); // [10, "Hello", [], 12.0]
    }
}