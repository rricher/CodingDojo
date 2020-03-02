import java.util.ArrayList;

public class ListOfExceptionsTest {
    public static void main(String[] args){
        ArrayList<Object> list = new ArrayList<Object>();
        list.add("13");
        list.add("Hello World");
        list.add(48);
        list.add("Goodbye World");
        for (int i = 0; i < list.size(); i++) {
            try {
                Integer castedValue = (Integer) list.get(i);
            } catch (ClassCastException e) {
                System.out.println("Could not cast this object. exception: ");
                System.out.println(e);
                System.out.println("index: " + i);
                System.out.println("value: " + list.get(i));
            }
        }
    }
}