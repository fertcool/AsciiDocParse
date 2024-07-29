from adparser.Visitors.Visitor import *


class Selector(Visitor):
    def __init__(self, sectors, styles):
        self.select_list = []
        self.sectors = sectors
        self.styles = styles

    def _add(self, treeblock: Block):
        if set(self.sectors).issubset(set(treeblock.section)) \
                and set(self.styles).issubset(set(treeblock.styles)):
            self.select_list.append(treeblock)


class TextLineSelector(Selector):

    def visit_text_line(self, text_line: TextLine):
        self._add(text_line)


class LinkSelector(Selector):

    def visit_link(self, link: Link):
        self._add(link)


class ParagraphSelector(Selector):

    def visit_paragraph(self, paragraph: Paragraph):
        self._add(paragraph)


class HeadingSelector(Selector):

    def visit_heading(self, heading: Heading):
        self._add(heading)


class ListSelector(Selector):

    def visit_list(self, list_block: List):
        self._add(list_block)


class SourceSelector(Selector):

    def visit_source(self, source: SourceBlock):
        self._add(source)


class TableSelector(Selector):

    def visit_table(self, table: Table):
        self._add(table)


class AudioSelector(Selector):

    def visit_audio(self, audio: Audio):
        self._add(audio)


class VideoSelector(Selector):

    def visit_video(self, video: Video):
        self._add(video)


class ImageSelector(Selector):

    def visit_image(self, image: Image):
        self._add(image)
