class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        return str(self.value)

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.num_entries = 0
        self.hash_table = {}
        self.head = None
        self.tail = None

        
    def get(self, key):
        if key is None:
            return None
        
        value = self.hash_table.get(key, -1)
        
        if value !=-1:
            
            if value.key != self.head.key and value.key != self.tail.key:
                self.move_to_top(value)
            elif value.key==self.tail.key and value.key != self.head.key:
                self.move_tail(value.previous)
                self.move_to_top(value)                

        return value

    def set(self, key, value):
        if key is None:
            return None
        if self.capacity < 1:
            return 

        if self.get(key) == -1:
            self.add_value( key, value)

            if self.is_cache_full():
                self.remove_last_used()
                            
        else:
            self.update_value(key, value)


    def move_to_top(self,node):
        self.remove(node)
        self.prepend(node)

    def move_tail(self,node):     
        self.tail = node


    def remove(self,node):
        if node.previous:
            node.previous.next =node.next

        if node.next:
            node.next.previous = node.previous
        node.next = None
        node.previous = None

    def prepend(self, node):
        node.next = self.head
        if self.head:
            self.head.previous = node
        self.head = node

    
    def update_value(self, key, value):
    
        node = self.hash_table.get(key)
        node.value = value
        
            

    def is_cache_full(self):
        return self.num_entries  > self.capacity

            
                
    def add_value(self, key, value):
        new_node = Node(key,value) 
        self.hash_table[key] = new_node
        self.prepend(new_node)
        self.num_entries+=1
        if self.tail is None:
            self.move_tail(new_node)

          
    def remove_last_used(self):
        self.hash_table.pop(self.tail.key)
        self.move_tail(self.tail.previous)
        self.remove(self.tail.next)
        self.num_entries-=1

               

    def size(self):
        return self.num_entries


def test_add_one_value_to_empty_cache():
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)

    cache_hit = our_cache.get(1)
    
    if cache_hit.value ==1 and our_cache.size() == 1 and our_cache.head.value == 1 and our_cache.tail.value==1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_add_one_value_to_empty_cache {}".format(result))
    
def test_add_one_value_to_filled_cache():
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)

    cache_hit = our_cache.get(2)


    if cache_hit.value ==2 and our_cache.size() == 2 and our_cache.head.value == 2 and our_cache.tail.value==1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_add_one_value_to_filled_cache {}".format(result))    

def test_add_one_value_to_full_cache():
    
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)





    result = ''

    if  our_cache.size() == 3 and our_cache.head.value == 4 and our_cache.tail.value==2:
        result = "Pass"
    else:
        result = "Fail"

    print("test_add_one_value_to_full_cache {}".format(result))    

    
def test_updating_tail_value_in_cache():

    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(1, 7)




    result = ''

    if  our_cache.size() == 3 and our_cache.head.key == 1 and our_cache.head.value == 7 and our_cache.tail.key == 2 :
        result = "Pass"
    else:
        result = "Fail"

    print("test_updating_tail_value_in_cache {}".format(result))    
    
def test_updating_node_value_in_cache():

    
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(3, 7)




    assert our_cache.size()==3
    assert our_cache.head.key == 3
    assert our_cache.head.value == 7
    assert our_cache.tail.key == 1
    
    result = ''

    if  our_cache.size() == 3 and our_cache.head.key == 3 and our_cache.head.value == 7 and our_cache.tail.key == 1 :
        result = "Pass"
    else:
        result = "Fail"

    print("test_updating_node_value_in_cache {}".format(result))  
      
def test_updating_node_value_in_cache_with_one_entry():

    
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(1, 2)




    assert our_cache.size()==1
    assert our_cache.head.key == 1
    assert our_cache.head.value == 2
    assert our_cache.tail.key == 1
    assert our_cache.tail.value == 2

    result = ''

    if  our_cache.size() == 1 and our_cache.head.key == 1 and our_cache.head.value == 2 and our_cache.tail.key == 1 :
        result = "Pass"
    else:
        result = "Fail"

    print("test_updating_node_value_in_cache_with_one_entry {}".format(result))  
    

