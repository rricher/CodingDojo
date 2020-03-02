public class ProjectTest {
    public static void main(String[] args) {
        Project p1 = new Project();
        Project p2 = new Project("Ryan");
        Project p3 = new Project("Ryan", "Ryan is Great");

        System.out.println(p1.elevatorPitch());
        p1.setName("Not Ryan");
        System.out.println(p1.getName());
        p1.setDescription("Not Ryan isn't that great");
        System.out.println(p1.getDescription());
        System.out.println(p1.elevatorPitch());

        System.out.println(p2.elevatorPitch());
        System.out.println(p2.getName());
        p2.setDescription("Ryan is kinda that great");
        System.out.println(p2.getDescription());
        System.out.println(p2.elevatorPitch());

        System.out.println(p3.elevatorPitch());
        System.out.println(p3.getName());
        System.out.println(p3.getDescription());
        System.out.println(p3.elevatorPitch());
    }
}