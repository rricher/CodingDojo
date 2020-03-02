
public class HumanTester {

	public static void main(String[] args) {
		Human ryan = new Human();
		Human pete = new Human();
		ryan.attackHuman(pete);
		System.out.println(pete.getHealth());
		ryan.attackHuman(pete);
		System.out.println(pete.getHealth());
		ryan.attackHuman(pete);
		System.out.println(pete.getHealth());
	}

}
