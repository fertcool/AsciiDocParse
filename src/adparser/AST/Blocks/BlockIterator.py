# iterator over the blocks of the tree

from adparser.AST.Blocks import Block


class BlockIterator:

    def __init__(self, blocklist: list[Block]):
        self.blocklist = blocklist

        self.current = 0
        self.end = len(self.blocklist) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.blocklist[self.current]
            self.current += 1
            return value
        else:
            raise StopIteration()
