
# Problem 2: File Recursion
### Explanation
### Design Decisions:
The find_files function receives two parameters which are the initial path that we'll be starting searching for files and the suffix of the files or extension.
At the beginning of the function, there is a treatment for None values, if any parameter is a None value an empty array is returned.
The array directories is tricky because it will store the paths found in our scanning and then remove those paths
so that they can be transformed into directories and scanned if there is any other file that has the suffix sent by parameter during the scan, it will be stored into array files.


### Time Complexity:
Time Complexity
Considering that we are traversing directory list as each time its is expanding takes O(d) and inside of it 
we're traversing the contents of the directory takes O(c). At the end we have O(d * c)

### Space Complexity:
The Space Complexity considering data structures as directories and folder_contents is O(n).