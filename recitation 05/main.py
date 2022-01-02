from collections import defaultdict


def supersort(a, k):
    """
    The main sorting algorithm. You'll complete the
    three funcions count_values, get_positions, and construct_output.

    Params:
      a.....the input list
      k.....the maximum element in a

    Returns:
      sorted version a
    """
    counts = count_values(a, k)
    positions = get_positions(counts)
    return construct_output(a, positions)


def count_values(a, k):
    """
    Params:
      a.....input list
      k.....maximum value in a

    Returns:
      a list of k values; element i of the list indicates
      how often value i appears in a

    >>> count_values([2,2,1,0,1,0,1,3], 3)
    [2, 3, 2, 1]
    """
    result = [0] * (k + 1)
    for i in a:
        result[i] += 1
    return result


def test_count_values():
    assert count_values([2, 2, 1, 0, 1, 0, 1, 3], 3) == [2, 3, 2, 1]


def test_count_values_hard():
    assert count_values([2, 2, 1, 1, 6, 6, 1, 3], 6) == [0, 3, 2, 1, 0, 0, 2]


def get_positions(counts):
    """
    Params:
      counts...counts of each value in the input
    Returns:
      a list p where p[i] indicates the location of the first
      appearance of i in the desired output.

    >>> get_positions([2, 3, 2, 1])
    [0, 2, 5, 7]
    """
    result = scan(plus, 0, counts)[0]
    result.insert(0, 0)
    del result[-1]
    return result


def test_get_positions():
    assert get_positions([2, 3, 2, 1]) == [0, 2, 5, 7]


def construct_output(a, positions):
    """
    Construct the final, sorted output.

    Params:
      a...........input list
      positions...list of first location of each value in the output.

    Returns:
      sorted version of a

    >>> construct_output([2,2,1,0,1,0,1,3], [0, 2, 5, 7])
    [0,0,1,1,1,2,2,3]
    """
    result = [-1] * len(a)
    for i in a:
        result[positions[i]] = i
        positions[i] += 1
    return result


def test_construct_output():
    assert construct_output([2, 2, 1, 0, 1, 0, 1, 3], [0, 2, 5, 7]) == [0, 0, 1, 1, 1, 2, 2, 3]


def count_values_mr(a, k):
    """
    Use map-reduce to implement count_values.
    This is done; you'll have to complete count_map and count_reduce.
    """
    # done.
    int2count = dict(run_map_reduce(count_map, count_reduce, a))
    return [int2count.get(i, 0) for i in range(k + 1)]


def test_count_values_mr():
    assert count_values_mr([2, 2, 1, 0, 1, 0, 1, 3], 3) == [2, 3, 2, 1]


def count_map(value):
    # hint: this function should return a list, even if that list
    # contains a single tuple
    return [(value, 1)]


def count_reduce(group):
    return (group[0], reduce(plus, 0, group[1]))


# the below functions are provided for use above.
def run_map_reduce(map_f, reduce_f, mylist):
    # done.
    # explanation:
    # apply map_f to every element of mylist, returning a list of
    # tuples [(value_0, map_f(value_0)), (value_1, map_f(value_1)), ...]
    pairs = flatten(list(map(map_f, mylist)))
    # collect tuples with the same value into single tuples
    # (value, [list of mapped values])
    # e.g, [(2,1), (2,1)] becomes [(2,[1,1])]
    groups = collect(pairs)
    # reduce each tuple, e.g., [(2,[1,1])] becomes [(2,2)]
    return [reduce_f(g) for g in groups]


def collect(pairs):
    # done.
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())


def plus(x, y):
    # done.
    return x + y


def scan(f, id_, a):
    # done. inefficient but in analysis assume efficient
    # implementation from lecture
    return (
        [reduce(f, id_, a[:i + 1]) for i in range(len(a))],
        reduce(f, id_, a)
    )


def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        return f(reduce(f, id_, a[:len(a) // 2]),
                 reduce(f, id_, a[len(a) // 2:]))


def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])


def flatten(sequences):
    return iterate(plus, [], sequences)
