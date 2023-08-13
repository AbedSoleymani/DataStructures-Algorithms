# DataStructures and Algorithms

This repo is about how to write code to **solve algorithmic problems** and to do so **efficiently** in terms of computation and memory demand.
You're likely aware that computers have the capacity to tackle a wide varity of challenges—ranging from determining optimal travel routes on a map to deciphering the human genome sequence.
However, the methods for problem-solving are rarely unique, with certain approaches offering significantly heightened efficiency compared to others.
Although both of these approaches may resolve the same problem, their execution time can vary greatly, ranging from mere milliseconds to prolonged hours.

How can you analyze a problem and identify multiple potential solutions?
Furthermore, how can you assess the relative efficiency of these approaches?
Will your solution run quickly or slowly?
Will it consume substantial memory space or very small?
Proficiency in addressing such inquiries will make you a more effective software developer.

## Steps to solve an algorithmic problem
1. Carefully specify the **inputs**
2. What are the **outputs**?
3. Understand the **relationship** between inputs/outputs by some examples.
4. Consider **systematically** how a human solves this problem!
5. Forget the implementation details, write a **pseudocode**.
6. Try to develope a simple **mechanical solution**. At this step, do not optimize prematurely! Just find a simple and correct answer.
7. Write the code!

## Efficiency
Until now, we've explored the fundamental elements of solving algorithmic problems, but we haven't given extensive thought to how effective our solutions are.
When we talk about a program's effectiveness, we're not solely focused on its speed.
We're also taking into account the time it needs to operate and the memory space it occupies in the computer.
Frequently, there's a balance between these two factors.
You might need to make a choice between designing a program that operates quicker by opting for a data structure that consumes more memory or going the other way around.

Code efficiency or complexity refers to how well a computer program utilizes computational resources, such as time and memory, to perform its tasks. It's a measure of how optimized and well-designed a program is in terms of resource usage. Let's consider these two algorithms:<br>
```
def some_function(n):
    for i in range(2):
        n += 100
    return n
```
There are four lines in total, but the line inside the for loop will get run twice. So running this code will involve running 5 lines.

Now let's look at another example:
```
def other_function(n):
    for i in range(100):
        n += 2
    return n
```
<br>In this case, the code inside the loop runs 100 times. So running this code will involve running 103 lines!<br>
Although the two functions have the exact same end result, one of them iterates many times to get to that result. Counting lines of code is not a perfect way to quantify efficiency, and we'll see that there's a lot more to it as we go through the program.<br>
For this fucntion<br>
```
def say_hello(n):
    for i in range(n):
        print("Hello!")
```
<br>As the input to an algorithm increases, the time required to run the algorithm may also increase. In technical words, the complexity of this code is $O(n)$: linear rate of increase.<br>
Similarly, the complexity of this code
```
def say_hello(n):
    for i in range(n):
        for i in range(n):
            print("Hello!")
```
is $O(n^2)$: quadratic rate of increase.<br>
Notice that if $n$ is very small, it doesn't really matter which function we use—but as we put in larger values for $n$, the function with the nested loop will quickly become far less efficient (please see the diagram below).<br><br><br>
<img width="514" alt="Screenshot 2023-08-06 at 6 01 07 PM" src="https://github.com/AbedSoleymani/DataStructures-Algorithms/assets/72225265/038d077c-ec12-4a54-9ad7-d4424b613e28">
<br>
The rate of increase of an algorithm is also referred to as the _order_ of the algorithm. For such important concept, mathematicians developed a form of notation called big $O$ notation.<br>
The choice of data structures also play a crucial role in determining the efficiency and complexity of algorithms and code which we will discuss in the following section.

## Data structures
The choice of the right data structure for a specific problem can significantly impact the performance and resource usage of your code. Moreover, good choice of data structure can impact the readability and maintainability of your code. Using an appropriate data structure makes the code easier to understand and reduces the chances of errors.<br>
Data structures are like storage units that arrange and group information in various manners. Whenever you create a program to tackle a task, data is inevitably involved. The manner in which you organize or arrange this data in the computer's memory can greatly influence the range of operations you can perform with it and how smoothly and effectively you can carry out those operations.

