import java.util.ArrayList;

public class Loops {
    public static void main(String[] args) {
        int i1 = 0;
        while(i1 < 7)
        {
            System.out.println("foo");
            i1++;
        }

        for (int i2 = 0; i2 < 7; i2++){
            System.out.println("bar");
        }
        // for (initialization; termination; increment){
        //     body statements
        // }

        ArrayList<String> dynamicArray = new ArrayList<String>();
        dynamicArray.add("hello");
        dynamicArray.add("world");
        dynamicArray.add("etc");
        for (int i = 0; i < dynamicArray.size(); i++){
            System.out.println(dynamicArray.get(i));
        }

        for(String name : dynamicArray){
            System.out.println("hello " + name);
            // other operations using name
        }
        // for(element container : collection){
        //     // body statements
        // }

    }
}