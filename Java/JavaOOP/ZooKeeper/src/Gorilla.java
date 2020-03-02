
public class Gorilla extends Mammal {
	
	public void throwSomething() {
		int energy = super.displayEnergy();
		energy -= 5;
		super.setEnergy(energy);
	}
	
	public void eatBannans() {
		int energy = super.displayEnergy();
		energy += 10;
		super.setEnergy(energy);
	}
	
	public void climb() {
		int energy = super.displayEnergy();
		energy -= 10;
		super.setEnergy(energy);
	}

}
