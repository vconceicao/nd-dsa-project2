import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash 
      self.hash = self.calc_hash()
      self.next = None


    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = self.data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def __repr__(self):
       
        return "block[timestamp: {}, data: {}, sha256_hash: {}, prev_hash: {}]".format(self.timestamp, self.data, self.hash, self.previous_hash)

    def __eq__(self, other):
        return self.data == other.data

class Blockchain:
    
    def __init__(self):
        self.head_block = None
        self.tail_block = None
        
    def append(self, data):
           
        if data is None or data =="":
            return
        
        if self.head_block is None:
            new_block = Block(datetime.utcnow(), data, 0)
            self.head_block = new_block
            self.tail_block = self.head_block
        else:
            new_block = Block(datetime.utcnow(), data, self.tail_block.hash)
            self.tail_block.next = new_block
            self.tail_block = self.tail_block.next
        
    def __str__(self):
        current_block = self.head_block
        out_string = ""
        while current_block:
            out_string += current_block.data + " -> "
            current_block = current_block.next
        return out_string
    
    def to_list(self):
        blocks_list = []
        current_block = self.head_block
        while current_block:
            blocks_list.append([current_block])
            current_block = current_block.next
        return blocks_list




def test_function(blockchain, data, expected_blockchain_result):


    print("Blockchain to be tested: {}".format(blockchain))
    print ("Data to be added: {}".format(data))
    blockchain.append(data)

  
    print("Expected blockhain result: {}".format(expected_blockchain_result))

    
    if blockchain.to_list() == expected_blockchain_result.to_list():
        print("Result: Pass")
    else:
        print("Result: Fail")



print("### Test case 1 adding data into a blockchain ###")
blockchain = Blockchain()
data_list = ["one", "two", "three", "four"]

for element in data_list:
    blockchain.append(element)


expected_blockchain_result = Blockchain()
expected_data_list = ["one", "two", "three", "four", "five"]
for element in expected_data_list:
    expected_blockchain_result.append(element)
    
data = "five"

test_function(blockchain, data, expected_blockchain_result)
# expected blockchain result: one -> two -> three -> four -> five ->    



print("### Test case 2 adding none into blockchain ###")
blockchain = Blockchain()


expected_blockchain_result =Blockchain()

data = None


test_function(blockchain, data, expected_blockchain_result)    
# expected blockchain result:   


print("### Test case 3 adding empty data into a blockchain ###")
blockchain = Blockchain()

expected_blockchain_result =Blockchain()

data = ""

test_function(blockchain, data, expected_blockchain_result)    
# expected blockchain result:   

