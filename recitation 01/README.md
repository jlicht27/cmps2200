# CMPS 2200  Recitation 01

**Name (Team Member 1):** Jonathan Licht
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Login to Github.
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment (e.g., https://github.com/tulane-cmps2200/recitation-01-your_username).
- [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) the repository to your local device
- Complete the lab task
- [Add, commit, and push](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-using-the-command-line/adding-a-file-to-a-repository-using-the-command-line) your completed lab back up to GitHub.
  - You will need to issue `git add` for all files that you have modified, e.g., `main.py`, `README.md`, and any others that you modify as well.
  - For example, on the command line, in the same directory as your cloned lab:
```
$ git add main.py
$ git commit -m "Implement Required Functions"
$ git push origin main
```

You'll work with a partner to complete this recitation. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Turning in your work
- Only one team member needs to push your completed lab to github.
- In the README.md file, include the name of the team members.


## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

- [x] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`.

- [x] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [x] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [x] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`?

The worst case input value of `key` for `linear_search` would be the last element in the list.
The worst case input value of `key` for `binary_search` would be the first or last element in the list.

- [x] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`?

The best case input value of `key` for `linear_search` would be the first element in the list.
The best case input value of `key` for `binary_search` would be the middle element in the list.

- [x] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [x] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [x] 8. Call `print_results(compare_search())` and paste the results here:

|            n |   linear |   binary |
|--------------|----------|----------|
|       10.000 |    0.001 |    0.004 |
|      100.000 |    0.004 |    0.006 |
|     1000.000 |    0.051 |    0.005 |
|    10000.000 |    0.544 |    0.008 |
|   100000.000 |    5.885 |    0.012 |
|  1000000.000 |   57.918 |    0.018 |
| 10000000.000 |  567.487 |    0.026 |

- [x] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

Yes it does match. The linear times grow linearly and the binary times grow logarithmically.

- [x] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times.
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search?

  The worst-case complexity would be linear O(kn). This is k times of searching multiplied the worst case scenario which is linear.

  + For binary search?

  The worst-case complexity would be O(n^2 + klog(n)). It only needs to be sorted once and then it's k times of searching mulitplied by the worst case scenario which is logarithmic.


  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting?

  It is more efficient to sort first and then use binary search for values of k that are less than n^2 / (n - log(n))
