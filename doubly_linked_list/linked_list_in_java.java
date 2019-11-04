public class Node {
    Node next; // has a next value
    int data;
    public Node(int data) {
        this.data = data //constructor
    }
}

// There could be multiple places in codebase that link to same head,
// so how does everyone know the head has been changed???
// Rather than giving access to the head, define a LL class that wraps the head
public class LinkedList {
    Node head;

    //APPEND
    public void append(int data) { // takes in a data value
        if (head == null) { // add in case if head is null
            head = new Node(data);
            return;
        } 
        Node current = head; // pointer to current node, the head
        while (current.next != null) { // walk through LL until we get to the end
            current = current.next; // if not the end, keep moving
        }
        current.next = new Node(data); //when to end, create new Node
    }
    
    public void prepend(int data) {
        Node = newHead = new Node(data)  // create new head value
        newHead.next = head; // newHead next value links over to old head
        head = newHead; // change the head pointer
    }

    // DELETES first node with a particular value
    public void delete(int data) {
        if (head == null) return; // if head is null, return right away. Nothing else to do
        if (head.data == data) { // what if the node we want to delete is the head???
            head = head.next; // The, cut the head out of the LL
            return;
        } 
        Node current = head; // walk through LL, stop one before the element we want to delete
        while (current.next != null) { //walk through as long as not null
            if (current.next.data == data) {
                current.next = current.next.next// Update pointers to work around the element, set next pointer to my next pointer's next pointer
                return;
            }
            current = current.next; // in other case, just move onto nthe next element
        }
        
        // so that the deleted values next pointer becomes the current next pointer
    }
}