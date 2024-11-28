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
            if not os.path.exists(path):
                raise FileNotFoundError("adoc file not exist!")

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
        with open(new_path, encoding="utf-8") as htmlfile:
            self._htmlcontent = htmlfile.read()

        # delete html file
        os.remove(new_path)

        scaner = HTMLScaner()
        self._astree = scaner.build_AST(self._htmlcontent)
        # print_tree(self.astree)

    """the functions create a visitor, dfs with this visitor returns an iterator to the blocks"""

    def _select_and_parse(self, style, section, selectorclass):
        if style is None:
            style = []
        if section is None:
            section = []
        visitor = selectorclass(section, style)
        self._astree.dfs(visitor)
        return BlockIterator(visitor.select_list)

    def text_lines(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, TextLineSelector)

    def links(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, LinkSelector)

    def paragraphs(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, ParagraphSelector)

    def headings(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, HeadingSelector)

    def lists(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, ListSelector)

    def source_blocks(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, SourceSelector)

    def tables(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, TableSelector)

    def audios(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, AudioSelector)

    def images(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, ImageSelector)

    def videos(self, style=None, section=None) -> BlockIterator:
        return self._select_and_parse(style, section, VideoSelector)

