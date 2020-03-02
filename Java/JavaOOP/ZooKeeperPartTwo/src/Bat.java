
public class Bat extends Mammal{
	public Bat() {
		super.setEnergy(300);
	}

	public void fly() {
		System.out.println("The bat is taking off.");
		int energy = super.displayEnergy();
		energy -= 50;
		super.setEnergy(energy);
	}
	
	public void eatHumans() {
		int energy = super.displayEnergy();
		energy += 25;
		super.setEnergy(energy);
	}
	
	public void attackTown() {
		System.out.println("The town is on fire.");
		int energy = super.displayEnergy();
		energy -= 100;
		super.setEnergy(energy);
	}

}
