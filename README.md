# Teaching Blockchain Concepts

This repository is a compact Python playground that I originally built three years ago to introduce students to the core ideas that underpin blockchains: blocks, chain linkage, and consensus via proof-of-work. The code is intentionally small so learners can read every line during a single lecture or lab session.

## Project structure

```
block.py        # Block data model and hashing
blockchain.py   # Global chain list plus simple consensus function
main.py         # Demo script creating and validating a handful of blocks
```

## How it works

- **Blocks** (`block.Block`): each block stores the creator hash, the previous block hash (or a genesis marker), a timestamp, and arbitrary payload data. A SHA-256 digest of those fields plus a random nonce becomes the block hash.
- **Chain** (`blockchain.chain`): an in-memory list that starts with a hard-coded genesis hash (`"0"`). New blocks always point to the previous block's hash, enforcing immutability.
- **Consensus** (`blockchain.consensus`): mimics proof-of-work by requiring the block hash to start with five zeros. Formally, $hash(block)_{0..4} = 0$. A block is appended to the chain only when it satisfies this rule; otherwise a new block is attempted.

Because `Block` mixes in a random nonce, repeated attempts eventually stumble upon a hash that passes the difficulty target, illustrating why mining consumes many tries.

## Running the demo

1. Ensure Python 3.8+ is installed. (A virtual environment is optional but recommended.)
2. From the repository root, run:

```bash
python main.py
```

You will see log lines each time a block satisfies consensus, followed by a printout of the in-memory chain. Expect multiple hashing attempts per block—the randomness makes runtime vary from seconds to minutes.

## Teaching ideas

- **Adjust difficulty**: change the `"00000"` prefix in `blockchain.consensus` to show how harder targets slow down mining.
- **Visualize links**: have students print `block.previous_block` for each block to highlight the tamper-evident chain.
- **Data integrity exercise**: modify `block.block_data` after mining to demonstrate how the hash no longer meets consensus.
- **Persistence extension**: challenge students to write the chain to disk or expose it via a small API.

## Limitations to discuss

- No networking or peer-to-peer coordination; everything runs in a single process.
- Blocks are stored only in memory, so the chain disappears when the script ends.
- The proof-of-work target is fixed and does not retarget based on time.

Use these constraints as prompts for class discussions about what real-world blockchain systems must handle beyond this minimal prototype.
