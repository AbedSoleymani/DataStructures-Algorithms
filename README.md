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
<br>As the input to an algorithm increases, the time required to run the algorithm may also increase.
<br>
![Alt text](../../../../borna/Downloads/00-all-comparison-computational-complexity-2.svg)
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
