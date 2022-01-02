"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time


class BinaryNumber:
    """ done """

    def __init__(self, n):
        self.decimal_val = n
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        return ('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def quadratic_multiply(x, y):
    #this is to handle the fact that x and y might be passed in as a
    #BinaryNumber or a list
    try:
        n = max(len(x), len(y)) #if its a list, get the length
    except:
        x = x.binary_vec #if its not a list, extract the list, then get length
        y = y.binary_vec
        n = max(len(x), len(y))

    #base case
    if n == 1:
        return int(x[0]) * int(y[0])

    #recursive case
    else:
        while len(x) > len(y): #add zeros to beginning of y to make them equal length
            y.insert(0, '0')

        while len(y) > len(x): #add zeros to beginning of x to make them equal length
            x.insert(0, '0')

        if n % 2 != 0: #make x and y an even amount of digits
            x.insert(0, '0')
            y.insert(0, '0')
            n += 1

        #split lists in half
        xl = x[:n // 2]
        xr = x[n // 2:]
        yl = y[:n // 2]
        yr = y[n // 2:]

        #do recusrion
        xl_times_yl = quadratic_multiply(xl, yl)
        xl_times_yr = quadratic_multiply(xl, yr)
        xr_times_yl = quadratic_multiply(xr, yl)
        xr_times_yr = quadratic_multiply(xr, yr)

        #combine everything together
        return ((2 ** n) * xl_times_yl + 2 ** (n // 2) * (xl_times_yr + xr_times_yl) + xr_times_yr)


#take in x and y as lists and n is length of x and y
#returns the sum as a BinaryNumber
def binary_addition(x_list, y_list, n):
    x_string = ""
    y_string = ""
    for i in range(n//2):
        x_string += x_list[i]
        y_string += y_list[i]

    x_int = int(x_string, 2)
    y_int = int(y_string, 2)

    return BinaryNumber(x_int + y_int)


def subquadratic_multiply(x, y):
    #this is to handle the fact that x and y might be passed in as a
    #BinaryNumber or a list
    try:
        n = max(len(x), len(y)) #if its a list, get the length
    except:
        x = x.binary_vec #if its not a list, extract the list, then get length
        y = y.binary_vec
        n = max(len(x), len(y))

    #base case
    if n == 1:
        return int(x[0]) * int(y[0])

    #recusive case
    else:
        while len(x) > len(y): #add zeros to beginning of y to make them equal length
            y.insert(0, '0')

        while len(y) > len(x): #add zeros to beginning of x to make them equal length
            x.insert(0, '0')

        if n % 2 != 0: #make x and y an even amount of digits
            x.insert(0, '0')
            y.insert(0, '0')
            n += 1

        #split lists in half
        xl = x[:n // 2]
        xr = x[n // 2:]
        yl = y[:n // 2]
        yr = y[n // 2:]

        #these two variables are of type BinaryNumber
        xl_plus_xr = binary_addition(xl, xr, n)
        yl_plus_yr = binary_addition(yl, yr, n)

        #do recusrion
        xl_plus_xr__times__yl_plus_yr = subquadratic_multiply(xl_plus_xr, yl_plus_yr)
        xl_times_yl = subquadratic_multiply(xl, yl)
        xr_times_yr = subquadratic_multiply(xr, yr)

        middle_term = xl_plus_xr__times__yl_plus_yr - xl_times_yl - xr_times_yr

        return ((2 ** n) * xl_times_yl + 2 ** (n // 2) * middle_term + xr_times_yr)


## Feel free to add your own tests here.
def test_quadratic_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(12)) == 10 * 12
    assert quadratic_multiply(BinaryNumber(123456), BinaryNumber(98765)) == 123456 * 98765


def test_subquadratic_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2
    assert subquadratic_multiply(BinaryNumber(56), BinaryNumber(120567)) == 56 * 120567
    assert subquadratic_multiply(BinaryNumber(627), BinaryNumber(726)) == 627 * 726

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(BinaryNumber(x), BinaryNumber(y))
    return (time.time() - start) * 1000


#this function doesnt work all the time
#not sure how this should be changed because the functions are implemented correctly
def compare_multiply():
    # compare the empirical runtimes of multiplication functions
    ### TODO - add test cases and measure runtime

    sizes = [800,900,1000]

    for i in range(len(sizes)):
        quad_time = time_multiply(sizes[i], sizes[i], quadratic_multiply)
        subquad_time = time_multiply(sizes[i], sizes[i], subquadratic_multiply)

        #if it isn't working as expected, break
        if quad_time < subquad_time:
            print("Broken")
            break

        print("In loop ", i+1)
        print("quadratic time:    ", quad_time)
        print("subquadratic time: ", subquad_time, "\n")
