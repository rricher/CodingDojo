
public class Samurai extends Human{
	
	private static int counter = 0;
	
	public Samurai() {
		super.setHealth(200);
		Samurai.increaseCount();
	}
	
	public void deathBlow(Human human) {
		human.setHealth(0);
		super.setHealth(super.getHealth() / 2);
	}
	
	private static void increaseCount() {
		counter ++;
	}
	
	public static int howMany() {
		return counter;
	}

}
