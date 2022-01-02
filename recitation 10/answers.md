# CMPS 2200 Recitation 10## Answers

**Name:** Jonathan Licht


Place all written answers from `recitation-10.md` here for easier grading.



- **2)**

The work of reachable is O(n + m) because it only reaches each node and edge once.

- **4)**

1 time. If the graph is connected, we can call reachable from any node, and it will return the True. If it's not connected it will return a list that is not the same as the total list of nodes and therefore false.

- **5)**

O(n + m) because it calls reachable only one time. The work outside the function call is O(n) which is also linear so it ends up with the same result.

- **7)**

It would remain the same. You could use the same logic to accomplish the same goal just the implementation would be different.
