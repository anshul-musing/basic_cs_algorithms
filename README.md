# Basic computer science algorithms

Python implementation of basic computer science algorithms for the following data structures:

## Stacks
* We test pushing, popping, and checking if a stack is empty
* Stack is implemented as a python list
* It's not the best implementation as we'll show that the stack will be empty yet it will be occupying memory with the previously inserted elements

## Queues
* We test enqueue, dequeue, and checking if a queue is empty
* Queue is implemented as a python list
* It's not the best implementation as we'll show that the queue will be empty yet it will be occupying memory with the previously inserted elements

## Linked List
* We test insert, delete, and search functions
* Each node of the linked list is an object of the Node class, which has a value and the previous and the next links

## Binary search tree
* We test 
     * insert in a tree
     * finding minimum, maximum in a tree
     * displaying a tree using in-order, pre-order, post-order walk, and level-order walk
     * deleting a node in tree using transplant function
     * calculating height of a tree
     * calculating number of nodes in the tree
     * finding the second largest element
* Each node of the binary search tree is an object of the Node class, which has a value and the left and the right links

## Graphs
* We test 
     * breadth first search
     * depth first search
     * minimum spanning tree using Prim's algorithm
     * shortest distance using Dijkstra's algorithm
* Graph's vertices are specified as a list
* Graph's edges are represented as a dictionary

## Sorting
* We test 
     * bubble sort
     * selection sort
     * insertion sort
     * merge sort
     * quick sort
     
## Max heap
* The heap class takes a balanced binary tree as an input and converts it into a max heap
* We test
     * creating a balanced tree from an unsorted array
     * building a max heap
     * heapify operation
* Each node of the max heap is an object of the Node class, which has a value and the left and the right links

## Trie tree
* We test insert, search, and start-with functions
* Each node of the trie tree is an object of the TrieNode class, which has
    * children hash that stores characters as hash keys
    * endOfWord boolean indicator
