'''max_freq_stack'''
from collections import deque


class FreqStack:

    def __init__(self):
        self.val_freq = {}
        self.freq_to_stack = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.val_freq.get(val, 0) + 1
        self.val_freq[val] = freq

        if freq > self.max_freq:
            self.max_freq = freq

        if freq not in self.freq_to_stack:
            self.freq_to_stack[freq] = deque()
        self.freq_to_stack[freq].append(val)

    def pop(self) -> int:
        val = self.freq_to_stack[self.max_freq].pop()

        if not self.freq_to_stack[self.max_freq]:
            del self.freq_to_stack[self.max_freq]
            self.max_freq -= 1

        self.val_freq[val] -= 1

        return val
