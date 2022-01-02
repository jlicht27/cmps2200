# CMPS 2200 Recitation 05
## Answers

**Name:** Jonathan Licht
**Name:**_________________________


Place all written answers from `recitation-05.md` here for easier grading.




- **3)**

The work of get_positions is O(n). It uses scan followed by 2 constant time operations so it just depends on scan which is linear.

The same logic aplies to span. The span of scan is O(lgn) so the span is O(lgn)

- **5)**

The work of construct_output is O(n) becuase it iterates through the list once. The span is also O(n) because it can't be parallelized at all.

- **6)**

The work and span are both O(n) because it calls 3 linear functions which is O(3n) which is just simply O(n).

- **8)**

It depends on the work and span of reduce which are:
Work: O(n)
Span: O(lgn)
