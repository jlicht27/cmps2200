# CMPS 2200 Assignment 4
## Answers

**Name:** Jonathan Licht


Place all written answers from `assignment-04.md` here for easier grading.


- **1a.**

If X is the amount of work done by quicksort then α should be n^2. This is then saying the probability of the work being done by quicksort is ≥ to n^2. The expected value of the work of quicksort is nlogn.
Therefore P(X ≥ n^2) ≤ nlgn / n^2 = logn / n.

- **1b.**

P(X ≥ 10^c * nlgn) ≤ nlgn / 10^c * nlgn = 1 / 10^c.


- **2a.**

Algorithm A can be improved to A' by increasing the number of trials. This type of algorithm is a monte carlo algorithm. Generally, as we increase the number of trials to estimate the result, the estimate becomes more accurate.

The number of trials should be as follows:

(1-ε)^k = (1-δ)
log((1-ε)^k) = log(1-δ)
k = log(1-δ) / log(1-ε)

We need to try A(I) k times.

W(A') = W(k * n)

- **2b.**

The best way to go about this is as follows:

  while true:
    run A(I)
    if C(A(I)) is correct using v(n):
      return C(A(I))
      break

This depends on the probability ε and and w(n) since v(n) ∈ O(w(n)).


- **3b.**

results for shuffled list:

|     n |   qsort-fixed-pivot |   qsort-random-pivot |       ssort |   tim-sort |
|-------|---------------------|----------------------|-------------|------------|
|   100 |            0.161171 |             0.180006 |    0.225782 |   0.001907 |
|   200 |            0.314951 |             0.381231 |    0.751734 |   0.002146 |
|   400 |            0.605106 |             0.737906 |    2.774954 |   0.003815 |
|   600 |            0.922203 |             1.165867 |    6.373167 |   0.011206 |
|   800 |            1.243830 |             1.667738 |   10.298252 |   0.005960 |
|  1000 |            1.590014 |             1.865864 |   16.044140 |   0.008345 |
|  2000 |            3.431797 |             3.938198 |   63.045740 |   0.015020 |
|  4000 |            7.006884 |             8.225203 |  256.635189 |   0.033617 |
|  6000 |           10.236025 |            12.653112 |  580.804825 |   0.097036 |
|  8000 |           14.858007 |            17.748833 | 1036.417723 |   0.103235 |
| 10000 |           18.935919 |            22.662163 | 1621.300936 |   0.113249 |

results for a presorted list:

|     n |   qsort-fixed-pivot |   qsort-random-pivot |       ssort |   tim-sort |
|-------|---------------------|----------------------|-------------|------------|
|   100 |            0.601053 |             0.183821 |    0.186205 |   0.002146 |
|   200 |            1.729965 |             0.386238 |    0.622034 |   0.002146 |
|   400 |            6.294012 |             0.770092 |    2.983809 |   0.007868 |
|   600 |           13.630867 |             1.218796 |    5.072117 |   0.006914 |
|   800 |           25.634766 |             1.571178 |    9.078741 |   0.010014 |
|  1000 |           35.156965 |             2.080917 |   13.756990 |   0.010014 |
|  2000 |          140.963793 |             4.011154 |   58.865070 |   0.019073 |
|  4000 |          558.773994 |             9.332895 |  226.337194 |   0.036001 |
|  6000 |         1253.655672 |            12.712955 |  473.405838 |   0.082970 |
|  8000 |         2297.745943 |            16.216993 |  842.610121 |   0.106096 |
| 10000 |         3456.832886 |            21.496058 | 1312.573910 |   0.076056 |



For qsort-fixed-pivot, having a shuffled list is far better. A shuffled list is nlgn and having a presorted list makes the runtime n^2. This difference is clearly evident in the table.

For qsort_random_pivot, having a presorted or shuffled list doesn't matter that much. The results are about the same. They are both nlgn.

- **3c.**

Whatever algorithm tim_sort uses is far superior to any implementation in this lab. It is not sensitive to presort or shuffled lists and its way faster than the other 3 at any list size.
