class SectionIterator:
    def __init__(self, collection):
        self.idx = 0
        self.collection = collection

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.collection):
            value = self.collection[self.idx]
            self.idx += 1
            return value
        else:
            raise StopIteration
