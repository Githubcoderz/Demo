class Even:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        self.count += 1
        return result

even_iter = Even(10)
for even in even_iter:
    print(even, end=" ")