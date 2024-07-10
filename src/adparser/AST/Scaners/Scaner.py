# base Scaner class
# each implementation performs the construction of a tree in outs own way
# the constructed tree may be different for each implementation

import abc
from src.adparser.AST.Blocks import Blocks


class Scaner(abc.ABC):

    @abc.abstractmethod
    def build_AST(self, text: str) -> Block:  # Block = head of AST
        pass