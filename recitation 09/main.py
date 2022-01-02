def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number.
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """
    counts[n] += 1
    if n <= 1:
        return n
    else:
         return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)

def test_fib_recursive():
    n = 10
    counts = [0] * (n+1)
    assert fib_recursive(n, counts) == 55
    print(counts)
    print(sum(counts))

def fib_top_down(n, fibs):
    if fibs[n] == -1:
        if n <= 1:
            fibs[n] = n
            return fibs[n]
        else:
             fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
             return fibs[n]
    else:
        return fibs[n]

def test_fib_top_down():
    n = 10
    fibs = [-1] * (n+1)
    assert fib_top_down(n, fibs) == 55
    print(fibs)

def fib_bottom_up(n):
    fibs = [0] * (n+1)
    for i in range(len(fibs)):
        if i == 0:
            fibs[i] = 0
        elif i == 1:
            fibs[i] = 1
        else:
            fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]

def test_fib_bottom_up():
    n = 10
    assert fib_bottom_up(n) == 55
