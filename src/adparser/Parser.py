
from src.adparser.AST.Blocks.BlockIterator import BlockIterator
from src.adparser.AST.Scaners.HTMLScaner import HTMLScaner


class Parser:

    def __init__(self, file, link_opt='hide_url'):

        # discriptor or str
        if hasattr(file, 'read'):
            self.content = file.read()
        else:
            self.content = file

        self.link_opt = link_opt

        scaner = HTMLScaner()
        self.astree = scaner.build_AST(self.content)
        pass

    """the functions create a visitor, dfs with this visitor returns an iterator to the blocks"""

    def text_lines(self, style=None, section=None) -> BlockIterator:
        pass

    def links(self, section=None) -> BlockIterator:
        pass

    def paragraphs(self, style=None, section=None) -> BlockIterator:
        pass

    def headings(self, section=None) -> BlockIterator:
        pass

    def lists(self, section=None) -> BlockIterator:
        pass

    def source_blocks(self, style=None, section=None) -> BlockIterator:
        pass

    def tables(self, section=None) -> BlockIterator:
        pass

    def admonition_blocks(self, style=None, section=None) -> BlockIterator:
        pass

    def audios(self, section=None) -> BlockIterator:
        pass

    def images(self, section=None) -> BlockIterator:
        pass

    def video(self, section=None) -> BlockIterator:
        pass

