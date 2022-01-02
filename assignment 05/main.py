import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))


def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return C

# given a dictionary f mapping characters to frequencies,
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        x = p.get()
        y = p.get()
        p.put(TreeNode(x, y, (x.data[0] + y.data[0], x.data[1] + y.data[1])))

    # return root of the tree
    return p.get()

# Perform a traversal on the prefix code tree to collect all encodings.
# Recursively call get_code, appending 0 or 1 to prefix as appropriate
# depending on if the call is to the left or right child.
# When a leaf is found, update the code dict object to map from
# the value in the leaf to the encoding specified by prefix.
# Return the code object.
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    if node.left == None and node.right == None:
        code[node.data[1]] = prefix
        return code
    else:
        if node.left is not None:
            l = get_code(node.left, prefix + "0", code)

        if node.right is not None:
            r = get_code(node.right, prefix + "1", code)

        l.update(r)

        return l

# Given an alphabet and frequencies, compute the cost of a fixed length encoding.
# You'll have to consider the total number of unique elements in f to
# determine the number of bits needed to represent each character.
def fixed_length_cost(f):
    elements = 0
    for key in f.keys():
        elements += f[key]
    unique = len(f.keys())
    digits = math.ceil(math.log(unique, 2))

    return elements * digits

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    result = 0
    for i in f.keys():
        result += len(C[i]) * f[i]
    return result


def test_huffman_simple():
    """ example from class """
    f = Counter(["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "C", "D"])
    T = make_huffman_tree(f)
    C = get_code(T)
    print(C)
    assert huffman_cost(C, f) == 17

def analyze_files():
    for fname in ['alice29.txt', 'asyoulik.txt', 'f1.txt', 'fields.c', 'grammar.lsp']:
        f = get_frequencies(fname)
        print("Fixed-length cost:  %d" % fixed_length_cost(f))
        T = make_huffman_tree(f)
        C = get_code(T)
        print("Huffman cost:  %d" % huffman_cost(C, f))



analyze_files()
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

#the shortest edit distnace a substring is part of the solution for the whole string
def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))

def fast_MED(S, T, MED_cache={}):
    if (S, T) in MED_cache.keys(): #if the calculation has already been done
        return MED_cache.get((S, T))
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(fast_MED(S[1:], T[1:]))
        else:
            result = 1 + min(fast_MED(S, T[1:], MED_cache), fast_MED(S[1:], T, MED_cache), fast_MED(S[1:], T[1:], MED_cache))
            MED_cache[(S, T)] = result
            return result


#didn't finish
def fast_align_MED(S, T, MED_cache={}):
    pass
#     s_align = ""
#     t_align = ""
#     if (S, T) in MED_cache.keys():
#         return MED_cache.get((S, T))
#
#     if (s == ""):
#         s_align = len(T) * "-"
#         MED_cache[(S, T)] = (s_align, T)
#         return s_align, T
#
#     elif (T == ""):
#         t_align = len(S) * "-"
#         MED_cache[(S, T)] = (S, t_align)
#         return S, t_align
#
#     else:
#         if (S[0] == T[0]):
#             s_align = S[0] + fast_align_MED(S[1:], T[1:])[0]
#             t_align = T[0] + fast_align_MED(S[1:], T[1:])[1]
#         else:
#             add = fast_MED(S, T[1:], MED_cache)
#             delete = fast_MED(S[1:], T, MED_cache)
#             sub = fast_MED(S[1:], T[1:], MED_cache)
#             minimum = min(add, delete, sub)
#             if minimum = add:
#                 add - to s
#
#     return s_align, t_align


def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)

def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
