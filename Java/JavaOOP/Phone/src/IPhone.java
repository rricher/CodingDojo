
public class IPhone extends Phone implements Ringable {

	public IPhone(String versionNumber, int batteryPercentage, String carrier, String ringTone) {
		super(versionNumber, batteryPercentage, carrier, ringTone);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String ring() {
		String ring = "iPhone " + super.getVersionNumber() + " says " + super.getRingTone();
		return ring;
	}

	@Override
	public String unlock() {
		String unlock = "Unlocking via facial recognition";
		return unlock;
	}

	@Override
	public void displayInfo() {
		String info = "iPhone " + super.getVersionNumber() + " from " + super.getCarrier();
		System.out.println(info);
	}

}
