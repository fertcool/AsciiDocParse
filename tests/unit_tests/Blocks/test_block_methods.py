"""getnear"""
import pytest
import pytest_check as check

from adparser.AST.Blocks import Paragraph


class TestBlockMethods:

    def base_test(self, block, test_input, expected):
        type = test_input[0]
        style = test_input[1]
        direction = test_input[2]
        search_block = block.get_near(type, style, direction)
        if isinstance(search_block, Paragraph):
            check.equal(search_block.get_text(), expected)
        elif search_block is None:
            check.equal(search_block, expected)
        else:
            check.equal(search_block.data, expected)

    @pytest.mark.parametrize("test_input,expected", [(["heading", None, "up"], "Tytle"),
                                                     (["heading", None, "down"], "s1"),
                                                     (["paragraph", None, "up"], None),
                                                     (["paragraph", ["exampleblock"], "down"], "s1 par"),
                                                     (["paragraph", ["literalblock"], "down"], "s1 nest"),
                                                     (["paragraph", ["quoteblock"], "down"], "s1 quote"),
                                                     (["paragraph", ["tip"], "down"], "s1 tip"),
                                                     (["text_line", ["bold"], "down"], "s1 bold"),
                                                     (["source_block", ["python"], "down"], "s1 python"),
                                                     (["link", None, "down"], "s2_link"),
                                                     (["image", None, "down"], "s2_im"),
                                                     (["video", None, "down"], "s2_video"),
                                                     (["audio", None, "down"], "s2_aud"),
                                                     (["table", None, "down"], {'col1': ["s2 table"]}),
                                                     (["list", None, "down"], 's2l1\n\n\n\ns2l2')])
    def test_get_near_top(self, top_block, test_input, expected):
        self.base_test(top_block, test_input, expected)

    @pytest.mark.parametrize("test_input,expected", [(["heading", None, "up"], "middle"),
                                                     (["heading", None, "down"], "s3"),
                                                     (["paragraph", None, "up"], "s2_link"),
                                                     (["paragraph", ["exampleblock"], "up"], "s1 nest"),
                                                     (["paragraph", ["literalblock"], "up"], "s1 nest"),
                                                     (["paragraph", ["quoteblock"], "up"], "s1 quote"),
                                                     (["paragraph", ["tip"], "up"], "s1 tip"),
                                                     (["paragraph", ["exampleblock"], "down"], "s4 par"),
                                                     (["paragraph", ["literalblock"], "down"], "s4 nest"),
                                                     (["paragraph", ["quoteblock"], "down"], "s4 quote"),
                                                     (["paragraph", ["tip"], "down"], "s4 tip"),
                                                     (["text_line", ["bold"], "up"], "s1 bold"),
                                                     (["text_line", ["bold"], "down"], "s4 bold"),
                                                     (["source_block", ["python"], "up"], "s1 python"),
                                                     (["source_block", ["python"], "down"], "s4 python"),
                                                     (["link", None, "up"], "s2_link"),
                                                     (["link", None, "down"], "s3_link"),
                                                     (["image", None, "up"], "s2_im"),
                                                     (["image", None, "down"], "s3_im"),
                                                     (["video", None, "up"], "s2_video"),
                                                     (["video", None, "down"], "s3_vid"),
                                                     (["audio", None, "up"], "s2_aud"),
                                                     (["audio", None, "down"], "s3_aud"),
                                                     (["table", None, "up"], {'col1': ["s2 table"]}),
                                                     (["table", None, "down"], {'col1': ["s3 table"]}),
                                                     (["list", None, "up"], 's2l1\n\n\n\ns2l2'),
                                                     (["list", None, "down"], 's3l1\n\n\n\ns3l2')])
    def test_get_near_middle(self, mid_block, test_input, expected):
        self.base_test(mid_block, test_input, expected)

    @pytest.mark.parametrize("test_input,expected", [(["heading", None, "up"], "bottom"),
                                                     (["paragraph", None, "down"], None),
                                                     (["paragraph", ["exampleblock"], "up"], "s4 nest"),
                                                     (["paragraph", ["literalblock"], "up"], "s4 nest"),
                                                     (["paragraph", ["quoteblock"], "up"], "s4 quote"),
                                                     (["paragraph", ["tip"], "up"], "s4 tip"),
                                                     (["text_line", ["bold"], "up"], "s4 bold"),
                                                     (["source_block", ["python"], "up"], "s4 python"),
                                                     (["link", None, "up"], "s3_link"),
                                                     (["image", None, "up"], "s3_im"),
                                                     (["video", None, "up"], "s3_vid"),
                                                     (["audio", None, "up"], "s3_aud"),
                                                     (["table", None, "up"], {'col1': ["s3 table"]}),
                                                     (["list", None, "up"], 's3l1\n\n\n\ns3l2')])
    def test_get_near_bottom(self, bot_block, test_input, expected):
        self.base_test(bot_block, test_input, expected)