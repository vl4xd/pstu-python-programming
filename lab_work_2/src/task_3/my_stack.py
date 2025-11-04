from typing import Self


class Node:


    def __init__(self, value: object) -> None:
        self._prev: Self = None
        self._value = value


    def __repr__(self):
        return f"Node(prev={self._prev}, value={self._value})"


class MyStack:


    def __init__(self):
        self._head: Node = None


    def push(self, item: object) -> None:

        new_node = Node(item)

        if self._head is None:
            self._head = new_node
            return

        new_node._prev = self._head
        self._head = new_node

        return


    def pop(self) -> object:

        if self._head is None:
            raise IndexError("pop from empty queue")

        value = self._head._value

        if self._head._prev:
            self._head = self._head._prev
        else:
            self._head = None

        return value


    def peek(self) -> object:

        if self._head is None:
            raise IndexError("peek from empty queue")

        return self._head._value

    def __str__(self) -> str:

        string = "("

        if self._head is None:
            return string + ")"

        cur_node = self._head
        while True:
            string += f"{cur_node._value}"
            if cur_node._prev is None:
                break
            string += " ← "
            cur_node = cur_node._prev

        return string + ")"


stack = MyStack()
print(stack)
stack.push(1)
print(stack)
stack.push(2)
print(stack)
stack.push(3)
print(stack)
_ = stack.pop()
print(stack)
stack.push(4)
print(stack)
_ = stack.pop()
print(stack)
_ = stack.pop()
print(stack)
_ = stack.pop()
print(stack)