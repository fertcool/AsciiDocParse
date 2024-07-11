# base block class for AST
import abc
from dataclasses import dataclass


class Block(abc.ABC):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent):
        self.section = section
        self.data = data
        self._parent = parent
        self._children: list = None  # list of children blocks


    @abc.abstractmethod
    def accept(self, visitor: Visitor):
        pass

    def get_near_up(self, element: str):
        pass

    def get_near_down(self, element: str):
        pass


"""blocks classes description"""


class TextLine(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style=None):
        super().__init__(data, section, parent)
        self.style = style

    def accept(self, visitor: Visitor):
        pass


class Link(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, attribute):
        super().__init__(data, section, parent)
        self.attribute = attribute

    def accept(self, visitor: Visitor):
        pass


class Paragraph(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style=None):
        super().__init__(data, section, parent)
        self.style = style

    def accept(self, visitor: Visitor):
        pass


class Section(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent):
        super().__init__(data, section, parent)

    def accept(self, visitor: Visitor):
        pass


class Heading(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent):
        super().__init__(data, section, parent)

    def accept(self, visitor: Visitor):
        pass


class List(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent):
        super().__init__(data, section, parent)

    def accept(self, visitor: Visitor):
        pass


class SourceBlock(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style=None):
        super().__init__(data, section, parent)
        self.style = style

    def accept(self, visitor: Visitor):
        pass


@dataclass
class MatDict:
    matrix: list
    dict: dict


class Table(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, matrix, diction, section, parent):
        super().__init__(None, section, parent)
        self.data = MatDict(matrix, diction)

    def accept(self, visitor: Visitor):
        pass


class Admonition(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style=None):
        super().__init__(data, section, parent)
        self.style = style

    def accept(self, visitor: Visitor):
        pass


class Audio(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent):
        super().__init__(data, section, parent)

    def accept(self, visitor: Visitor):
        pass


class Image(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent):
        super().__init__(data, section, parent)

    def accept(self, visitor: Visitor):
        pass

