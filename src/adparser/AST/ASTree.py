# AST for AsciiDoc document

from src.adparser.AST.Blocks.Blocks import Block, RootBlock
from src.adparser.AST.Blocks.BlockIterator import BlockIterator
from src.adparser.Visitors import Visitor


class ASTree:

    def __init__(self, head: RootBlock):
        self.head = head

    @staticmethod
    def add_sub_element(parent: Block, newchild: Block):
        parent._children.append(newchild)

    def dfs(self, visitor: Visitor) -> BlockIterator:
        stack = [self.head]

        while stack:
            node = stack.pop()

            node.accept(visitor)

            for child in reversed(node._children):
                stack.append(child)

