public class FizzBuzz {
    public String fizzBuzz(int number) {
        String fizz = "Fizz";
        String buzz = "Buzz";
        String numString = String.valueOf(number);
        if ((number % 5 == 0) && (number % 3 == 0)) {
            return fizz + buzz;
        } else if (number % 5 == 0) {
            return buzz;
        } else if (number % 3 == 0) {
            return fizz;
        } else {
            return numString;
        }
    }
}