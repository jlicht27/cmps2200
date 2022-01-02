"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate


###


def simple_work_calc(n, a, b):
    """Compute the value of the recurrence $W(n) = aW(n/b) + n

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor

    Returns: the value of W(n).
    """

    if n == 1:
        return n
    else:
        return n + a * simple_work_calc(n // b, a, b)


def test_simple_work():
    """ done. """
    assert simple_work_calc(8, 2, 2) == 32
    assert simple_work_calc(8, 3, 2) == 65
    assert simple_work_calc(9, 2, 3) == 19
    assert simple_work_calc(16, 2, 4) == 28
    assert simple_work_calc(64, 2, 2) == 448
    assert simple_work_calc(16, 3, 2) == 211


def work_calc(n, a, b, f):
    """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor
    f......a function that takes an integer and returns
           the work done at each node

    Returns: the value of W(n).
    """
    if n == 1:
        return n
    else:
        return f(n) + a * work_calc(n // b, a, b, f)


def span_calc(n, a, b, f):
    """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor
    f......a function that takes an integer and returns
           the work done at each node

    Returns: the value of W(n).
    """
    if n == 1:
        return n
    else:
        return f(n) + span_calc(n // b, a, b, f)


def test_work():
    """ done. """
    # first set of tests for problem 3
    assert work_calc(8, 2, 2, lambda n: n) == 32
    assert work_calc(8, 1, 2, lambda n: n * n) == 85
    assert work_calc(8, 3, 2, lambda n: 1) == 40
    assert work_calc(4, 2, 2, lambda n: n) == 12
    assert work_calc(4, 3, 2, lambda n: n) == 19
    assert work_calc(4, 3, 2, lambda n: n * n * n) == 97

    # second set of tests for confirming asymptotic behavior for problem 4

    # constant
    assert work_calc(10, 2, 2, lambda n: 1) == 15
    assert work_calc(100, 2, 2, lambda n: 1) == 127
    assert work_calc(1000, 2, 2, lambda n: 1) == 1023

    # linear
    assert work_calc(10, 2, 2, lambda n: n) == 36
    assert work_calc(100, 2, 2, lambda n: n) == 652
    assert work_calc(1000, 2, 2, lambda n: n) == 9120

    # quadratic
    assert work_calc(10, 2, 2, lambda n: n * n) == 174
    assert work_calc(100, 2, 2, lambda n: n * n) == 19580
    assert work_calc(1000, 2, 2, lambda n: n * n) == 1990744


def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
    """
    Compare the values of different recurrences for
    given input sizes.

    Params:
    work_fn1....a curried version of work_calc expecting a single input n
    work_fn2....a curried version of work_calc expecting a single input n
    sizes.......list of values for n to compare these two work functions.

    Returns:
    A list of tuples of the form
    [(n, work_fn1(n), work_fn2(n)), ...)

    """
    result = []
    for n in sizes:
        # compute W(n) using current a, b, f
        result.append((
            n,
            work_fn1(n),
            work_fn2(n)
        ))
    return result


def print_work_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers=['n', 'W_1', 'W_2'],
                            floatfmt=".3f",
                            tablefmt="github"))


def print_span_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers=['n', 'S_1', 'S_2'],
                            floatfmt=".3f",
                            tablefmt="github"))


def curry_work(a, b, f):
    return lambda n: work_calc(n, a, b, f)


def test_compare_work():
    # curry work_calc to create multiple work
    # functions that can be passed to compare_work

    # create work_fn1
    work_fn1 = curry_work(2, 2, lambda n: 1)
    # create work_fn2
    work_fn2 = curry_work(2, 2, lambda n: n ** 2)

    res = compare_work(work_fn1, work_fn2)
    print_work_results(res)


def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
    """
    Compare the values of different span recurrences for
    given input sizes.

    Params:
    span_fn1....a curried version of span_calc expecting a single input n
    span_fn2....a curried version of span_calc expecting a single input n
    sizes.......list of values for n to compare these two span functions.

    Returns:
    A list of tuples of the form
    [(n, span_fn1(n), span_fn2(n)), ...]

    """
    result = []
    for n in sizes:
        # compute S(n) using current a, b, f
        result.append((
            n,
            span_fn1(n),
            span_fn2(n)
        ))
    return result


def curry_span(a, b, f):
    return lambda n: span_calc(n, a, b, f)


def test_compare_span():
    assert span_calc(10, 2, 2, lambda n: 1) == 4
    assert span_calc(20, 1, 4, lambda n: n * n) == 426
    assert span_calc(30, 3, 4, lambda n: n) == 38
    assert span_calc(8, 2, 2, lambda n: n) == 15

    ## make span_fn1 and span_fn2

    span_fn1 = curry_span(2, 2, lambda n: 1)
    span_fn2 = curry_span(2, 2, lambda n: n ** 2)
    res = compare_span(span_fn1, span_fn2)
    print_span_results(res)
