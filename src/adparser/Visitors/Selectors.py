from adparser.Visitors.Visitor import *


class Selector(Visitor):
    def __init__(self, sectors, styles):
        self.select_list = []
        self.sectors = sectors
        self.styles = styles

    def check_subsets(self, sectors, styles):
        return set(self.sectors).issubset(set(sectors)) \
                and set(self.styles).issubset(set(styles))


class TextLineSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_text_line(self, text_line: TextLine):
        if self.check_subsets(text_line.section, text_line.styles):
            self.select_list.append(text_line)


class LinkSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_link(self, link: Link):
        if self.check_subsets(link.section, link.styles):
            self.select_list.append(link)


class ParagraphSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_paragraph(self, paragraph: Paragraph):
        if self.check_subsets(paragraph.section, paragraph.styles):
            self.select_list.append(paragraph)


class HeadingSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_heading(self, heading: Heading):
        if self.check_subsets(heading.section, heading.styles):
            self.select_list.append(heading)


class ListSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_list(self, list_block: List):
        if self.check_subsets(list_block.section, list_block.styles):
            self.select_list.append(list_block)


class SourceSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_source(self, source: SourceBlock):
        if self.check_subsets(source.section, source.styles):
            self.select_list.append(source)


class TableSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_table(self, table: Table):
        if self.check_subsets(table.section, table.styles):
            self.select_list.append(table)


class AudioSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_audio(self, audio: Audio):
        if self.check_subsets(audio.section, audio.styles):
            self.select_list.append(audio)


class VideoSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_video(self, video: Video):
        if self.check_subsets(video.section, video.styles):
            self.select_list.append(video)


class ImageSelector(Selector):
    def __init__(self, sectors, styles):
        super().__init__(sectors, styles)

    def visit_image(self, image: Image):
        if self.check_subsets(image.section, image.styles):
            self.select_list.append(image)
