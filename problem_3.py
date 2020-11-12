import sys


class Node:
    def __init__(self, char, frequency):
        self.value = char
        self.frequency = frequency
        self.left = None
        self.right = None
        self.huffman_code = None

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __repr__(self):
        return "value={} and frequency={}".format(self.value, self.frequency)


class FrequencyTable:
    def __init__(self):
        self.table = {}

    def has_element(self, char):
        return self.table.get(char)

    def update_element_count(self, char):
        self.table.get(char).frequency += 1

    def add_element(self, char):
        self.table[char] = Node(char, 1)

    def get(self, char):
        return self.table.get(char)

    def __iter__(self):
        return iter(sorted(self.table.values(), key=lambda item: (item.frequency)))

    def __len__(self):
        return len(self.table)

    def __repr__(self):
        object_string = ""
        for i in self.table:
            object_string += "{} \n".format(self.table.get(i))
        return object_string


class MinHeap:

    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.Heap = [0]*(self.max_size + 1)
        self.Heap[0] = Node('', -1 * sys.maxsize)
        self.FRONT = 1

    def __len__(self):
        return self.size

    def parent(self, pos):
        return pos//2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

    def get_root(self):
        return self.Heap[self.FRONT]

    def set_root(self, value):
        self.Heap[self.FRONT] = value

    def is_leaf(self, pos):
            return not(self.has_left_child(pos) or self.has_right_child(pos))

    def has_right_child(self, pos):
        return self.right_child(pos) <= self.size

    def has_left_child(self, pos):
        return self.left_child(pos) <= self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def min_heapify(self, pos):

        if not self.is_leaf(pos):
            if (self.Heap[pos] > self.Heap[self.left_child(pos)] or
                    self.Heap[pos] > self.Heap[self.right_child(pos)]):

                if self.Heap[self.left_child(pos)] < self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))

                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def minHeap(self):

        for pos in range(self.size//2, 0, -1):
            self.min_heapify(pos)

    def remove(self):

        popped = self.get_root()
        self.set_root(self.Heap[self.size])
        self.size -= 1
        self.min_heapify(self.FRONT)
        return popped

    def __repr__(self):
        object_representation = ""
        for i in self.Heap:
            object_representation += "{} \n".format(i)
        return object_representation


def create_frequency_table(message):

    frequency_table = FrequencyTable()

    for char in message:
        if frequency_table.has_element(char):
            frequency_table.update_element_count(char)
        else:
            frequency_table.add_element(char)

    return frequency_table


def create_min_heap(frequency_table):
    min_heap = MinHeap(len(frequency_table))

    for node in frequency_table:
        min_heap.insert(node)

    return min_heap


def remove_two_nodes(min_heap):

    no1 = None
    no2 = None
    if len(min_heap) >= 2:
        no1 = min_heap.remove()
        no2 = min_heap.remove()

    return no1, no2


def create_huffman_node(n1, n2):
    node_frequency_sum = n1.frequency + n2.frequency
    huffman_node = Node('', node_frequency_sum)
    huffman_node.left = n1
    huffman_node.right = n2
    return huffman_node


def build_huffman_tree(min_heap):
    while len(min_heap) > 1:
        node1, node2 = remove_two_nodes(min_heap)
        huffman_node = create_huffman_node(node1, node2)
        min_heap.insert(huffman_node)
    return min_heap


def fill_frequency_table(frequency_table, huffman_tree):
    node = huffman_tree.Heap[1]
    stack = []

    def traverse(node, byte):

        if node:
            stack.append(str(byte))
            if node.value is not None and node.value != '':
                frequency_table.get(node.value).huffman_code = "".join(stack)

            traverse(node.left, 0)
            traverse(node.right, 1)
            if len(stack) > 0:
                stack.pop()

    traverse(node, 0)

    return frequency_table


def generate_encoded_data(frequency_table, data):
    encoded_data = ""
    for char in data:

        char_byte_value = frequency_table.get(char).huffman_code
        encoded_data += char_byte_value
    return encoded_data


def huffman_encoding(data):

    if data is None:
        print("Data must not be none\n")
        return "", None

    if len(data) == 0:
        print("Data must not be empty\n")
        return "", None

    fqt = create_frequency_table(data)
    mh = create_min_heap(fqt)
    huffman_tree = build_huffman_tree(mh)
    complete_fqt = fill_frequency_table(fqt, huffman_tree)
    encoded_data = generate_encoded_data(complete_fqt, data)
    return encoded_data, huffman_tree


def huffman_decoding(data, tree):

    if data is None or tree is None:
        print("Data or Tree must not be None\n")
        return

    if len(data) == 0 or len(tree) == 0:
        print("Data or Tree must not be empty\n")
        return

    node = None
    decoded_data = []
    msg_list = list(data)

    i = 0

    while i < len(msg_list)+1:

        if node is not None:
            if node.value != '':
                decoded_data.append(node.value)
                node = None
                if i >= len(msg_list):
                   break
            

       
        if msg_list[i] == '0':
            if node is None:
                node = tree.Heap[1]
            else:
                node = node.left
        else:
            node = node.right
        i+=1
   
    return "".join(decoded_data)
    



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 001000100000001100101101110001100010110011100010101100111110100000001100111100101000110001

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: The bird is the word

    an_empty_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(an_empty_sentence)))
    # The size of the data is: 49
    print ("The content of the data is: {}\n".format(an_empty_sentence))
    # The content of the data is: 

    encoded_data, tree = huffman_encoding(an_empty_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #Data must not be empty
    #The content of the encoded data is:
    decoded_data = huffman_decoding(encoded_data, tree)
     

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #Data or Tree must not be None
    #The size of the decoded data is: 16
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: None
   
    a_none_sentence = None

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_none_sentence)))
    #The size of the data is: 16
    print ("The content of the data is: {}\n".format(a_none_sentence))
    #The content of the data is: None

    encoded_data, tree = huffman_encoding(a_none_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #Data must not be none
    #The content of the encoded data is: 
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #Data or Tree must not be None
    #The size of the decoded data is: 16
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: None

    an_weird_sentence = 'aaaaaaaa'

    print ("The size of the data is: {}\n".format(sys.getsizeof(an_weird_sentence)))
    #The size of the data is: 57
    print ("The content of the data is: {}\n".format(an_weird_sentence))
    # The content of the data is: aaaaaaaa

    encoded_data, tree = huffman_encoding(an_weird_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 00000000

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 57
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The size of the decoded data is: 57
    
