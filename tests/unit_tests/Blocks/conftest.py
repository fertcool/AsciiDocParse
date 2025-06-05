import pytest
from src.adparser import Parser


@pytest.fixture(scope="module")
def tree():
    try:
        parser = Parser("C:/Users/fertc/PycharmProjects/AsciiDocParse/tests/unit_tests/Blocks/test_block.adoc")
    except Exception as e:
        pytest.skip(f"Не удалось создать parser: {e}")
    return parser._astree


@pytest.fixture(scope="module")
def top_block(tree):
    return tree.head._children[0]._children[1]


@pytest.fixture(scope="module")
def mid_block(tree):
    return tree.head._children[0]._children[4]._children[1]


@pytest.fixture(scope="module")
def bot_block(tree):
    return tree.head._children[0]._children[7]._children[1]
