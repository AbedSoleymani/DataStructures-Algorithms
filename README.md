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

<br>wef
<br>
<br>
