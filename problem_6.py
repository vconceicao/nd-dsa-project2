class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_set(self):
        if self is None:
            return None
        
        current_node = self.head
        convertedSet = set()
        while current_node:
            convertedSet.add(current_node.value)
            current_node = current_node.next
        return convertedSet

   

def union(llist_1, llist_2):

    if llist_1 is None or llist_2 is None:
        return None 

   
 
    unionSet = llist_1.to_set().union(llist_2.to_set())
    llist = LinkedList()
    for value in unionSet:
        llist.append(value)
    return llist

def intersection(llist_1, llist_2):

    if llist_1 is None or llist_2 is None:
        return None 
    
    instersection_set = llist_1.to_set().intersection(llist_2.to_set())
    llist = LinkedList()
    for value in instersection_set:
        llist.append(value)
    return llist





# Test case 
def test_function(linked_list_1, linked_list_2, expected_union_result,expected_intersection_result, test_compare):

    
    union_result = union(linked_list_1,linked_list_2)
    intersection_result = intersection(linked_list_1, linked_list_2)

   
    
    print("Linked List 1:  {}".format(linked_list_1))
    print("Linked List 2:  {}".format(linked_list_2))
    print ("Union Result: {}".format(union_result)) 
    print ("Intersection Result: {}".format(intersection_result)) 

    is_union_result_correct = test_compare(union_result,expected_union_result)
    is_intersection_result_correct = test_compare(intersection_result,expected_intersection_result)
    print("Test Case: Pass" if is_union_result_correct and is_intersection_result_correct else "Test Case: Fail")
    print()

element_1 = [3,2,4,35,6,65,6,4,3,21]
linked_list_1 = LinkedList()
element_2 = [6,32,4,9,6,1,11,21,1]
linked_list_2 = LinkedList()

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

expected_union_list = [32,65,2,35,3,4,6,1,9,11,21]
expected_union_result = LinkedList()
expected_intersection_list = [4,21,6]
expected_intersection_result = LinkedList()


for i in expected_union_list:
    expected_union_result.append(i)

for i in expected_intersection_list:
    expected_intersection_result.append(i)   
    
test_compare = lambda a,b : a.to_set() == b.to_set()
test_function(linked_list_1, linked_list_2, expected_union_result, expected_intersection_result, test_compare)
# Union Result: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
# Intersection Result: 4 -> 21 -> 6 ->


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
linked_list_2.append(5)

expected_union_result = LinkedList()
expected_intersection_result = LinkedList()
expected_union_result.append(5)
test_compare = lambda a,b : a.to_set() == b.to_set()
test_function(linked_list_1, linked_list_2, expected_union_result, expected_intersection_result, test_compare)
# Union Result: 5 ->
# Intersection Result:

none_linked_list_1 = None
none_linked_list_2 = None
expected_none_union_result = None
expected_none_intersection_result = None
test_compare = lambda a,b : a == b
test_function(none_linked_list_1, none_linked_list_2, expected_none_union_result, expected_none_intersection_result, test_compare)
# Union Result: None
# Intersection Result: None