# Problem: 6 Union and Intersection
### Explanation
### Design Decisions:
A **Set** is a data structure that doesn’t have a  specific order and doesn’t allow duplicates, and in **Python** it has **union** and **intersection** functions already implemented. Because of that, I have decided to create a method called **to_set()** inside the **LinkedList** class to convert a **LinkedList** into a **Set**. 
However, in both union and intersection functions, the return is a Set, and because this I have to transfer the set values to a new linked list that will be the return of the two newly created functions.

### Time ComplexityTime Complexity:
The **union** and **intersection** functions of the set are **O (len(s)+len(t))** and **O(len(s) \* len(t))** respectively, but traversing the set to add values into the new LinkedList is **O(n)** . Simplifying the time complexity is **O(n)** for both functions in the **worst case.**

### Space Complexity:
Considering that a new LinkedList will be created and it is going to have the size of the returned Set, the space complexity is **O(n)**