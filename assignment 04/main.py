import random, time
import tabulate

#added this to test bigger numbers
import sys
sys.setrecursionlimit(11000)

def ssort(L):
    for i in range(len(L)):
        #print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L


def qsort(a, pivot_fn):

    if len(a) == 1:
        return [a[0]]
    if len(a) == 0:
        return []
    else:
        pivot = pivot_fn(a)
        small = [i for i in a if i < pivot]
        mid = a[a.index(pivot)]
        large = [i for i in a if i > pivot]

        return qsort(small, pivot_fn) + [mid] + qsort(large, pivot_fn)


def time_sort(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 400, 600, 800, 1000, 2000, 4000, 6000, 8000, 10000]):
    """
    Compare the running time of different sorting algorithms.
    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    def qsort_fixed_pivot(x):
        return qsort(x, lambda a: a[0])

    def qsort_random_pivot(x):
        return qsort(x, lambda a: random.choice(a))

    def tim_sort(x):
        return sorted(x)

    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_sort(qsort_fixed_pivot, mylist),
            time_sort(qsort_random_pivot, mylist),
            time_sort(ssort, mylist),
            time_sort(tim_sort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort_fixed_pivot', 'qsort_random_pivot', 'ssort','tim-sort'],
                            floatfmt=".6f",
                            tablefmt="github"))

def test_qsort_fixed():
	assert(qsort([5,4,3,2,1], lambda a: a[0])) == [1,2,3,4,5]

def test_qsort_random():
	assert(qsort([5,4,3,2,1], lambda a: random.choice(a))) == [1,2,3,4,5]

random.seed()
print_results(compare_sort())
