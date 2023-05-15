import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_hm_1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def test_hm_2():
    return Phone('iPhone 14', 120000, 5, 2)


def test__str__(test_hm_2, test_hm_1):
    assert str(test_hm_2) == 'iPhone 14'
    assert str(test_hm_1) == 'Смартфон'


def test__repr__(test_hm_2):
    assert repr(test_hm_2) == "Phone('iPhone 14', 120000, 5, 2)"
