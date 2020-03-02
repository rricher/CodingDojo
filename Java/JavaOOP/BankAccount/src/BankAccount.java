import java.util.Random;

public class BankAccount {

	private String accountNumber;
	private double checkingBalance;
	private double savingsBalance;
	private static int totalAccounts = 0;
	private static double totalMoney = 0;
	
	public BankAccount() {
		this.accountNumber = createAccountString();
		totalAccounts++;
	}
	
	public String getAccountNumber() {
		return this.accountNumber;
	}
	
	private String createAccountString() {
		Random rand = new Random();
		String accountString = "";
		for (int i = 0; i < 10; i++) {
			accountNumber += rand.nextInt();	
		}
		return accountString;
	}

	
	public double getCheckingBalance() {
		return checkingBalance;
	}
	
	public void depositChecking(double ammount) {
		this.checkingBalance += ammount;
		totalMoney += ammount;
	}
	
	public void withdrawChecking(double ammount) {
		if (this.checkingBalance - ammount > 0) {
			this.checkingBalance -= ammount;
			totalMoney -= ammount;
		}
	}
	
	public double getSavingsBalance() {
		return savingsBalance;
	}
	
	public void depositSavings(double ammount) {
		this.savingsBalance += ammount;
		totalMoney += ammount;
	}
	
	public void withdrawSavings(double ammount) {
		if (this.savingsBalance - ammount > 0) {
			this.savingsBalance -= ammount;
			totalMoney -= ammount;
		}
	}
	
	public static int getTotalAccounts() {
		return totalAccounts;
	}
		
	public static double getTotalMoney() {
		return totalMoney;
	}	

}
