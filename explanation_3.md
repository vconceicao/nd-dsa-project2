# Problem 3: Active Directory###
# Explanation### 
Design Decisions:
Abstractions/Classes created:
 - Node
 - Frequency Table
 - MinHeap

 Operations - Encoding and Decoding are divided in some steps, and because of  this I have decide to create functions for each one them, in order to organize and tests the steps individually.


### Time Complexity:
Encoding - It envolves creation of the frequency table that takes O(n), huffman_tree building takes O(log n) and the functions fill frequency table and generate encoded data leads to O(n) as it gets huffman code from frequency table. At end calculating everything, the time complexity will take O(n log n)

Decoding - It traverses the huffman tree as it pops each an element from the data stack and fill the decoded message array. The solution leads to O(n)


### Space Complexity:
For both solutions the space complexity takes O(n) at worst scenario depending on the size of the message.