We will start with a very general structure—a _collection_. Collections:
* Don't have a particular order (so you can't say "give me the 3rd element in this collection")
* Don't have to have objects of the same type

<br>Here are several examples of collections: lists, arrays, linked lists, stacks, queues, sets, maps (dictionaries), trees, and graphs.

**Lists**: have an order (so you can say things like "give me the 3rd item in the list") and they have no fixed length (you can add or remove elements).

**Arrays**: have some things in common with lists. In both cases, there is a collection of items and the items have an order to them. But they have some differences in terms of their properties, behavior, and usage.
* _Fixed vs. Dynamic Size_:
    * Arrays: Arrays have a fixed size, meaning you need to specify the size when creating them. Once created, the size cannot be changed.
    * Lists: Lists have a dynamic size, meaning you can add or remove elements without specifying an initial size. They can grow or shrink as needed.
* _Memory Allocation_:
    * Arrays: Arrays are often allocated a contiguous block of memory, which can make them more memory-efficient in terms of memory overhead.
    * Lists: Lists may use more memory due to their dynamic nature, as they might allocate extra space for potential growth.
* _Performance_:
    * Arrays: Accessing elements in an array is generally faster due to their fixed memory layout and direct indexing.
    * Lists: Accessing elements in a list might be slightly slower compared to arrays, especially when using sequential searching or when the list has to be resized.
* _Insertions and Deletions_:
    * Arrays: Inserting or deleting elements in the middle of an array can be inefficient, as it might require shifting elements to make space or close gaps.
    * Lists: Lists handle insertions and deletions more efficiently since they are designed for dynamic resizing.

**</ins>Linked list</ins>**: A linked list is a linear data structure used in computer science and programming to organize and store a collection of elements. Unlike arrays, which use a contiguous block of memory to store elements, linked lists use a series of interconnected nodes, where each node contains both the data and a reference (or pointer) to the next node in the sequence.<br>
Each node in a linked list consists of two main components:
* Data: This is the value or information that you want to store in the linked list, such as an integer, string, object, etc.
* Next Pointer: This is a reference or pointer to the next node in the sequence. It establishes the linkage between nodes and defines the order of elements in the linked list. In an array, we have the index of that data instead.

The last node in a linked list typically has a "null" or "None" reference as its next pointer, indicating the end of the list.

Linked lists are useful in scenarios where dynamic resizing, frequent insertions and deletions, or efficient memory usage are important. They can be more flexible than arrays but might have slightly higher memory overhead due to the need for storing pointers.

We also have three different variations of linked list.
* Singly linked list: Each node contains data and a reference to the next node. It only allows traversal in one direction, from the head (start) to the tail (end).
* Doubly linked list: Each node contains data and references to both the next and previous nodes. This enables bidirectional traversal.
* Circular linked list: Similar to a singly or doubly linked list, but the last node's next pointer points back to the first node, creating a circular structure.

**Stacks**: A stack is a linear data structure in computer science that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. Think of it like a stack of plates – you can only add or remove plates from the top of the stack.

A stack has two primary operations:
* Push: This operation adds an element to the top of the stack.
* Pop: This operation removes and returns the element from the top of the stack.

The stack is commonly used for managing function calls and local variables in programming, as well as for solving problems involving backtracking, parsing expressions, and more. Stack is useful when the most recently seen elements matters (e.g., news feed) or when the order which you see the elements matters.

**Queue**: A queue is a linear data structure in computer science that follows the First-In-First-Out (FIFO) principle (opposite of stack!). In a queue, elements are added at the rear (also known as the "back" or "tail") and removed from the front (also known as the "front" or "head"). Think of it like a queue of people waiting in line – the first person to join the queue is the first one to be served.

A queue has two primary operations:
* Enqueue (Push): This operation adds an element to the rear of the queue.
* Dequeue (Pop): This operation removes and returns the element from the front of the queue.

In addition to enqueue and dequeue, there is often an operation called "Peek" or "Front," which allows you to view the element at the front of the queue without removing it.<br>
Queues are commonly used in scenarios where tasks need to be processed in the order they were added, such as task scheduling, breadth-first search algorithms, print spooling, and more.

