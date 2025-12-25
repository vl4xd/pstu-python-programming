from typing import Self


class Node:


    def __init__(self, value: object) -> None:
        self._prev: Self = None
        self._value = value
        self._next: Self = None


    def __repr__(self):
        return f"Node(prev={self._prev}, value={self._value}, next={self._next})"


class MyQueue:


    def __init__(self) -> None:
        self._head: Node = None
        self._tail: Node = None


    def enqueue(self, item: object) -> None:

        new_node = Node(item)

        if self._head is None and self._tail is None:
            self._head = new_node
            self._tail = new_node
            return

        new_node._next, self._tail._prev = self._tail, new_node
        self._tail = new_node

        return


    def dequeue(self) -> object:

        if self._head is None:
            raise IndexError("dequeue from empty queue")

        value = self._head._value

        if self._head._prev:
            self._head._prev._next = None
            self._head = self._head._prev
        else:
            self._head, self._tail = None, None
        return value


    def peek(self) -> object:

        if self._head is None:
            raise IndexError("peek from empty queue")

        return self._head._value


    def __str__(self) -> str:

        string = "("

        if self._tail is None:
            return string + ")"

        cur_node = self._tail
        while True:
            string += f"{cur_node._value}"
            if cur_node._next is None:
                break
            string += " → "
            cur_node = cur_node._next

        return string + ")"


queue = MyQueue()
print(queue)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
_ = queue.dequeue()
print(queue)
_ = queue.dequeue()
print(queue)
_ = queue.dequeue()
print(queue)
queue.enqueue(4)
print(queue)
queue.enqueue(5)
print(queue)
_ = queue.dequeue()
print(queue)
queue.enqueue(6)
print(queue)