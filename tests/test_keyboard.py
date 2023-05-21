import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def test_kb_class():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_init_(test_kb_class):
    assert test_kb_class.name == 'Dark Project KD87A'
    assert test_kb_class.language == 'EN'


def test_change_lang(test_kb_class):
    test_kb_class.change_lang()
    assert test_kb_class.language == 'RU'
