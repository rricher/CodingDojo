import java.util.ArrayList;

public class Calculator {
	
	private static ArrayList<Object> equation = new ArrayList<Object>();
	private static double result;
	
	public static void preformOperation(double num) {
		equation.add(num);
	}
	
	public static void preformOperation(String oper) {
		if (oper != "=" ) {
			equation.add(oper);
		} else {
			
			@RequestParam(value="q") String searchQuery
		}
		
	}
	
	public static double getResult() {
		return result;
	}
	
}