**Deque**: A deque (short for "double-ended queue") is a versatile and linear data structure that allows you to add and remove elements from both ends with constant-time complexity. _It can be thought of as a hybrid between a stack and a queue_, providing the functionality of both while maintaining efficient operations at both ends.
<br>
A deque supports the following basic operations:
<br>
1. Append/Enqueue: Add an element to the back of the deque.
2. Appendleft: Add an element to the front of the deque.
3. Pop: Remove and return an element from the back of the deque.
4. Popleft: Remove and return an element from the front of the deque.
5. Peek/Peekleft: View the element at the back/front of the deque without removing it.
6. Size: Get the number of elements in the deque.

Deques are particularly useful in scenarios where you need to efficiently add or remove elements from both ends of a collection, such as implementing algorithms that require efficient FIFO and LIFO operations.

Another important feature of deque is that we can set a given max length to that:
```
from collections import deque
my_deque = deque(maxlen=100)
```
After reching the `maxlen`, when we append a number, it automatically removes the oldest number in the deque (i.e., automatically does `popleft`). It is very useful when we want a window-like history of our process (i.e., average accuracy of last 100 epochs in learning!)

**Priority queue**: allows you to retrieve elements based on their priority, rather than their insertion order or value. Elements with higher priority are typically dequeued or processed before elements with lower priority.
Priority queues are often used in scenarios where tasks or items need to be processed in a specific order based on some criteria. They have various applications, including: task scheduling, Dijkstra's algorithm (used to find the shortest path in a graph by selecting nodes with the lowest tentative distance),
Huffman coding (used in data compression algorithms to encode characters with higher frequencies using shorter codes), $A^*$ search algorithm (a heuristic-based search algorithm that uses a priority queue to explore potential paths in search space).

**Trees**: Trees and linked lists are built upon the concept of linked structures. Both trees and linked lists are hierarchical data structures. consists of nodes connected by edges, where each node contains a value (also called a key) and zero or more child nodes. The topmost node in a tree is called the root, and nodes with no children are called leaves.
1. Root: The topmost node of the tree, serving as the starting point for traversal.
2. Node: An element in the tree that contains a value and can have zero or more child nodes.
3. Parent: A node that has one or more child nodes.
4. Child: A node that is directly connected to and descended from another node (its parent).
5. Leaf: A node with no children, often found at the end of branches.
6. Depth: The distance between a node and the root. The root has a depth of 0.
7. Height: The length of the longest path from a node to a leaf. The height of the tree is the height of the root.

**Binary Search Tree (BST)**: is a type of binary tree with the added property that for each node:
* The value of the node's left child (if present) is less than the value of the node itself.
* The value of the node's right child (if present) is greater than the value of the node itself.

This property makes binary search trees particularly useful for efficient searching, i.e., $\rightarrow O(\log n)$, insertion, and deletion of elements. It ensures that the elements in the tree are ordered in a way that allows for quick access and manipulation.

An _unbalanced_ binary search tree (BST) is a type of binary search tree where the structure of the tree is skewed or imbalanced, meaning that the heights of the subtrees differ significantly. In an unbalanced BST, one subtree (either left or right) can have significantly more nodes than the other subtree, leading to inefficient and suboptimal search and insertion operations, i.e., $\approx O(n)$.

**Tree traversal**:
1. Depth First Search (DFS): is a graph traversal algorithm used to explore and search through a graph or tree data structure. It starts at a designated node (often called the "root" or "source" node) and explores as far as possible along each branch before backtracking.
DFS can be applied to both directed and undirected graphs, and it can be used for various purposes, including searching for a specific node, finding connected components, solving mazes, and more.
The basic idea behind DFS is to follow these steps:
    1. Start at the initial node and mark it as visited.
    2. Explore the first unvisited adjacent node of the current node (if any) by recursively applying DFS to it.
    3. Repeat step ii for each unvisited neighbor until there are no more unvisited neighbors.
    4. Backtrack to the previous node and explore any remaining unvisited neighbors.
    5. Continue this process until all nodes have been visited or the desired condition is met.
       
