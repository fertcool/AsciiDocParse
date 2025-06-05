import pytest_check as check
from src.adparser.AST.Blocks import *


class TestAST:

    def test_hiearchy(self, section_list):
        slist = section_list
        slist_names = [tuple(x.section) for x in slist]
        check.equal(slist_names, [('AsciiDoc full syntax',),
                                  ('AsciiDoc full syntax', 'Paragraphs'),
                                  ('AsciiDoc full syntax', 'Paragraphs', 'Literal'),
                                  ('AsciiDoc full syntax', 'Paragraphs', 'Sidebar'),
                                  ('AsciiDoc full syntax', 'Paragraphs', 'Example & nested Listing'),
                                  ('AsciiDoc full syntax', 'Paragraphs', 'Quote'),
                                  ('AsciiDoc full syntax', 'Paragraphs', 'Admonition'),
                                  ('AsciiDoc full syntax', 'Formatted Text'),
                                  ('AsciiDoc full syntax', 'Lists'),
                                  ('AsciiDoc full syntax', 'Links'),
                                  ('AsciiDoc full syntax', 'Images'),
                                  ('AsciiDoc full syntax', 'Videos'),
                                  ('AsciiDoc full syntax', 'Audios'),
                                  ('AsciiDoc full syntax', 'Source Code'),
                                  ('AsciiDoc full syntax', 'Tables')])

    def test_paragraphs(self, section_dict):
        # --------------------------------- simple --------------------------------- #
        par_sect = section_dict[('AsciiDoc full syntax', 'Paragraphs')]
        simple_par = par_sect._children[1]
        check.is_instance(simple_par, Paragraph)
        check.equal(simple_par.get_text(), "Paragraphs don’t require any special markup in AsciiDoc. "
                                           "A paragraph is just one or more lines of consecutive text.")

        # -------------------------------- with link ------------------------------- #
        par_with_link = par_sect._children[2]
        check.is_instance(par_with_link, Paragraph)
        check.equal(par_with_link.get_text(), "Paragraph with link Google")
        check.equal(par_with_link.get_text(url_opt='show_urls'), "Paragraph with link https://www.google.com/[Google]")

        # -------------------------------- with image ------------------------------- #
        par_with_link = par_sect._children[3]
        check.is_instance(par_with_link, Paragraph)
        check.equal(par_with_link.get_text(), "Paragraph with image im")
        check.equal(par_with_link.get_text(url_opt='show_urls'), "Paragraph with image image[im]")

        # -------------------------------- with \n (+) ------------------------------- #
        par_with_n = par_sect._children[4]
        text_before_n = par_with_n._children[0]
        text_n = par_with_n._children[1]
        text_after_n = par_with_n._children[2]
        check.is_instance(par_with_link, Paragraph)
        check.is_instance(text_before_n, TextLine)
        check.is_instance(text_n, TextLine)
        check.is_instance(text_after_n, TextLine)

        check.equal(par_with_n.get_text(), "Paragraph with \\n\nAfter\\n")
        check.equal(text_before_n.data, "Paragraph with \\n")
        check.equal(text_n.data, "\n")
        check.equal(text_after_n.data, "After\\n")

        # -------------------------------- literal --------------------------------- #
        lit_sect = section_dict[('AsciiDoc full syntax', 'Paragraphs', 'Literal')]
        lit_par = lit_sect._children[1]._children[0]
        check.is_instance(lit_par, Paragraph)
        check.equal(lit_par.get_text(), "A sequence of lines that begin with at least one space "
                                        "is a literal paragraph.\n"
                                        "Literal paragraphs are treated as preformatted text.\n"
                                        "The text is shown in a fixed-width font\n"
                                        "and endlines are preserved.")
        check.equal(lit_par.styles, ['literalblock'])

        # -------------------------------- sidebar --------------------------------- #
        sb_sect = section_dict[('AsciiDoc full syntax', 'Paragraphs', 'Sidebar')]
        sb_par = sb_sect._children[1]._children[0]
        check.is_instance(sb_par, Paragraph)
        check.equal(sb_par.get_text(), "AsciiDoc was first released in Nov 2002 by Stuart Rackham. "
                                       "It was designed from the start to be a shorthand syntax for "
                                       "producing professional documents like DocBook and LaTeX.")
        check.equal(sb_par.styles, ['sidebarblock'])

        # -------------------------------- example --------------------------------- #
        # first paragraph in example
        ex_sect = section_dict[('AsciiDoc full syntax', 'Paragraphs', 'Example & nested Listing')]
        exfirst_par = ex_sect._children[1]._children[0]
        check.is_instance(exfirst_par, Paragraph)
        check.equal(exfirst_par.get_text(), "Here’s a sample AsciiDoc document:")
        check.equal(exfirst_par.styles, ['exampleblock'])
        # nested paragraph
        ex_nest_listing_par = ex_sect._children[1]._children[1]._children[0]
        check.is_instance(ex_nest_listing_par, Paragraph)
        check.equal(ex_nest_listing_par.get_text(), "= Title of Document\nDoc Writer\n:toc:\n\nThis guide provides...")
        check.equal(ex_nest_listing_par.styles, ['exampleblock', "listingblock"])
        # last paragraph in example
        exsecond_par = ex_sect._children[1]._children[2]
        check.is_instance(exsecond_par, Paragraph)
        check.equal(exsecond_par.get_text(), "The document header is useful, but not required.")
        check.equal(exsecond_par.styles, ['exampleblock'])

        # --------------------------------- quote ---------------------------------- #
        qt_sect = section_dict[('AsciiDoc full syntax', 'Paragraphs', 'Quote')]
        qt_par = qt_sect._children[1]._children[0]
        check.is_instance(qt_par, Paragraph)
        check.equal(qt_par.get_text(), 'Four score and seven years ago our fathers brought forth on this continent '
                                       'a new nation…​')
        check.equal(qt_par.styles, ["quoteblock", "\n— Abraham Lincoln\nSoldiers' National Cemetery Dedication\n"])

        # ------------------------------- admonition ------------------------------- #
        adm_sect = section_dict[('AsciiDoc full syntax', 'Paragraphs', 'Admonition')]
        # note
        adm_note_par = adm_sect._children[1]._children[0]
        check.is_instance(adm_note_par, Paragraph)
        check.equal(adm_note_par.get_text(), 'An admonition paragraph draws the reader’s attention '
                                             'to auxiliary information. '
                                             'Its purpose is determined by the label '
                                             'at the beginning of the paragraph.')
        check.equal(adm_note_par.styles, ['note'])
        # tip
        adm_tip_par = adm_sect._children[2]._children[0]
        check.is_instance(adm_tip_par, Paragraph)
        check.equal(adm_tip_par.get_text(), 'Pro tip…​')
        check.equal(adm_tip_par.styles, ['tip'])
        # important
        adm_imp_par = adm_sect._children[3]._children[0]
        check.is_instance(adm_imp_par, Paragraph)
        check.equal(adm_imp_par.get_text(), 'Don’t forget…​')
        check.equal(adm_imp_par.styles, ['important'])
        # warning
        adm_warn_par = adm_sect._children[4]._children[0]
        check.is_instance(adm_warn_par, Paragraph)
        check.equal(adm_warn_par.get_text(), 'Watch out for…​')
        check.equal(adm_warn_par.styles, ['warning'])
        # caution
        adm_cau_par = adm_sect._children[5]._children[0]
        check.is_instance(adm_cau_par, Paragraph)
        check.equal(adm_cau_par.get_text(), 'Ensure that…​')
        check.equal(adm_cau_par.styles, ['caution'])

    def test_text_forms(self, section_dict):
        par_sect = section_dict[('AsciiDoc full syntax', 'Formatted Text')]
        par = par_sect._children[1]
        # italic
        it_tl = par._children[0]
        check.is_instance(it_tl, TextLine)
        check.equal(it_tl.data, 'italic phrase')
        check.equal(it_tl.styles, ['italic'])
        # bold
        b_tl = par._children[2]
        check.is_instance(b_tl, TextLine)
        check.equal(b_tl.data, 'bold phrase')
        check.equal(b_tl.styles, ['bold'])
        # monospace
        msp_tl = par._children[4]
        check.is_instance(msp_tl, TextLine)
        check.equal(msp_tl.data, 'monospace phrase')
        check.equal(msp_tl.styles, ['monospace'])

    def test_lists(self, section_dict):
        list_sect = section_dict[('AsciiDoc full syntax', 'Lists')]
        # first list
        first_list = list_sect._children[1]
        check.is_instance(first_list, List)
        check.equal(first_list.data, "level 1\n\n\n\nlevel 2\n\n\n\nlevel 3\n\n\n\nlevel 4"
                                     "\n\n\n\nlevel 5\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nlevel 1")
        # second list
        second_list = list_sect._children[3]
        check.is_instance(second_list, List)
        check.equal(second_list.data, "Step 1\n\n\nStep 2\n\n\n\nStep 2a\n\n\nStep 2b"
                                      "\n\n\n\n\n\nStep 3")

    def test_links(self, section_dict):
        link_sect = section_dict[('AsciiDoc full syntax', 'Links')]
        link = link_sect._children[1]._children[0]
        # simple link
        check.is_instance(link, Link)
        check.equal(link.data, 'http://asciidoctor.org')
        check.equal(link.attribute, 'http://asciidoctor.org')

        # link with attribute
        link = link_sect._children[2]._children[0]
        check.is_instance(link, Link)
        check.equal(link.data, 'index.html')
        check.equal(link.attribute, 'Docs')

    def test_images(self, section_dict):
        image_sect = section_dict[('AsciiDoc full syntax', 'Images')]
        # simple image
        first_image = image_sect._children[1]
        check.is_instance(first_image, Image)
        check.equal(first_image.data, 'http://asciidoctor.org/images/octocat.jpg')
        # image in paragraph
        second_image = image_sect._children[2]._children[1]
        check.is_instance(second_image, Image)
        check.equal(second_image.data, 'icons/play.png')

    def test_videos(self, section_dict):
        vid_sect = section_dict[('AsciiDoc full syntax', 'Videos')]
        video = vid_sect._children[1]
        check.is_instance(video, Video)
        check.equal(video.data, "video_file.mp4")

    def test_audios(self, section_dict):
        aud_sect = section_dict[('AsciiDoc full syntax', 'Audios')]
        audio = aud_sect._children[1]
        check.is_instance(audio, Audio)
        check.equal(audio.data, "ocean-waves.wav")

    def test_source(self, section_dict):
        source_sect = section_dict[('AsciiDoc full syntax', 'Source Code')]
        source = source_sect._children[1]._children[0]
        check.is_instance(source, SourceBlock)
        check.equal(source.data, "from adparser import Parser\nmy_file = open(test.adoc)\nparser = Parser(my_file)")
        check.equal(source.styles[-1], "python")

    def test_tables(self, section_dict):
        table_sect = section_dict[('AsciiDoc full syntax', 'Tables')]
        # table with named columns
        table_named = table_sect._children[1]
        check.is_instance(table_named, Table)
        check.equal(table_named.data, {'Column 1': ['Cell in column 1'], 'Column 2': ['Cell in column 2'],
                                       'Column 3': ['Cell in column 3'], 'Column 4': ['Cell in column 4']})
        # matrix table
        table_matrix = table_sect._children[2]
        check.is_instance(table_matrix, Table)
        check.equal(table_matrix.data, {
            'col1': ['Cell in column 1, row 1', 'Cell in column 1, row 2', 'Cell in column 1, row 3'],
            'col2': ['Cell in column 2, row 1', 'Cell in column 2, row 2', 'Cell in column 2, row 3']})
