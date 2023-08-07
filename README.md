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
<br>
<br>
<br>
