import pytest

from praktikum.database import Database
from praktikum.burger import Burger


@pytest.fixture(scope="session")
def database():
    return Database()


@pytest.fixture
def bun(database):
    return database.available_buns()[0]


@pytest.fixture
def first_ingredient(database):
    return database.available_ingredients()[0]


@pytest.fixture()
def second_ingredient(database):
    return database.available_ingredients()[3]


@pytest.fixture()
def burger():
    return Burger()
