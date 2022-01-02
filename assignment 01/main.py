"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""


# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x - 1) + foo(x - 2)


def longest_run(mylist, key):
    counter = 0
    max_num = 0
    for i in mylist:
        if i != key:
            if counter > max_num:
                max_num = counter
            counter = 0
        else:
            counter += 1
    if counter > max_num:
        max_num = counter
    return max_num


class Result:
    """ done """

    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
                (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def combine_result(result1, result2):
    if result1.is_entire_range == True and result2.is_entire_range == True:
        size = result1.left_size + result2.left_size
        return Result(size, size, size, True)

    if result1.is_entire_range == True:
        left = result1.left_size + result2.left_size
    else:
        left = result1.left_size

    if result2.is_entire_range == True:
        right = result1.right_size + result2.left_size
    else:
        right = result2.right_size

    middle = result1.right_size + result2.left_size

    if middle > max(result1.longest_size, result2.longest_size):
        return Result(left, right, middle, False)
    else:
        return Result(left, right, max(result1.longest_size, result2.longest_size), False)


def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    else:
        size = len(mylist) // 2
        left = longest_run_recursive(mylist[:size], key)
        right = longest_run_recursive(mylist[size:], key)
        return combine_result(left, right)


# Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
    assert longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 9) == 2
    assert longest_run([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 3


print(longest_run_recursive([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12))
print(longest_run_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 9))
print(longest_run_recursive([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
