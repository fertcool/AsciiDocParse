import pytest
import pytest_check as check

from adparser.AST.Blocks import Paragraph


class TestParserMethods:

    def base_test(self, parse_method, test_input, expected):
        result_list = list(parse_method(test_input[1], test_input[0]))
        if not result_list:
            check.equal(result_list, expected)
        for expect_list, result in zip(expected, result_list):
            if isinstance(result, Paragraph):
                check.equal(result.get_text(), expect_list[0])
            else:
                check.equal(result.data, expect_list[0])
            check.equal(result.section, expect_list[1])
            check.equal(result.styles, expect_list[2])

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["Preambule par", ["Title"], []],
                                              ["sb_par_s1", ["Title", "s1"], ["sidebarblock"]],
                                              ["ex_par_s1 link_sb_s1", ["Title", "s1"], ["sidebarblock",
                                                                                         "exampleblock"]],
                                              ["listi_par_s1", ["Title", "s1"], ["sidebarblock",
                                                                                 "exampleblock",
                                                                                 "literalblock"]],
                                              ["quote_s1", ["Title", "s1"], ["quoteblock", "\n— s1_q\n"]],
                                              ["bold_s2 par_s2", ["Title", "s2"], []],
                                              ["s21_note", ["Title", "s2", "s21"], ["note"]],
                                              ["google.com", ["Title", "s2", "s21"], []],
                                              ["it_s21", ["Title", "s2", "s21"], []],
                                              ["s3 quote", ["Title", "s3"], ["quoteblock", '\n— s3\n']],
                                              ["s31 tip", ["Title", "s3", "s31"], ["tip"]],
                                              ["msp_s31 ← par_s31", ["Title", "s3", "s31"], []],
                                              ["par_s311", ["Title", "s3", "s31", "s311"], []],
                                              ["it_war_s311", ["Title", "s3", "s31", "s311"], ["warning"]],
                                              ["par_s4", ["Title", "s4"], []]]),
                              ([["s1"], None], [["sb_par_s1", ["Title", "s1"], ["sidebarblock"]],
                                                ["ex_par_s1 link_sb_s1", ["Title", "s1"], ["sidebarblock",
                                                                                           "exampleblock"]],
                                                ["listi_par_s1", ["Title", "s1"], ["sidebarblock",
                                                                                   "exampleblock",
                                                                                   "literalblock"]],
                                                ["quote_s1", ["Title", "s1"], ["quoteblock", "\n— s1_q\n"]]]),
                              ([["s2"], None], [["bold_s2 par_s2", ["Title", "s2"], []],
                                                ["s21_note", ["Title", "s2", "s21"], ["note"]],
                                                ["google.com", ["Title", "s2", "s21"], []],
                                                ["it_s21", ["Title", "s2", "s21"], []]]),
                              ([["s21"], None], [["s21_note", ["Title", "s2", "s21"], ["note"]],
                                                 ["google.com", ["Title", "s2", "s21"], []],
                                                 ["it_s21", ["Title", "s2", "s21"], []]]),
                              ([None, ["sidebarblock"]], [["sb_par_s1", ["Title", "s1"], ["sidebarblock"]],
                                                          ["ex_par_s1 link_sb_s1", ["Title", "s1"], ["sidebarblock",
                                                                                                     "exampleblock"]],
                                                          ["listi_par_s1", ["Title", "s1"], ["sidebarblock",
                                                                                             "exampleblock",
                                                                                             "literalblock"]]]),
                              ([None, ["quoteblock"]], [["quote_s1", ["Title", "s1"], ["quoteblock", "\n— s1_q\n"]],
                                                        ["s3 quote", ["Title", "s3"], ["quoteblock", '\n— s3\n']]]),
                              ([None, ["warning"]], [["it_war_s311", ["Title", "s3", "s31", "s311"], ["warning"]]]),
                              ([["s3"], ["quoteblock"]], [["s3 quote", ["Title", "s3"], ["quoteblock", '\n— s3\n']]]),
                              ([["s8"], ["quoteblock"]], [])
                              ]
                             )
    def test_paragraphs(self, parser, test_input, expected):
        self.base_test(parser.paragraphs, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["Preambule par", ["Title"], []],
                                              ["sb_par_s1", ["Title", "s1"], ["sidebarblock"]],
                                              ["ex_par_s1 ", ["Title", "s1"], ["sidebarblock",
                                                                               "exampleblock"]],
                                              ["listi_par_s1", ["Title", "s1"], ["sidebarblock",
                                                                                 "exampleblock",
                                                                                 "literalblock"]],
                                              ["quote_s1", ["Title", "s1"], ["quoteblock", "\n— s1_q\n"]],
                                              ["bold_s2", ["Title", "s2"], ["bold"]],
                                              [" par_s2", ["Title", "s2"], []],
                                              ["s21_note", ["Title", "s2", "s21"], ["note"]],
                                              ["it_s21", ["Title", "s2", "s21"], ["italic"]],
                                              ["s3 quote", ["Title", "s3"], ["quoteblock", '\n— s3\n']],
                                              ["s31 tip", ["Title", "s3", "s31"], ["tip"]],
                                              ["msp_s31", ["Title", "s3", "s31"], ["monospace"]],
                                              [" ← par_s31", ["Title", "s3", "s31"], []],
                                              ["par_s311", ["Title", "s3", "s31", "s311"], []],
                                              ["it_war_s311", ["Title", "s3", "s31", "s311"], ["warning", "italic"]],
                                              ["par_s4", ["Title", "s4"], []]]),
                              ([["s1"], None], [["sb_par_s1", ["Title", "s1"], ["sidebarblock"]],
                                                ["ex_par_s1 ", ["Title", "s1"], ["sidebarblock",
                                                                                 "exampleblock"]],
                                                ["listi_par_s1", ["Title", "s1"], ["sidebarblock",
                                                                                   "exampleblock",
                                                                                   "literalblock"]],
                                                ["quote_s1", ["Title", "s1"], ["quoteblock", "\n— s1_q\n"]]]),
                              ([["s2"], None], [["bold_s2", ["Title", "s2"], ["bold"]],
                                                [" par_s2", ["Title", "s2"], []],
                                                ["s21_note", ["Title", "s2", "s21"], ["note"]],
                                                ["it_s21", ["Title", "s2", "s21"], ["italic"]]]),
                              ([None, ["exampleblock"]], [["ex_par_s1 ", ["Title", "s1"], ["sidebarblock",
                                                                                           "exampleblock"]],
                                                          ["listi_par_s1", ["Title", "s1"], ["sidebarblock",
                                                                                             "exampleblock",
                                                                                             "literalblock"]]]),
                              ([None, ["italic"]], [["it_s21", ["Title", "s2", "s21"], ["italic"]],
                                                    ["it_war_s311", ["Title", "s3", "s31", "s311"],
                                                     ["warning", "italic"]]]),
                              ([["s3"], ["quoteblock"]], [["s3 quote", ["Title", "s3"], ["quoteblock", '\n— s3\n']]]),
                              ([["s6"], ["quoteblock"]], [])
                              ]
                             )
    def test_text_lines(self, parser, test_input, expected):
        self.base_test(parser.text_lines, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["Title", ["Title"], []],
                                              ["s1", ["Title", "s1"], []],
                                              ["s2", ["Title", "s2"], []],
                                              ["s21", ["Title", "s2", "s21"], []],
                                              ["s3", ["Title", "s3"], []],
                                              ["s31", ["Title", "s3", "s31"], []],
                                              ["s311", ["Title", "s3", "s31", "s311"], []],
                                              ["s4", ["Title", "s4"], []]]),
                              ([["s3"], None], [["s3", ["Title", "s3"], []]]),
                              ([["s311"], None], [["s311", ["Title", "s3", "s31", "s311"], []]]),
                              ([["s3411"], None], [])
                              ]
                             )
    def test_headings(self, parser, test_input, expected):
        self.base_test(parser.headings, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["s21l1\n\n\n\ns21l2", ["Title", "s2", "s21"], []],
                                              ["s311l1\n\n\n\ns311l2", ["Title", "s3", "s31", "s311"], ["warning"]]]),
                              ([["s2"], None], [["s21l1\n\n\n\ns21l2", ["Title", "s2", "s21"], []]]),
                              ([["s3"], None], [["s311l1\n\n\n\ns311l2", ["Title", "s3", "s31", "s311"], ["warning"]]]),
                              ([None, ["warning"]],
                               [["s311l1\n\n\n\ns311l2", ["Title", "s3", "s31", "s311"], ["warning"]]]),
                              ([["s3"], ["warning"]], [["s311l1\n\n\n\ns311l2", ["Title", "s3", "s31", "s311"],
                                                        ["warning"]]]),
                              ([["s3411"], None], [])
                              ]
                             )
    def test_lists(self, parser, test_input, expected):
        self.base_test(parser.lists, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["src_pre", ["Title"], ["listingblock", "python"]],
                                              ["src_s31", ["Title", "s3", "s31"], ["listingblock", "c++"]]]),
                              ([["s3"], None], [["src_s31", ["Title", "s3", "s31"], ["listingblock", "c++"]]]),
                              ([None, ["c++"]], [["src_s31", ["Title", "s3", "s31"], ["listingblock", "c++"]]]),
                              ([["s3"], ["c++"]], [["src_s31", ["Title", "s3", "s31"], ["listingblock", "c++"]]]),
                              ([["s3411"], None], [])
                              ]
                             )
    def test_source_blocks(self, parser, test_input, expected):
        self.base_test(parser.source_blocks, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [[{"col1": ["s2 table 1", "s2 table 2"]}, ["Title", "s2"], []],
                                              [{"col1": ["s3 ex table 1", "s3 ex table 2"]}, ["Title", "s3"],
                                               ["exampleblock"]]]),
                              ([["s2"], None], [[{"col1": ["s2 table 1", "s2 table 2"]}, ["Title", "s2"], []]]),
                              ([None, ["exampleblock"]], [[{"col1": ["s3 ex table 1", "s3 ex table 2"]},
                                                           ["Title", "s3"], ["exampleblock"]]]),
                              ([["s3"], ["exampleblock"]], [[{"col1": ["s3 ex table 1", "s3 ex table 2"]},
                                                             ["Title", "s3"], ["exampleblock"]]]),
                              ([["s3411"], None], [])
                              ]
                             )
    def test_tables(self, parser, test_input, expected):
        self.base_test(parser.tables, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["link_sb_s1", ["Title", "s1"], ["sidebarblock", "exampleblock"]],
                                              ["google.com", ["Title", "s2", "s21"], []]]),
                              ([["s21"], None], [["google.com", ["Title", "s2", "s21"], []]]),
                              ([["s1"], ["sidebarblock"]], [["link_sb_s1", ["Title", "s1"],
                                                             ["sidebarblock", "exampleblock"]]]),
                              ([["s3411"], None], [])
                              ]
                             )
    def test_links(self, parser, test_input, expected):
        self.base_test(parser.links, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["pre_im", ["Title"], []],
                                              ["im_ex_s3", ["Title", "s3"], ["exampleblock"]]]),
                              ([None, ["exampleblock"]], [["im_ex_s3", ["Title", "s3"], ["exampleblock"]]]),
                              ([["s3411"], None], [])
                              ]
                             )
    def test_images(self, parser, test_input, expected):
        self.base_test(parser.images, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["ex_vid_s1", ["Title", "s1"], ["sidebarblock", "exampleblock"]],
                                              ["vid_s2", ["Title", "s2"], []],
                                              ["vid_s31", ["Title", "s3", "s31"], []]]),
                              ([["s3"], None], [["vid_s31", ["Title", "s3", "s31"], []]]),
                              ([None, ["sidebarblock"]], [["ex_vid_s1", ["Title", "s1"],
                                                           ["sidebarblock", "exampleblock"]]]),
                              ([["s1"], ["sidebarblock"]], [["ex_vid_s1", ["Title", "s1"],
                                                             ["sidebarblock", "exampleblock"]]]),
                              ([["s3411"], None], [])

                              ]
                             )
    def test_videos(self, parser, test_input, expected):
        self.base_test(parser.videos, test_input, expected)

    @pytest.mark.parametrize("test_input,expected",
                             [([None, None], [["sb_aud_s1", ["Title", "s1"], ["sidebarblock"]],
                                              ["aud_s311", ["Title", "s3", "s31", "s311"], []]]),
                              ([["s3"], None], [["aud_s311", ["Title", "s3", "s31", "s311"], []]]),
                              ([["s1"], ["sidebarblock"]], [["sb_aud_s1", ["Title", "s1"], ["sidebarblock"]]]),
                              ([["s3411"], None], [])
                              ]
                             )
    def test_audios(self, parser, test_input, expected):
        self.base_test(parser.audios, test_input, expected)
