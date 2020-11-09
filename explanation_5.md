# Problem 5: Blockchain
### Explanation
### Design Decisions:
I created a class called **Blockchain** to model the problem by following the implementation of a **Linked List**. The **Blockchain** class can consist of multiple **Blocks** and these are linked to the next block, in addition to saving the **hash** of the **previous block**. The main function of the class called **append** adds a new block to the **Blockchain** with the data passed by parameter. The class has helper functions to help with tests such as **__str__()**  and **to_list()**.

### ComplexityTime Complexity Time:
Because the **Blockchain** class has an attribute called **tail_block** that holds the last added block, all addition of a new block that is made by the append function is **O(1)** in the worst cases.

### Space Complexity:
The **append** function creates a new block from the data sent by a parameter that is **O(1)** in the worst cases.