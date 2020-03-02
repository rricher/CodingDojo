
public class Galaxy extends Phone implements Ringable {

	public Galaxy(String versionNumber, int batteryPercentage, String carrier, String ringTone) {
		super(versionNumber, batteryPercentage, carrier, ringTone);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String ring() {
		String ring = "Galaxy " + super.getVersionNumber() + " says " + super.getRingTone();
		return ring;
	}

	@Override
	public String unlock() {
		String unlock = "Unlocking via finger print";
		return unlock;
	}

	@Override
	public void displayInfo() {
		String info = "Galaxy " + super.getVersionNumber() + " from " + super.getCarrier();
		System.out.println(info);
	}

}
