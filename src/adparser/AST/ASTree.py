# AST for AsciiDoc document

from src.adparser.AST.Blocks.Blocks import Block
from src.adparser.AST.Blocks.BlockIterator import BlockIterator
from src.adparser.Visitors import Visitor



class ASTree:

    def __init__(self, head: Block):
        self.head = head

    @staticmethod
    def add_sub_element(parent: Block, newchild: Block):
        parent.children.append(newchild)

    def dfs(self, visitor: Visitor) -> BlockIterator:
        pass
