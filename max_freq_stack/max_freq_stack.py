'''max_freq_stack'''
from collections import deque


class FreqStack:

    def __init__(self):
        self.val_freq = deque()

    def push(self, val: int) -> None:
        freq = 0
        for v, _ in self.val_freq:
            if v == val:
                freq += 1
        self.val_freq.append((val, freq + 1))

    def pop(self) -> int:
        max_freq = max(freq for _, freq in self.val_freq)
        for i in range(len(self.val_freq) - 1, -1, -1):
            if self.val_freq[i][1] == max_freq:
                val = self.val_freq[i][0]
                del self.val_freq[i]
                return val
