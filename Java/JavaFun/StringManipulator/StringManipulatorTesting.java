public class StringManipulatorTesting {
    public static void main(String[] args) {
        StringManipulator manipulator = new StringManipulator();
        String str = manipulator.trimAndConcat("    Hello     ","     World    ");
        System.out.println(str); // HelloWorld 

        char letter = 'o';
        Integer i1 = manipulator.getIndexOrNull("Coding", letter);
        Integer i2 = manipulator.getIndexOrNull("Hello World", letter);
        Integer i3 = manipulator.getIndexOrNull("Hi", letter);
        System.out.println(i1); // 1
        System.out.println(i2); // 4
        System.out.println(i3); // null

        String word1 = "Hello";
        String subString = "llo";
        String notSubString = "world";
        Integer i4 = manipulator.getIndexOrNull(word1, subString);
        Integer i5 = manipulator.getIndexOrNull(word1, notSubString);
        System.out.println(i4); // 2
        System.out.println(i5); // null

        String word2 = manipulator.concatSubstring("Hello", 1, 2, "world");
        System.out.println(word2); // eworld
    }
}