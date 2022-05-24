import time

import blockchain

data_list = [
    "di3a: {amauri: 8.0, anderson: 7.5, robert: 8.0}",
    "pnt2a: {adryan: 7.5, heberton: 8.0, jessica: 8.0}",
    "pnt2b: {charles: 8.0, fabio: 8.0, jaqueline: 8.5}"
]

if __name__ == '__main__':

    for data in data_list:
        block_timestamps = time.time()
        flag = False

        while not flag:
            block = blockchain.create_block(hash("grandino"), data, block_timestamps)

            flag = blockchain.consensus(block)

    print(blockchain.chain)
