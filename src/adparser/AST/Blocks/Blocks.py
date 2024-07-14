# base block class for AST
import abc
from dataclasses import dataclass


class Block(abc.ABC):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style):
        if not section:
            self.section = []
        else:
            self.section = section

        if not style:
            self.styles = []
        else:
            self.styles = style

        self.data = data
        self._parent = parent



        self.children: list = []  # list of children blocks

    def add_style(self, style):
        if style:
            self.styles.append(style)

    @abc.abstractmethod
    def accept(self, visitor: Visitor):
        pass

    def get_near_up(self, element: str, style=None):
        pass

    def get_near_down(self, element: str, style=None):
        pass


"""blocks classes description"""


class RootBlock(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, section=None):
        super().__init__(None, section, None, None)

    def accept(self, visitor: Visitor):
        pass


class DelimeterBlock(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, section, parent, style):
        super().__init__(None, section, parent, style)

    def accept(self, visitor: Visitor):
        pass


class TextLine(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style=None):
        super().__init__(data, section, parent, style)

    def accept(self, visitor: Visitor):
        pass


class Link(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style, attribute):
        super().__init__(data, section, parent, style)
        self.attribute = attribute

    def accept(self, visitor: Visitor):
        pass


class Paragraph(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style=None):
        super().__init__(data, section, parent, style)

    def accept(self, visitor: Visitor):
        pass


class Section(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, section, parent):
        super().__init__(None, section, parent, None)

    def accept(self, visitor: Visitor):
        pass


class Heading(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style=None):
        super().__init__(data, section, parent, style)

    def accept(self, visitor: Visitor):
        pass


class List(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style):
        super().__init__(data, section, parent, style)

    def accept(self, visitor: Visitor):
        pass


class SourceBlock(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style):
        super().__init__(data, section, parent, style)
        self.style = style

    def accept(self, visitor: Visitor):
        pass


@dataclass
class MatDict:
    matrix: list
    dict: dict


class Table(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, matrix, diction, section, parent, style=None):
        super().__init__(None, section, parent, style)
        self.data = MatDict(matrix, diction)

    def accept(self, visitor: Visitor):
        pass


class Admonition(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, section, parent, style):
        super().__init__(None, section, parent, style)

    def accept(self, visitor: Visitor):
        pass


class Audio(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style):
        super().__init__(data, section, parent, style)

    def accept(self, visitor: Visitor):
        pass


class Image(Block):
    from src.adparser.Visitors import Visitor

    def __init__(self, data, section, parent, style):
        super().__init__(data, section, parent, style)

    def accept(self, visitor: Visitor):
        pass

