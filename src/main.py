import lxml.html

from adparser.Parser import Parser
import re

from lxml import html, etree



with open("C:/Users/fertc/PycharmProjects/AsciiDocParse/tests/test.html") as my_file:
    parser = Parser(my_file, link_opt='show_url')


