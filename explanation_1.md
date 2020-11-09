
# Problem 1:  LRU Cache
### Explanation
### Design Decisions:
In problem 2, I created a **Node** class with two attributes **next** and **previous**
, in addition to the key attributes and value that will be useful in the **LRU_Cache**. 
In the LRU_Cache, I created the **head** and **tail** attribute that will store an object of the Node class, which can
so represent a Doubly Linked List. 
The **get(key**) method is responsible for verifying that a node exists in the cache by the key attribute that is stored in a python dict, if
exist the method returns the desired node and moves it to the front of the list, making it in the MRU.
The **set(key, value)** method can add a node to the cache if its key does not exist in the list. If the method exists
only updates the value attribute of the node. In the cases of insertion and updating the chosen node will be moved to the first
position of the list.
The two cache size control attributes are **capacity** and **num_of_entries**, and that will be checked
if the **num_of_entries** is greater than the capacity in the **is_cache_full** function, if the function returns **true**, or **Least Recently
Used** value should be removed.

### Time Complexity:
The get method will take O(1) time because it uses python dict to store the key attr of node to retrieve it.
The set method will take O(1) time in both cases as it does need to traverse the entire chain to add or to remove nodes
from list because it is a Doubly Linked List.
### Space Complexity:
The Space Complexity of the LRU_Cache considering its capacity and the dict created is O(n)