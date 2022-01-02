# CMPS 2200 Recitation 11

## Answers

**Name:** Jonathan Licht



Place all written answers from `recitation-12.md` here for easier grading.



- **2)**

The worst case scenario for this is if every element is connected to every other element. If it has k connected components then the work would be O(k * ElogE). It does ElogE work for each connected component k.

- **4)**

The first part of mst_from_points is O(V^2) where is V the total number of vertices. It iterates over the list of points 2 times in a nested for loop. Then it calls on prim. Because everything is connected in this example, the runtime for prim is O(ElogE) because k is 1. For this example then the work is O(V^2 + ElogE).
