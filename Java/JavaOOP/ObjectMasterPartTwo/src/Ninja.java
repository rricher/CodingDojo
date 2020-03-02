
public class Ninja extends Human{
	
	public Ninja() {
		super.setStealth(10);
	}
	
	public void steal(Human human) {
		human.setHealth(human.getHealth() - super.getStealth());
		super.setHealth(super.getHealth() + super.getStealth());
	}
	
	public void runAway() {
		super.setHealth(super.getHealth() - 10);
	}

}
