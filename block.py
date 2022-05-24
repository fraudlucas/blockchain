import hashlib
from random import random


class Block:
    creator_hash = None
    previous_block = None
    block_hash = None
    block_timestamps = None
    block_data = None

    def __init__(self, creator_hash, previous_block, block_data, block_timestamps):
        self.creator_hash = creator_hash
        self.previous_block = previous_block
        self.block_timestamps = block_timestamps
        self.block_data = block_data
        self.block_hash = hashlib.sha256((self.__dict__.__str__() + random().__str__()).encode("utf-8")).hexdigest()
