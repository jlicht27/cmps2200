# CMPS 2200 Recitation 05
## Answers

**Name:** Jonathan Licht


Place all written answers from `recitation-08.md` here for easier grading.



- **1)**

In general, the work/span of deleteMin is O(n) because it is linear time to find the smallest element and then removing it is a constant time operation.

In general, the work/span of inserting an element into a list is O(1).

- **2a)**

The depth of the tree is lg(n).

- **2b)**

The minimum element is at the top of the tree. The maximum element is somewhere in the bottom level of the tree but we can't say exactly where it is.

- **4)**

The work/span of these operations is O(lgn). This is because you iterate through the depth of the tree which is lg(n).

- **6)**

In this implementation there are two loops. The first loop, it iterates over the entire list a. In each iteration, it adds an element to the list and then calls reheapUp which has logarithmic work/span as stated above. So it is n iterations times lg(n) in each iteration which is nlgn.

In the second loop, it iterates over the list again. It removes the min element and adds it to the final result. Removing the min element is logarithmic because it calls reheapDown which has logarithmic work/span as stated above.
So this is also n iteration times lg(n) in each iteration which is also nlgn.

The final result is 2nlgn which is in O(nlgn).
