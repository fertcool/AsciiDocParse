import re

from lxml import html, etree
from src.adparser.AST.Scaners.Scaner import Scaner
from src.adparser.AST.Blocks.Blocks import *
from src.adparser.AST.Blocks.Enums import BlockType
from src.adparser.AST.ASTree import ASTree


class HTMLScaner(Scaner):

    def __init__(self):

        # stacks for creating lists of styles and headings in tree blocks

        self.__heading_stack = []  # [['h1', 'h1name', 0], ['h2', 'h2curname':h2curcounter], ['h3', 'h2curname':h2curcounter], ...]
        # The counter is how many items are currently planned to be added to the tree with the current heading

        self.__style_stack = []  # [['style1name',style1curcounter], ['style2name':style2curcounter], ['style3name':style3curcounter], ...]
        self.__htmltree_stack = []  # [[htmlnode1, adparentnode1], [htmlnode2, adparentnode2], [htmlnode3, adparentnode3] ]

        self.adtree = RootBlock()

    # -------  functions for working with stacks of styles and headers -------

    def __push_heading(self, htag, hname, hcounter):  # hname - name of header tag, hkey, hvalue as above
        if htag == 'h1':
            self.adtree.section = hname

        # we decrease the counter of the tags to view under upper header
        # if we have already viewed the inner header tags,
        # because the upper one will no longer have to be viewed
        if self.__heading_stack:
            self.__heading_stack[-1][2] -= hcounter

        self.__heading_stack.append([htag, hname, hcounter])

    def __pop_heading(self):
        if self.__heading_stack[-1][0] != 'h1':
            self.__heading_stack.pop()
        # if tags in the internal header has already been viewed, and the top one has nothing more to view,
        # then delete the top one as well
        if self.__heading_stack[-1][2] == 0:
            self.__heading_stack.pop()

    def __decrease_heading(self, html_node):
        if self.__heading_stack:
            if self.__heading_stack[-1][0] != 'h1':
                self.__heading_stack[-1][2] -= 1

            if self.__heading_stack[-1][2] == 0 and not len(html_node):
                # print(self.__heading_stack)
                self.__pop_heading()

    def __increase_heading(self):
        if self.__heading_stack:
            self.__heading_stack[-1][2] += 1

    def __push_style(self, stylename, stylecounter):
        self.__style_stack.append([stylename, stylecounter])

    def __pop_style(self):
        self.__style_stack.pop()
        if self.__style_stack[-1][1] == 0:
            self.__style_stack.pop()

    def __increase_style(self):
        if self.__style_stack:
            self.__style_stack[-1][1] += 1

    def __decrease_style(self, html_node):
        if self.__style_stack:
            self.__style_stack[-1][1] -= 1

            if self.__style_stack[-1][1] == 0 and not len(html_node):
                print(self.__style_stack)
                self.__style_stack.pop()

    # -------  functions for creating tree blocks -------

    def __create_heading(self, html_node, old_ad_parent):

        self.__push_heading(html_node.tag,
                            html_node.text_content(),
                            len(html_node.getparent()) - 1)
        new_ad_parent = Section([heading[1] for heading in self.__heading_stack], old_ad_parent)
        # for the last elements in the stack, we change the references to the parent ad_tree
        change_len = 0
        if html_node.tag == 'h1':  # h1 can be in the header tag, so we apply all the elements should be
            # inherited from the sector with it, and not just what is in the header tag

            change_len = len(self.__htmltree_stack)
        else:
            change_len = len(html_node.getparent())
        for node in self.__htmltree_stack[-(change_len - 1):]:
            node[1] = new_ad_parent

        return new_ad_parent

    def __create_admonition(self, html_node, old_ad_parent):
        self.__push_style(html_node.get("class").split()[1], 0)  # we set the counter to 0,
        # because we need to add only the number
        # of internal elements to the counter,
        # and not + external ones,
        # as in the case of headers

        return Admonition([heading[1] for heading in self.__heading_stack],
                          old_ad_parent,
                          [style[0] for style in self.__style_stack])

    # def print_html_content(self, element, level=0):
    #     indent = "  " * level
    #     print(f"{indent}{element.text or ''}")
    #
    #     for child in element.findall("li | dl | ol | ul"):
    #         self.print_html_content(child, level + 1)
    #         if child.tail:
    #             print(f"{indent}{child.tail.strip()}")

    def __create_delimeter(self, html_node, old_ad_parent):
        self.__push_style(html_node.get("class"), 0)

        new_ad_parent = DelimeterBlock([heading[1] for heading in self.__heading_stack],
                                       old_ad_parent,
                                       [style[0] for style in self.__style_stack])

        # in the style of a quote, we add the author
        if new_ad_parent.styles[-1] == "quoteblock":
            new_ad_parent.styles.append(html_node.xpath(".//*[@class='attribution']")[0].text_content())

        return new_ad_parent

    def __create_table(self, html_node, old_ad_parent):
        table_matrix = []
        table_dict = {}
        if html_node.find("thead") is not None:
            head = html_node.find("thead")

            table_matrix = [[x.text_content()] for x in head.findall(".//th")]
            table_dict = {x.text_content(): [] for x in head.findall(".//th")}

            body = html_node.find("tbody")

            for tr in body.findall(".//tr"):
                colomns = tr.findall(".//td")
                for i, tcol in zip(range(len(colomns)), tr.findall(".//td")):
                    table_matrix[i].append(tcol.text_content())

                for dek, tcol in zip(table_dict.keys(), tr.findall(".//td")):
                    table_dict[dek].append(tcol.text_content())

        else:
            body = html_node.find("tbody")
            table_dict = {'col' + str(i): [] for i in range(1, len(body.findall(".//tr")))}
            table_matrix = [[] for i in range(1, len(body.findall(".//tr")))]
            for tr in body.findall(".//tr"):
                for mcol, dcolkey, td in zip(table_matrix, table_dict.keys(), tr.findall(".//td")):
                    mcol.append(td.text_content())
                    table_dict[dcolkey].append(td.text_content())

        return Table(table_matrix, table_dict, [heading[1] for heading in self.__heading_stack],
                                   old_ad_parent,
                                   [style[0] for style in self.__style_stack])

    def __create_list(self, html_node, old_ad_parent):

        return List(html_node.text_content(), [
                    heading[1] for heading in self.__heading_stack],
                    old_ad_parent,
                    [style[0] for style in self.__style_stack])

    # ------- a function that forms a new block -------
    # sequentially checking the html element of the document for belonging to certain conditions
    def __checknode_createblock(self, html_node, old_ad_parent, go_down_flag: list) -> Block:  # -> parent (old or new)

        new_ad_parent = old_ad_parent

        # ---- 1 - the header element? -------
        # we work with the header tag in a special way, because it does not recursively include other html tags
        if html_node.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            new_ad_parent = self.__create_heading(html_node, old_ad_parent)

        # ---- 2 - the admonition element? -------
        elif html_node.get("class") in ['admonitionblock caution', 'admonitionblock note', 'admonitionblock tip',
                                        'admonitionblock important',
                                        'admonitionblock warning']:
            new_ad_parent = self.__create_admonition(html_node, old_ad_parent)

        # ---- 3 - the delimeter element? -------
        elif html_node.get("class") in ['sidebarblock', 'exampleblock', 'quoteblock', 'listingblock',

                                        'literalblock', 'literalblock output']:
            new_ad_parent = self.__create_delimeter(html_node, old_ad_parent)

        # ---- 4 - the table element? -------
        elif html_node.get("class") and html_node.tag == 'table' and html_node.get("class").startswith('tableblock '):
            new_ad_parent = self.__create_table(html_node, old_ad_parent)
            go_down_flag[0] = False

        elif html_node.get("class") and (html_node.get("class").startswith('dlist')
                                     or html_node.get("class").startswith('ulist')
                                     or html_node.get("class").startswith('olist')):
            new_ad_parent = self.__create_list(html_node, old_ad_parent)
            go_down_flag[0] = False

        else:
            pass
        """add code/image/video/audio/p/pre/a"""

        return new_ad_parent

    # ------- the main function, which, through a search in the depth of the html document, forms a tree -------
    def build_AST(self, htmltext: str) -> ASTree:
        cur_ad_parent = self.adtree
        cur_html_node = html.fromstring(htmltext)

        self.__htmltree_stack.append([cur_html_node, cur_ad_parent])

        while self.__htmltree_stack:
            cur_html_node, cur_ad_parent = self.__htmltree_stack.pop()

            self.__decrease_heading(cur_html_node)
            self.__decrease_style(cur_html_node)

            # a flag indicating that the current block has been not fully processed
            go_down_flag = [True]

            new_ad_parent = self.__checknode_createblock(cur_html_node, cur_ad_parent, go_down_flag)

            # creating a new tree node
            if not (new_ad_parent is cur_ad_parent):
                ASTree.add_sub_element(cur_ad_parent, new_ad_parent)

            if go_down_flag[0]:
                for child in reversed(cur_html_node.getchildren()):
                    self.__htmltree_stack.append([child, new_ad_parent])
                    self.__increase_heading()
                    self.__increase_style()

        return self.adtree
