# CMPS 2200  Recitation 11

In this lab we'll investigate minimum spanning tree algorithms.


1. In class, we gave an implementation of Prim's algorithm. It assumes that the input graph $G$ is connected. What if it's not? Modify `prim` to return a list of trees, one per connected component. Test with `test_prim`.

.  
.  
.  


2. What is the worst-case work of your algorithm, assuming $G$ has $k$ connected components?

**put in answers.md**

.  
.  
.  

3. Consider the problem of finding the MST to connect a list of cities by roads. If we have as input the (x,y) coordinates of each city, we can first build a fully-connected, undirected, weighted graph, where each pair of cities is joined by an edge with weight equal to the Euclidean distance between their coordinates. Complete `mst_from_points` to find the MST from a list of points, and test with `test_mst_from_points`. 

.  
.  
.  

4. What is the work of your full algorithm in the previous answer?

**put in answers.md**

.  
.  
.  
