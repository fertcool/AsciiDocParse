import pytest
from src.adparser.AST.Blocks import Section
from src.adparser import Parser


@pytest.fixture(scope="module")
def tree():
    try:
        parser = Parser("C:/Users/fertc/PycharmProjects/AsciiDocParse/tests/unit_tests/ASTcreate/full_syntax.adoc")
    except Exception as e:
        pytest.skip(f"Не удалось создать parser: {e}")
    return parser._astree


@pytest.fixture(scope="module")
def section_dict(tree):
    sectdict = {}
    stack = [tree.head]

    while stack:
        node = stack.pop()
        if isinstance(node, Section):
            sectdict[tuple(node.section)] = node

        for child in reversed(node._children):
            stack.append(child)

    return sectdict


@pytest.fixture(scope="module")
def section_list(tree):
    sectlist = []
    stack = [tree.head]

    while stack:
        node = stack.pop()
        if isinstance(node, Section):
            sectlist.append(node)

        for child in reversed(node._children):
            stack.append(child)

    return sectlist

