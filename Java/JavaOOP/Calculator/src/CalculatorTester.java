
public class CalculatorTester {

	public static void main(String[] args) {
		Calculator.setOperandOne(10.2);
		Calculator.setOperation("+");
		Calculator.setOperandTwo(5.5);
		Calculator.preformOperation();
		System.out.println(Calculator.getResult());
	}

}
