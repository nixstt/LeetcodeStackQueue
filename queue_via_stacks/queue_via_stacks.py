'''queue_via_stacks'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        rem = self.top
        self.top = self.top.next
        return rem.data

    def peek(self):
        return self.top.data


class MyQueue:

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def push(self, x: int) -> None:
        self.inbox.push(x)

    def pop(self) -> int:
        self.outbox.pop()

    def peek(self) -> int:
        return self.outbox.peek()

    def empty(self) -> bool:
        return self.outbox.is_empty()
