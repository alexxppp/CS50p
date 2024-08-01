class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n + self._size > self._capacity:
            raise ValueError("Not enough capacity in the jar")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
