# Problem 4: Active Directory
### Explanation
### Design Decisions:
The method is take advantage of the classes Stack and State, Stack was chose because we need to traverse the group childs
to find the user and the reason behind the class State is because we don't want to search user in a group that we visited before. So I did
a little modification to store the groups that we visited before.
As using the classes mentioned above I can iteratively traverse all the groups to find the user that was set as parameter


### Time Complexity:
Time Complexity
I chose to traverse the groups using DFS Pre-order, so if the user is in first group we could find him, without
visiting the other groups. 
Considering that we are traversing groups iteratively takes O(g) and inside of it 
we're checking the if the user is group users takes O(u). At the end we have O(g * u)

### Space Complexity:
The Space Complexity considering data structures used such as Stack, List and State takes O(n).