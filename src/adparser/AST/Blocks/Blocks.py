# base block class for AST
import abc


class Block(abc.ABC):
    from src.adparser.Visitors import Visitor

    _parent = None
    _children: list = None  # list of children blocks

    data = None
    section: str = None

    @abc.abstractmethod
    def accept(self, visitor: Visitor):
        pass

    def get_near_up(self, element: str):
        pass

    def get_near_down(self, element: str):
        pass


"""blocks classes description"""
