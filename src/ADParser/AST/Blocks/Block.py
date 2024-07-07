# base block class for AST
import abc


class Block(abc.ABC):
    from src.ADParser.Visitors import Visitor

    @abc.abstractmethod
    def accept(self, visitor: Visitor):
        pass