DFS is implemented using either recursion or an explicit stack data structure. The order in which nodes are visited in DFS depends on whether it's implemented using recursion or an iterative approach.

2. Breadth First Search (BFS): is a graph traversal algorithm used in computer science to explore and visit all the nodes (vertices) of a graph in a systematic and level-wise manner. It starts at a given source node and explores its neighbors before moving on to their neighbors and so on. BFS is commonly used to solve problems that involve finding the shortest path between nodes, exploring the connectivity of a graph, and more.
Here's how BFS works:
    1. Choose a starting node (often called the "source" node) from which to begin the traversal.
    2. Place the starting node in a queue.
    3. While the queue is not empty, do the following:
        * Dequeue a node from the front of the queue.
        * Process the node (visit it, perform any required operations).
        * Enqueue all unvisited neighbors of the dequeued node into the queue.
    
    iv.Repeat step 3 until the queue becomes empty.

BFS guarantees that nodes are visited level by level, meaning that all nodes at a certain distance (or "depth") from the source node are visited before moving on to nodes at a greater depth. This property makes BFS particularly useful for finding the shortest path between two nodes in an unweighted graph.

**Hashing**: is a process of converting input data of arbitrary size (such as text, numbers, files, or any other type of data) into a fixed-size value, often represented as a sequence of numbers and letters. The output of this process is called a hash value or hash code. Hashing is used in various computer science applications, including data storage, data retrieval, cryptography, and more.<br>
Hashing is used to create data structures like hash tables and hash maps, which allow efficient storage and retrieval of data based on a key. This enables faster look-up operations compared to linear search. Moreover, hashing is employed to verify the integrity of data. Even a small change in the data results in a vastly different hash value, making it useful for detecting tampering or errors.<br>
The downside of hashing is hash collisions, where different inputs produce the same hash value. Collisions can lead to data inconsistencies and negatively impact the performance of hash-based data structures. Moreover, selecting an appropriate hash function for a specific application is critical. An inadequate choice can lead to poor performance, security vulnerabilities, or unexpected behavior.<br>
A _hash table_, also known as a hash map, is a data structure used in computer science to store and manage key-value pairs for efficient data retrieval and storage. It is designed to provide fast access to values based on their associated keys. The main idea behind a hash table is to use the hash function to compute an index from the key, and then use that index to store or retrieve the value associated with the key. This allows for constant-time average-case complexity for insertion, deletion, and retrieval operations, making hash tables a valuable tool for tasks that involve frequent data access.

**Heaps**: A heap can be visualized as a binary tree where each node has a value and must satisfy the heap property, which can be defined in two ways:
* Max Heap Property: In a max heap, the value of each node is greater than or equal to the values of its children. The highest-valued element is at the root.
* Min Heap Property: In a min heap, the value of each node is less than or equal to the values of its children. The lowest-valued element is at the root.

