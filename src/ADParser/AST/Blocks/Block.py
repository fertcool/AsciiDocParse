# base block class for AST
import abc


class Block(abc.ABC):
    from src.ADParser.Visitors import Visitor

    children: list = None  # list of children blocks

    @abc.abstractmethod
    def accept(self, visitor: Visitor):
        pass


