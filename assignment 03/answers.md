# CMPS 2200 Assignment 3
## Answers

**Name:** Jonathan Licht


Place all written answers from `assignment-03.md` here for easier grading.


- **1b.**

The work and span depend on iterate()'s work and span. It is O(n) for both.

- **1d.**

The work and span depend on reduce()'s work and span. The work is O(n) and the span is O(lgn).

- **1e.**

The work would remain the same. However the span would be dependant only on the longer tree.
S(n) = S(2n/3) + n
This works out to be root dominated and so the span is O(n)

- **3b.**

Work:

W(n) = W(n-1) + 1
W(n) = W(n-k) + k
when k = n:
W(n) = W(n-k) + k
W(n) = n + 1
W(n) = O(n)

Span:

S(n) = S(n-1) + 1
using the same logic:
S(n) = O(n)

- **3d.**

The work would linear O(n) because scan is linear and then we use reduce to find the mininum element of the list which is also linear.

The span would be logarithmic O(lgn) because span of both scan and reduce are O(lgn)

- **3f.**

Work:

W(n) = 2W(n/2) + 1
C(root) = 1
C(level 1) = 2 * 1
it is leaf dominated so
there are n leaves and constant time on each leaf so
W(n) = O(n)

Span:

W(n) = W(n/2) + 1
C(root) = 1
C(level 1) = 1
it is balanced
num of levels is lgn * max work per leaf is constant
S(n) = O(lgn)
