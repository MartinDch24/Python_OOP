class reverse_iter:

    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.end_index = len(self.iter_obj)
        self.start_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.end_index -= 1
        if self.start_index <= self.end_index:
            return self.iter_obj[self.end_index]
        raise StopIteration
