
public class Calculator {
	
	private static double operandOne;
	private static String operation;
	private static double operandTwo;
	private static double result;
	
	public static void preformOperation() {
		if (Calculator.operation.equals("+")) {
			result = operandOne + operandTwo;			
		} else if (Calculator.operation.equals("-")) {
			result = operandOne - operandTwo;
		}
		
	}
	
	public static double getOperandOne() {
		return operandOne;
	}
	
	public static void setOperandOne(double operandOne) {
		Calculator.operandOne = operandOne;
	}
	
	public static String getOperation() {
		return operation;
	}
	
	public static void setOperation(String operation) {
		Calculator.operation = operation;
	}
	
	public static double getOperandTwo() {
		return operandTwo;
	}
	
	public static void setOperandTwo(double operandTwo) {
		Calculator.operandTwo = operandTwo;
	}
	
	public static double getResult() {
		return result;
	}

}
