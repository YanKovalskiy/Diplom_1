import pytest

from src.praktikum.bun import Bun
from src.praktikum.ingredient import Ingredient
from src.praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    name = 'Флюоресцентная булка R2-D3'
    price = 989.99
    return Bun(name, price)


@pytest.fixture
def ingredient():
    ingredient_type = INGREDIENT_TYPE_FILLING
    name = 'Биокотлета из марсианской Магнолии'
    price = 424
    return Ingredient(ingredient_type, name, price)
