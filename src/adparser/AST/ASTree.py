# AST for AsciiDoc document

from src.adparser.AST.Blocks import Blocks
from src.adparser.Visitors import Visitor
import src.adparser.AST.Scaners


class ASTree:

    def __init__(self):
        pass
        # scaner = Scaner()
        # self.head: Block = scaner.build_AST()

    def dfs(self, visitor: Visitor):
        pass
