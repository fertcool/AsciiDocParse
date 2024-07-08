# base Visitor class
# each implementation processes each node of the AST in its own way
# Visitor gives desired result of parsing the AsciiDoc document

import abc


class Visitor(abc.ABC):
    pass
    """ abc methods for all AST implemented blocks
    
    @abc.abstractmethod
    def visit_some_block1():
        pass 
    @abc.abstractmethod
    def visit_some_block2():
        pass 
    ... 
    ... 
        """