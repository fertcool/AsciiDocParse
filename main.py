
from src.adparser.Parser import Parser

fff = open("tests/test.adoc")
parser = Parser(fff)
fff.close()
for p in parser.paragraphs([], ['DNF']):
    print(p.get_text())

