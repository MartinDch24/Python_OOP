class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.current
        self.current += 1
        if temp <= self.end:
            return temp
        raise StopIteration
