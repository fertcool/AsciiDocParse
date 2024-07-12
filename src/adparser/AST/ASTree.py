# AST for AsciiDoc document

from src.adparser.AST.Blocks.Blocks import Block
from src.adparser.AST.Blocks.BlockIterator import BlockIterator
from src.adparser.Visitors import Visitor
from src.adparser.AST.Scaners.Scaner import Scaner


class ASTree:

    def __init__(self, sourcetext: str):
        """scaner = Scaner()
        self.head: Block = scaner.build_AST(sourcetext)"""

    @staticmethod
    def _add_sub_element(self, parent: Block, newchild: Block):
        parent.children.append(newchild)

    def dfs(self, visitor: Visitor) -> BlockIterator:
        pass