Heaps are primarily used for maintaining a priority queue, which is a data structure that allows efficient access to the element with the highest (max heap) or lowest (min heap) priority. Priority queues are used in various applications, such as scheduling tasks, graph algorithms (like Dijkstra's algorithm), and implementing efficient sorting algorithms like heapsort.

## Sorting algorithms
**Bubble Sort**:
1. Start at the beginning of the list.
2. Compare the first two elements. If the first element is larger than the second, swap them.
3. Move to the next pair of adjacent elements and repeat step 2.
4. Continue this process for the entire list, repeatedly comparing and swapping adjacent elements until the largest (or smallest, depending on the desired order) element "bubbles" to the end of the list.
5. After completing one pass through the list, the largest (or smallest) element is in its correct position. Repeat the process for the remaining elements in the list, excluding the last one that is already in its correct position.
6. Continue this process until the entire list is sorted.

Bubble Sort has a time complexity of $O(n^2)$. Due to its poor time complexity, Bubble Sort is rarely used in practical applications for sorting large datasets


Merge Sort is a popular comparison-based sorting algorithm that follows the divide-and-conquer strategy to sort a list or array of elements. It works by recursively dividing the input list into smaller sublists, sorting each sublist, and then merging the sorted sublists to produce the final sorted output. Merge Sort has a stable sort property, meaning that equal elements maintain their relative order after sorting.

**Merge Sort**: can be summarized in the following steps:
1. Divide: Divide the unsorted list into two halves (sublists) by finding the middle point.
2. Conquer: Recursively sort each half of the sublist. This step involves repeatedly dividing each sublist into smaller sublists until they contain only one element, which is already sorted.
3. Merge: Merge the sorted sublists from the previous step to produce a single sorted list. This involves comparing elements from both sublists and placing them in the correct order.
4. Repeat: Repeat the divide, conquer, and merge steps until the entire list is sorted.

The key advantage of Merge Sort is its consistent time complexity. It guarantees a time complexity of $O(n \log n)$ in the worst, best, and average cases.<br>
However, Merge Sort does require additional memory to hold the sublists during the merging process. This additional memory consumption makes it less space-efficient compared to some other _in-place_ sorting algorithms.

Quick Sort is a widely used comparison-based sorting algorithm that follows the divide-and-conquer strategy to efficiently sort a list or array of elements. It works by selecting a "pivot" element from the input list, partitioning the list into two sublists – one containing elements less than the pivot and another containing elements greater than the pivot – and then recursively sorting these sublists. Quick Sort is known for its high performance and is often used in practice for sorting large datasets.

**Quick Sort**: can be summarized in the following steps:

1. Pivot Selection: Choose a pivot element from the list. The pivot can be chosen in various ways, such as selecting the first element, the last element, a random element, or using a median-of-three approach.
2. Partitioning: Rearrange the elements in the list so that all elements less than the pivot are on the left side, and all elements greater than the pivot are on the right side. The pivot itself will be in its correct sorted position.
3. Recursion: Recursively apply Quick Sort to the left and right sublists created during the partitioning step.
4. Base Case: The base case of the recursion is when a sublist has only one or zero elements, which is already considered sorted.
5. Combine: As the recursion unwinds, the sublists will be merged to produce the final sorted list.

Quick Sort is known for its efficient average-case time complexity of $O(n \log n)$. In practice, Quick Sort often outperforms other sorting algorithms like Merge Sort and Heap Sort, especially for small to medium-sized datasets. Its efficiency is due to its ability to partition the list and sort it in place, reducing the amount of memory needed for temporary storage.

However, it's important to note that Quick Sort's worst-case time complexity is $O(n^2)$, which occurs when the pivot selection and partitioning steps consistently result in unbalanced sublists. To mitigate this issue, various optimizations and pivot selection strategies (like the median-of-three approach) are employed to improve the algorithm's performance and avoid worst-case scenarios.

**Graph**: 
A graph is a fundamental data structure in computer science used to represent a collection of objects (nodes or vertices) and the connections between them (edges). An example for that is a data base for websites and there likes to eachother. Graphs are widely used to model and solve problems involving relationships, connections, and networks.<br>
Graphs can also have various applications:
* Social Networks: Modeling connections between individuals in social media networks.
* Transportation Networks: Representing routes, roads, and transportation systems.
* Web Pages and Hyperlinks: Modeling the structure of the World Wide Web.
* Circuit Design: Representing electronic circuits and their components.
* Recommendation Systems: Modeling user preferences and item relationships.
* Data Processing: Representing data dependencies in workflows or processing pipelines.

The components of a graph include:

1. Nodes (Vertices): Nodes represent individual entities or objects in the graph. Each node can have associated attributes or data.
2. Edges: Edges represent connections or relationships between nodes. Edges can be directed (pointing from one node to another) or undirected (bidirectional). In addition, edges can have weights or labels that represent additional information, such as distances or strengths of connections.

Graphs can be classified into different types based on their characteristics:
1. Directed Graph (Digraph): A graph where each edge has a specific direction from one node to another. The relationship between nodes is asymmetric.
2. Undirected Graph: A graph where edges do not have a specific direction. The relationship between nodes is symmetric.
3. Weighted Graph: A graph where edges have associated weights or values that represent additional information about the connections.
4. Unweighted Graph: A graph where all edges are considered to have equal weight, and no additional values are associated with the connections.
5. Cyclic Graph: A graph that contains at least one cycle, which is a sequence of nodes that forms a closed loop.
6. Acyclic Graph: A graph that does not contain any cycles.

**DAG**: Directed Acyclic Graph. It is a type of graph data structure that consists of nodes (vertices) and directed edges, where each edge has a specific direction and there are no cycles in the graph.

**Knapsack problem**: is a well-known optimization problem in computer science and mathematics. It is a classic example of a combinatorial optimization problem, where the goal is to select a subset of items from a given set, subject to certain constraints, in order to maximize a specified value.

The problem is typically formulated as follows:

You are given a set of items, each with a weight and a value. You have a knapsack with a limited weight capacity. The goal is to select a subset of items to include in the knapsack such that the total weight does not exceed the capacity of the knapsack, and the total value of the selected items is maximized.

There are two main variants of the knapsack problem:

1. 0-1 Knapsack Problem: In this variant, you can either select an item (weight and value) or not select it (binary decision) for inclusion in the knapsack. In other words, you cannot take fractional amounts of items.
2. Fractional Knapsack Problem: In this variant, you can take fractional amounts of items, which means you can decide to include a fraction of an item's weight and value in the knapsack.

The knapsack problem is NP-hard, which means that there is no known efficient algorithm that can solve it for all possible inputs in polynomial time (i.e., $O(n^2)$ or $O(n)$). However, it can be solved using various optimization techniques, including dynamic programming, greedy algorithms, and branch and bound methods.

One dumb method to solve 0-1 knapsack problem is _Brute Force_ Solution which considers all possible combinations which has the complexity of $O(2^n)$ (polynomial complexity) which $n$ is the total number of objects.


## Dynamic Programming
**Dynamic programming** is a method used in computer science and mathematics to solve problems by breaking them down into smaller subproblems and solving each subproblem only once. The solutions to the subproblems are stored in a table or memoization array, so that they can be reused when needed to solve larger subproblems or the original problem.

It can solve problems in *polynomial time* $O(n^c)$ which a naive approach solves them in *exponential time* $O(c^n)$. As a result, dynamic programming is less or more an optimization technique which optimise the solution. Sometimes we can add some heuristics to reduce the complexity to a *linear* one $O(n)$.

Problems that can be solved by DP should have these properties:
1. ***Optimal substructure:*** The optimal solution to the problem can be found by combining the optimal solutions to its subproblems. In other words, the optimal solution to the problem can be computed by using the optimal solutions to the subproblems.
2. ***Overlapping subproblems:***  The problem can be broken down into smaller subproblems, and the solutions to these subproblems are reused to solve the larger problem. These subproblems must overlap, meaning that the same subproblem is solved multiple times.
3. ***Subproblems can be solved independently:***  The subproblems should be independent of each other, meaning that the solution to one subproblem does not affect the solution to another subproblem.

DP problems fall into two main group:
1. ***Combinatoric problems*** that want to **count** something:
    - How many steps needed to get from point A to B
    - How many ways needed to complete ...
2. ***Optimization problems*** that want the minimum number of something:
    - What us the minimum number of steps needed to get from point A to B
    - What is the minimum number of ways needed to complete ...
    - What is the mximum profit of buying or selling a stock

The data structure for the dynamic programming buffer can be a _list_ or _dictionary_. The choice depends on several factors, including the specific problem, the nature of the data, and the operations performed on the buffer. List is more memory efficient, faster to search, and simpler, especially when the state space can be represented using sequential indices. Dictionary, on the other hand, is more flexible in associating values with specific keys (states), which can be useful when working with complex and un-ordered state representations (e.g., Q-learning).

There are two main approaches to dynamic programming:

1. Top-Down Approach (Memoization): In this approach, the problem is solved recursively by breaking it down into smaller subproblems. The solutions to these subproblems are stored in a memoization table to avoid redundant calculations.
2. Bottom-Up Approach (Tabulation): In this approach, the problem is solved iteratively by building up the solution from the bottom (i.e., the smallest subproblems) to the top (i.e., the original problem). The solutions to subproblems are stored in a table as they are computed.


