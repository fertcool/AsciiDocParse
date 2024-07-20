
from src.adparser import Parser

fff = open("tests/test.adoc")
parser = Parser(fff)
fff.close()
for docelem in parser.tables():
    up_heading = docelem.get_near("heading", direction='up')
    print(up_heading.data)


