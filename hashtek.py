import datetime
import json
#da block

class Block:
    nonce = 0
    block_num = 0
    prev_hash = 0x0
    next_block = None
    data = None
    hash = None
    time_stamp = datatime.datetime. now()
    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha384()
        h.update(
            str(self.nonce).encode('utf-8')
            str(self.block_num).encode('utf-8')
            str(self.prev_hash).encode('utf-8')
            str(self.data).encode('utf-8')
            str(self.time_stamp).encode('utf-8')
        )
        return h.hexdigest()
    def __str__(self):
        return str(self.hash()) + "\n" + str(self.block_num)
    

#da chain

class BlockChain:

    diff = 500
    max_nonce = 2**32
    target = 2 ** (384-diff)
    block = Block("DaBaby")
    dummy = head = block

    def add(self, block):
        block.prev_hash = self.block.hash()
        block.block_num = self.block.block_num + 1

        self.block.next = block
        self.block = self.block.next

                    str(self.data).encode('utf-8')

        def mine(self, block):
            for n in range(self.max_nonce):
                if int(block.hash(), 16)  <= self.target:
                    self.add(block)
                    print(block)
                    break
                else:
                    block.nonce += 1
