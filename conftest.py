import pytest

from src.bun import Bun


@pytest.fixture
def bun():
    name = 'Космоблука'
    price = 3.99
    return Bun(name, price)
