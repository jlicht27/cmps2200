# CMPS 2200  Recitation 02

**Name (Team Member 1):** Jonathan Licht
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences.
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.

## Setup
- Login to Github.
- Click on the assignment link posted on canvas and accept the assignment.
- Click on your personal github repository for the assignment (e.g., https://github.com/CMPS2200-Fall2021/recitation-01-your_username).
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
## Running and testing your code
- You can run the tests using `pytest`. To install `pytest`, on your terminal:
  + `pip3 install pytest`
  + You may also have to install other python modules such as `tabulate` or other imported modules as you work through these recitations.
- It's usually best to run only one test at a time. To run tests, from the command-line, you can run
  + `pytest -s main.py` will run all tests
  + `pytest -s main.py::test_one` will just run `test_one`
- If you want to run your whole program, make sure to use `python3`. `python` still defaults to python version 2.

## Turning in your work
- You may work with a partner to complete this recitation.
- Only one team member needs to push your completed lab to github.
- In the README.md file, include the names of the team members.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [x] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [x] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [x] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [x] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = n$, and $f(n) = n^2$  with $a=2$ and $b=2$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

f(n) = 1:

C(root) = 1
C(level 1) = 2 * 1
so it is leaf dominated
there are n leaves * constant work on each leaf
W(n) when f(n) = 1 is O(n)

f(n) = n:

C(root) = n
C(level 1) = (n/2) + (n/2) = n
so it is balanced
maximum cost per level is n * number of levels is lgn
W(n) when f(n) = n is O(nlgn)

f(n) = n^2:

C(root) = n^2
C(level 1) = (n/2)^2 + (n/2)^2 = n^2/2
so it is root dominated
W(n) when f(n) = n^2 is O(n^2)

Results for testing this are in the test_work() function.

- [x] 5. (4 points) Now that you have a nice way to empirically generate values of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asymptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.

if for all examples we have a = b = 2

c < logb(a):

W(n) = 2W(n/2) + n^log2(1)
W(n) = 2W(n/2) + 1
C(root) = 1
C(level 1) = 2 * 1
so it is leaf dominated
there are n number of leaves * constant work on each leaf
W(n) = O(n)

c = logb(a):

W(n) = 2W(n/2) + n^log2(2)
W(n) = 2W(n/2) + n
C(root) = n
C(level 1) = (n/2) + (n/2) = n
so it is balanced
num of levels is logn * n maximum amount of work per level
W(n) = O(nlogn)

c > logb(a):

W(n) = 2W(n/2) + n^log2(4)
W(n) = 2W(n/2) + n^2
C(root) = n^2
C(level 1) = (n/2)^2 + (n/2)^2 = n^2/2
so it is root dominated
W(n) = O(n^2)

        f(n) is  f(n) is  f(n) is
   n    constant  linear  quadratic
|-------|-------|--------|-----------|
|    10 |    15 |     36 |       174 |
|    20 |    31 |     92 |       748 |
|    50 |    63 |    276 |      4790 |
|   100 |   127 |    652 |     19580 |
|  1000 |  1023 |   9120 |   1990744 |
|  5000 |  8191 |  61728 |  49957880 |
| 10000 | 16383 | 133456 | 199915760 |

Here are the results from the scenarios described above

- [x] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should.

f(n) = 1:

C(root) = 1
C(level 1) = 1
so it is balanced
number of levels lgn * the max span per level 1
S(n) = O(lgn)

f(n) = n:

C(root) = n
C(level 1) = n/2
it is root dominated
S(n) = O(n)

f(n) = n^2:

C(root) = n^2
C(level 1) = (n/2)^2 = n^2/4
it is root dominated
S(n) = n^2

        f(n) is  f(n) is  f(n) is
   n    constant  linear  quadratic
|-------|-------|-------|-----------|
|    10 |     4 |    18 |       130 |
|    20 |     5 |    38 |       530 |
|    50 |     6 |    97 |      3315 |
|   100 |     7 |   197 |     13315 |
|  1000 |    10 |  1994 |   1333214 |
|  5000 |    13 |  9995 |  33332873 |
| 10000 |    14 | 19995 | 133332873 |
