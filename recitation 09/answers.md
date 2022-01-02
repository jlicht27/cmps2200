# CMPS 2200 Recitation 09
## Answers

**Name:** Jonathan Licht

Place all written answers from `recitation-09.md` here for easier grading.



- **2)**

W(n) = W(n-1) + W(n-2) + C where C is some constant

Lower Bound:

  W(n-1) ≈ W(n-2)...

  W(n) = 2W(n-2) + C
  W(n) = 2(2W(n-4) + C) + C
  W(n) = 4W(n-4) + 3C
  W(n) = 8W(n-6) + 7C

  W(n) = 2^k (n - 2k) + (2^k - 1)C

  for W(0):
    n - 2k = 0 -> k = n/2
    W(n) = 2^k W(0) + 2^(n/2) - 1)C
    ≈ 2 ^ (n /2)


Upper Bound:

  W(n-2) ≈ W(n-1)...

  W(n) = 2W(n-1) + C
  W(n) = 4W(n-2) + 3C
  W(n) = 8W(n-3) + 3C

  W(n) = 2^k (n - k) + (2^k - 1)C

  for W(0):
    n - k = 0 -> k = n
    W(n) = 2^k W(0) + (2^n - 1)C
    ≈ 2^n


So, W(n) is O(2^a) where a is some number between n/2 and n. Either way this is exponential growth and is inefficient.

- **3)**

Span is only dependent on the longer of the two trees so:

S(n) = S(n-1) + 1

C(root) = 1
C(level 1) = 1

balanced

max cost per level times num of levels:

1 * n so S(n) is in O(n)

- **4)**

It is the fibonacci sequence but in reverse order except for the 0th element

- **6)**

It is called n times. therefore the work and span are both linear O(n).

- **8)**

Each element will be read 2 times. once for the element above it and once for the element 2 above it. Still we are iterating over a list so it is it is O(n).
