

# CMPS 2200 Assignment 1

**Name:** Jonathan Licht


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository.



1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?

    - Yes because 2^(n+1) = 2 * 2^n. when you drop constants it is 2^n so 2^n is in O(2^n).


  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?

    - No because there is no constant c that can be multiplied times 2^n that will asymptotically dominate 2^(2^n)


  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?

    - No because there is no constant c that can be multiplied times log^2(n) that will asymptotically dominate n^1.01


  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?

    - Yes because for every c, n^1.01 asymptotically dominates c * log^2(n)


  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?

    - No because there is no constant c that can be multiplied by (log(n))^3 that will asymptotically dominate sqrt(n).


  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?

    - Yes because for every c, sqrt(n) asymptotically dominates c * (log(n))^3


  - 1g. Consider the definition of "Little o" notation:

$g(n) \in o(f(n))$ means that for **every** positive constant $c$, there exists a constant $n_0$ such that $g(n) \le c \cdot f(n)$ for all $n \ge n_0$. There is an analogous definition for "little omega" $\omega(f(n))$. The distinction between $o(f(n))$ and $O(f(n))$ is that the former requires the condition to be met for **every** $c$, not just for some $c$. For example, $10x \in o(x^2)$, but $10x^2 \notin o(x^2)$.



**Prove** that $o(g(n)) \cap \omega(g(n))$ is the empty set.

let w represent lowercase omega.

Suppose it is not the empty set and f(n) is both in o(g(n)) and w(g(n))

f(n) = w(g(n)) if and only if g(n) = o(f(n)) and f(n) = o(g(n))
f(n) = o(f(n)) for all values of c that are non-negative

f(n) < c * f(n)
if c = 1 the above statement is false

2. **SPARC to Python**

Consider the following SPARC code:
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\
~~~~~~~~~~~~ra + rb\\
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$

  - 2a. Translate this to Python code -- fill in the `def foo` method in `main.py`

  - 2b. What does this function do, in your own words?

  This function returns the nth term of the fibonacci sequence.

3. **Parallelism and recursion**

Consider the following function:

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`

  - 3a. First, implement an iterative, sequential version of `longest_run` in `main.py`.

  - 3b. What is the Work and Span of this implementation?

  The work of this version is O(n) because it only goes through the list once. The span is the same becuase it is not parallelized at all.


  - 3c. Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.

  - 3d. What is the Work and Span of this sequential algorithm?

 . W(n) = 2W(n/2) + c1
   C(root level) = c1
   C(level 1) = c1 + c1 = 2 * c1
   2 * c1 > c1 so it is leaf dominated

   Amount of leaves in a perfectly balanced binary tree is n leaves
   so it is c1 amount of work * n leaves

   number of levels in tree = lgn

   so the total work is O(n*lgn)

 . The span is the same as the work because the algorithm isn't parallelized.


  - 3e. Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?

 . The work remains the same: O(n*lgn)

 . The span decreases though:
   S(n) = S(n/2) + c1
   S(root level) = c1
   S(level 1) = c1
   so it is balanced

   The maximum span for all levels is c1
   The total amount of levels is lgn
   so c1 * lgn

   So the span is O(lgn)
