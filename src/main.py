import os

import lxml.html

from adparser.Parser import Parser
import re

from lxml import html, etree



with open("C:/Users/fertc/PycharmProjects/AsciiDocParse/tests/test1.html") as my_file:
    parser = Parser(my_file)

    for p in parser.headings():
        print(p.data)



