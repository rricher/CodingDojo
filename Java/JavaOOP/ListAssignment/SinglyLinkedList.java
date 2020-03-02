public class SinglyLinkedList {
    public Node head;
    public SinglyLinkedList() {
        this.head = null;
    }
    // SLL methods go here. As a starter, we will show you how to add a node to the list.
    public void add(int value) {
        Node newNode = new Node(value);
        if(this.head == null) {
            this.head = newNode;
        } else {
            Node runner = this.head;
            while(runner.next != null) {
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }

    public void remove() {
        if(this.head != null) {
            Node runner = this.head;
            if (runner.next != null){
                Node runnerBehind = runner;
                runner = runner.next;
                while(runner.next != null) {
                    runnerBehind = runner;
                    runner = runner.next;
                }
                runnerBehind.next = null;
            } else {
                this.head = null;
            }
        }
    }

    public void printValues() {
        Node runner = this.head;
        while (runner != null) {
            System.out.println(runner.value);
            runner = runner.next;
        }
    }
}