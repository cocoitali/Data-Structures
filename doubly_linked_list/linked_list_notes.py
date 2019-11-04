
# Linked List class
class LinkedList:
    self.head = head_node
    self.tail = tail_node

    # It only refers to head and tail of the list.
    # It doesn't have direct access to any nodes in the middle of the list

    # No node is able to refer to the previous node.
    # EAch node is only able to refer to the next node

Linked Lists (Linear, Dynamic)
    - Insert beginning 0(1)
    - Insert End 0(n)
    -  linked lists describe lists of things in a recursive fashion
    - each element of a linked list is stored in a node
    - easier to insert and delete from middle of LL compared to array
    - Not as cache friendly
    - Can keep adding as many elements as we want
    - Doesn't allow for easy binary search
    - Not good for search in general OR finding random values
    - GOOD for when you need to add a lot of elements to a data set,
    and you know you won't need to retrieve them later 


Arrays (Linear, Static)
    - 0(1) to access index of any element
    - arrays describe lists of things in an iterative fashion
    - store and index elements contiguously
    - Cache-friendly: cacheds typically optimized for contiguous memory accesses
    - Static amount of allocated memory, not as easy to keep adding elements because contiguous...
    - To add or delete, you have to copy all the elements into a new array
    - Allows for easy binary search