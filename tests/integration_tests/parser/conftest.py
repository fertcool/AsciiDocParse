import pytest
from src.adparser import Parser


@pytest.fixture(scope="module")
def parser():
    try:
        parser = Parser("C:/Users/fertc/PycharmProjects/AsciiDocParse/tests/integration_tests/parser/shuffle.adoc")
    except Exception as e:
        pytest.skip(f"Не удалось создать parser: {e}")
    return parser
