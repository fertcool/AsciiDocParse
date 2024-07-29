# The class of the Parser object that the user interacts with directly.
# It has methods that return iterators for the selected type of asciidoc document objects

import os
import shutil
import subprocess
import tempfile

from adparser.AST.Blocks import BlockIterator
from adparser.AST.Scaners import HTMLScaner
from adparser.Visitors import *


def print_tree(node, level=0):
    indent = "    " * level
    print(f"{indent}{node.__class__.__name__}  {node.section}  {node.styles}")

    for child in node._children:
        print_tree(child, level + 1)


class Parser:

    def __init__(self, file):

        # discriptor or str
        if hasattr(file, 'read'):
            path = file.name
        else:
            path = file

        if shutil.which("asciidoctor") is None:
            print("asciidoctor not found in PATH")
            exit(1)

        # using OS temp dir
        temp_dir = tempfile.gettempdir()
        subprocess.run('asciidoctor ' + path + ' -D ' + temp_dir, shell=True)

        # forming the path to the html file that was automatically created by asciidoctor
        file_name = os.path.splitext(os.path.basename(path))[0]
        new_path = os.path.join(temp_dir, f"{file_name}.html")

        # read html
        with open(new_path) as htmlfile:
            self.htmlcontent = htmlfile.read()

        # delete html file
        os.remove(new_path)

        scaner = HTMLScaner()
        self.astree = scaner.build_AST(self.htmlcontent)
        # print_tree(self.astree)

    """the functions create a visitor, dfs with this visitor returns an iterator to the blocks"""

    def text_lines(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []
        visitor = TextLineSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)


    def links(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = LinkSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def paragraphs(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []
        visitor = ParagraphSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def headings(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = HeadingSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def lists(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = ListSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def source_blocks(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = SourceSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def tables(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = TableSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)


    def audios(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = AudioSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def images(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = ImageSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def videos(self, style=None, section=None) -> BlockIterator:
        if style is None:
            style = []
        if section is None:
            section = []

        visitor = VideoSelector(section, style)
        self.astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

