'''stack_via_queues'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.top = None
        self.back = None

    def push(self, data):
        new = Node(data)
        if self.empty():
            self.top = self.back = new
        else:
            self.back.next = new
            self.back = new

    def pop(self):
        rem = self.top
        self.top = self.top.next
        if not self.top:
            self.back = None
        return rem.data

    def peek(self) -> int:
        return self.top.data

    def empty(self) -> bool:
        return self.top is None


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x) -> None:
        self.q2.push(x)
        while not self.q1.empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.empty()