def test_cache_miss():

    
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    cache_miss = our_cache.get(2)



    assert cache_miss==-1
   

    
    result = ''

    if  our_cache.size() == 1 and cache_miss == -1 :
        result = "Pass"
    else:
        result = "Fail"

    print("test_cache_miss {}".format(result))  
    
def test_cache_hit_one_entry():

    
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    cache_hit = our_cache.get(1)

    result = ''

    if cache_hit.value ==1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_cache_hit_one_entry {}".format(result))

def test_cache_hit_most_recently_used():

    
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 3)
    our_cache.set(3, 3)
    cache_hit = our_cache.get(3)

    result = ''

    if cache_hit.value ==3 and our_cache.head.value == 3 and our_cache.tail.value==1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_cache_hit_most_recently_used {}".format(result))

def test_cache_hit_getting_node_at_middle_of_chain():

    
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    cache_hit = our_cache.get(2)

    result = ''


    if cache_hit.value ==2 and our_cache.head.value == 2 and our_cache.tail.value ==1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_cache_hit_getting_node_at_middle_of_chain {}".format(result))


def test_cache_hit_getting_node_at_middle_of_chain_with_4_entries():

    
    our_cache = LRU_Cache(4)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    cache_hit = our_cache.get(2)

    result = ''


    if cache_hit.value ==2 and our_cache.head.value == 2 and our_cache.tail.value ==1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_cache_hit_getting_node_at_middle_of_chain_with_4_entries {}".format(result))

            
def test_cache_hit_getting_the_last_node_in_the_list():

    our_cache = LRU_Cache(4)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    cache_hit = our_cache.get(1)

    result = ''


    if cache_hit.value ==1 and our_cache.head.value == 1 and our_cache.tail.value ==2:
        result = "Pass"
    else:
        result = "Fail"

    print("test_cache_hit_getting_the_last_node_in_the_list {}".format(result))

def test_adding_a_none_value_into_the_cache():

    our_cache = LRU_Cache(4)

    our_cache.set(None, None)

    cache_miss = our_cache.get(1)

    result = ''


    if cache_miss==-1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_adding_a_none_value_into_the_cache {}".format(result))

def test_adding_a_value_into_the_cache_zero_capacity():

    our_cache = LRU_Cache(0)

    our_cache.set(1, 1)

    cache_miss = our_cache.get(1)

    result = ''


    if cache_miss==-1:
        result = "Pass"
    else:
        result = "Fail"

    print("test_adding_a_value_into_the_cache_zero_capacity {}".format(result))
               
    
test_add_one_value_to_empty_cache()
#cache_hit.value ==1 and our_cache.size() == 1 and our_cache.head.value == 1 and our_cache.tail.value==1:
test_add_one_value_to_filled_cache()
# cache_hit.value ==2 and our_cache.size() == 2 and our_cache.head.value == 2 and our_cache.tail.value==1:
test_add_one_value_to_full_cache()
# our_cache.size() == 3 and our_cache.head.value == 4 and our_cache.tail.value==2:
test_updating_tail_value_in_cache()
#our_cache.size() == 3 and our_cache.head.key == 1 and our_cache.head.value == 7 and our_cache.tail.key == 2 :
test_updating_node_value_in_cache()
# our_cache.size() == 3 and our_cache.head.key == 3 and our_cache.head.value == 7 and our_cache.tail.key == 1 :
test_updating_node_value_in_cache_with_one_entry()
# our_cache.size() == 1 and our_cache.head.key == 1 and our_cache.head.value == 2 and our_cache.tail.key == 1 :
test_cache_miss()
# our_cache.size() == 1 and cache_miss == -1 :
test_cache_hit_one_entry()
# cache_hit.value ==1:
test_cache_hit_getting_node_at_middle_of_chain()
# cache_hit.value ==2 and our_cache.head.value == 2 and our_cache.tail.value ==1:
test_cache_hit_getting_node_at_middle_of_chain_with_4_entries()
# cache_hit.value ==2 and our_cache.head.value == 2 and our_cache.tail.value ==1:
test_cache_hit_getting_the_last_node_in_the_list()   
# cache_hit.value ==1 and our_cache.head.value == 1 and our_cache.tail.value ==2:
test_adding_a_none_value_into_the_cache()
# cache_miss==-1:
test_adding_a_value_into_the_cache_zero_capacity()


    
    