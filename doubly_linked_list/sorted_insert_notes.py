// steps to insert a new node into a dll
// head node 
// tail node 
// new node 
​
// 1. set head.next = new 
// 2. set new.prev = head 
// 3. set tail.prev = new 
// 4. set new.next = tail 
​
function sortedInsert(head, data) {
    // how do we handle an empty list?
    // create a new node with the data
    // set that new node as the head  
​
    // we'll use a current reference to 
    // keep track of where we currently 
    // are in the linked list as we traverse
    // through it 
​
    // iterate through our linked list 
    // to find the spot where we'll insert
    // the data 
        // how do we know when we've found the 
        // spot to insert the new node? 
        // if data <= current.data 
            // insert data as current's new 
            // previous node
            // break out of our loop  
        
        // if current.next === null && 
        // data > current.data 
            // set current.next = new 
            // set new.prev = current 
            // set new.next = null 
​
// return the head of our modified linked list 
​
    // are we checking for duplicates? 
    // it seems like our algorithm handles
    // duplicates just fine 
}