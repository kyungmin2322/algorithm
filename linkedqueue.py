# -*- coding: utf-8 -*-
"""linkedqueue

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J4_ohQDt5RdomYXgjjMOe05prJFuxrZ7
"""

from circularlinkedlist import CircularLinkedList

class LinkedQueue :
    def __init__(self) :
        self.__queue = CircularLinkedList()

    def enqueue(self, x) :
        self.__queue.append(x)

    def dequeue(self) :
        return self.__queue.pop(0)

    def fron(self) :
        return self.__queue.ger(0)

    def isEmpty(self) -> bool :
        return self.__queue.isEmpty()

    def dequeueAll(self) :
        self.__queue.clear()

    def printQueue(self) :
        print("Queue from front : ", end = ' ')
        for i in range(self.__queue.size()) :
            print(self.__queue.get(i), end = ' ')
        print()