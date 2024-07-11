
from src.adparser.AST.Blocks.BlockIterator import BlockIterator
from src.adparser.AST.ASTree import ASTree


class Parser:

    def __init__(self, file, link_opt='hide_url'):

        # discriptor or str
        if hasattr(file, 'read'):
            self.content = file.read()
        else:
            self.content = file

        self.link_opt = link_opt

        self.astree = ASTree(self.content)

    """the functions create a visitor, dfs with this visitor returns an iterator to the blocks"""

    def text_lines(self, style=None) -> BlockIterator:
        pass

    def links(self) -> BlockIterator:
        pass

    def paragraphs(self, style=None) -> BlockIterator:
        pass

    def sections(self) -> BlockIterator:
        pass

    def headings(self) -> BlockIterator:
        pass

    def lists(self) -> BlockIterator:
        pass

    def source_blocks(self, style=None) -> BlockIterator:
        pass

    def tables(self) -> BlockIterator:
        pass

    def admonition_blocks(self, style=None) -> BlockIterator:
        pass

    def audios(self) -> BlockIterator:
        pass

    def images(self) -> BlockIterator:
        pass

    def video(self) -> BlockIterator:
        pass

