
from src.adparser.Parser import Parser

fff = open("tests/test.adoc")
parser = Parser(fff)
fff.close()
for docelem in parser.source_blocks():
    up_heading = docelem.get_near("heading", direction='up')
    print(up_heading.data)
    down_image = docelem.get_near("image", direction='down')
    print(down_image.data)

