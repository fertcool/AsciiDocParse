# base Visitor class
# each implementation processes each node of the AST in its own way
# Visitor gives desired result of parsing the AsciiDoc document
from src.adparser.AST.Blocks.Blocks import *


class Visitor:

    def visit_text_line(self, text_line: TextLine):
        pass

    def visit_link(self, link: Link):
        pass

    def visit_paragraph(self, paragraph: Paragraph):
        pass

    def visit_heading(self, heading: Heading):
        pass

    def visit_list(self, list_block: List):
        pass

    def visit_source(self, source: SourceBlock):
        pass

    def visit_table(self, table: Table):
        pass

    def visit_audio(self, audio: Audio):
        pass

    def visit_video(self, video: Video):
        pass

    def visit_image(self, image: Image):
        pass

