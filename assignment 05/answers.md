# CMPS 2200 Assignment 5
## Answers

**Name:** Jonathan Licht


Place all written answers from `assignment-05.md` here for easier grading.



- **1d.**


                  | alice29.txt |  asyoulik.txt | f1.txt | fields.c | grammar.lsp
                  |             |               |        |          |
Fixed length cost |   1039367   |     876253    |  1340  |   78050  |  26047
                  |             |               |        |          |
Huffman cost      |   676374    |     606448    |  826   |   56206  |  17356
                  |             |               |        |          |
Huffman to fixed  |    0.65     |     0.69      |  0.62  |   0.72   |  0.67
length cost ratio |             |               |        |          |


The Huffman cost is about 2/3 of the size of the fixed length cost.


- **1e.**

It would be the sum of the length of the encodings times the frequency of those encodings.

- **2a.**

For each recursive step, greedily choose the largest coin possible which is <= the total. Subtract the coin from the total and then perform the same operation until the total reaches 0.

- **2b.**

If you have a multiple of a coin, you can replace it with the next biggest denomination becuase all coins are 2^k. For example if you had two 16 cent coins, you could have one 32 cent coin. Therefore you would only have 1 of each type of coin which minimizes the total amount of coins. The best choice is the largest coin <= total, and this achieves that.


- **2c.**

work and span are both lg(n) where n is the total amount.
