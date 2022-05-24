from typing import List
from block import Block

GENESYS_BLOCK = "0"
chain: List[Block] = list()


def create_block(creator_hash, block_data, block_timestamps):
    if len(chain) == 0:
        return Block(creator_hash, GENESYS_BLOCK, block_data, block_timestamps)
    else:
        previous_block = chain[-1]
        return Block(creator_hash, previous_block.block_hash, block_data, block_timestamps)


def consensus(block):
    if block.block_hash[0:5] == "00000":
        print(f"Add {block.block_hash} which previous block is {block.previous_block} to the chain.")
        print(f"Block content:\n  {block.block_data}")
        chain.append(block)
        print(f"Chain length: {len(chain)} \n")
        return True
    else:
        return False
