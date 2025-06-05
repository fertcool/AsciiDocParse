
from adparser import Parser
from adparser.Parser import print_tree
parser = Parser("full_syntax.adoc")
print_tree(parser._astree.head, 0)
# for par in parser.paragraphs():
#     print(par.get_text())
for docelem in parser.paragraphs():
    try:
        print(docelem.get_near("paragraph", ["exampleblock"], "up").get_text())
    except:
        continue


