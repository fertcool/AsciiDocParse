# AST for AsciiDoc document

from src.ADParser.AST.Blocks import Block
from src.ADParser.Visitors import Visitor
import src.ADParser.AST.Scaners


class ASTree:

    def __init__(self):
        pass
        # scaner = Scaner()
        # self.head: Block = scaner.build_AST()

    def dfs(self, visitor: Visitor):
        pass
