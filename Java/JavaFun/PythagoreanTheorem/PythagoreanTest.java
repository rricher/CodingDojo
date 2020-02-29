public class PythagoreanTest {
	public static void main(String[] args) {
		int legA, legB;
		legA = 3;
		legB = 4;
		Pythagorean pythag = new Pythagorean();
		double c = pythag.calculateHypotenuse(legA, legB);
		System.out.println(c);
	}
}