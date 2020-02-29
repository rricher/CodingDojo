public class StringDemo {
    public static void main(String[] args) {
        String ninja = "Coding Dojo is Awesome!";
        int length = ninja.length();
        System.out.println( "String Length is : " + length );

        String string1 = "My name is ";
        String string2 = "Michael";
        String string3 = string1.concat(string2);
        System.out.println(string3);
        // will output My name is Michael
        // This will do the same thing
        // "Welcome," + " ninja" + "!";  displays "Welcome, ninja!"

        String ninja1 = String.format("Hi %s, you owe me $%.2f !", "Jack", 25.0);
        System.out.println(ninja);
        // Will print out Hi Jack, you owe me $25.00 !
        // Where %s is expecting a string
        // And %.2f is expecting a float data type. The value 2 will just place two values to right of the decimal point.

        String ninja2 = "Welcome to Coding Dojo!";
        int a = ninja.indexOf("Coding"); // a is 11
        int b = ninja.indexOf("co"); // b is 3
        int c = ninja.indexOf("pizza"); // c is -1, "pizza" is not found

        String sentence = "   spaces everywhere!   ";
        System.out.println(sentence.trim());
        // This will output "spaces everywhere!"

        String strA = "HELLO";
        String strB = "world";
        System.out.println(strA.toLowerCase()); // hello
        System.out.println(strB.toUpperCase()); // WORLD

        String strA2 = new String("word");
        String strB2 = new String("word");
        System.out.println(strA2 == strB2); // false. not the same exact object.
        System.out.println(strA2.equals(strB2)); // true. same exact characters.
    }
}