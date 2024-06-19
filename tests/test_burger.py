from helpers import add_ingredients


class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_one_ingredient(self, burger, first_ingredient):
        burger.add_ingredient(first_ingredient)

        assert first_ingredient in burger.ingredients

    def test_add_two_ingredient(self, burger, first_ingredient, second_ingredient):
        ingredients = (first_ingredient, second_ingredient)
        add_ingredients(burger, ingredients)

        assert first_ingredient in burger.ingredients
        assert second_ingredient in burger.ingredients

    def test_remove_ingredient_by_index(self, burger, first_ingredient, second_ingredient):
        ingredients = (first_ingredient, second_ingredient)
        add_ingredients(burger, ingredients)
        burger.remove_ingredient(1)

        assert second_ingredient not in burger.ingredients

    def test_move_ingredient_to_new_position(self, burger, first_ingredient, second_ingredient):
        ingredients = (first_ingredient, second_ingredient)
        add_ingredients(burger, ingredients)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == second_ingredient

    def test_get_price(self, burger, bun, first_ingredient, second_ingredient):
        burger.set_buns(bun)
        ingredients = (first_ingredient, second_ingredient)
        add_ingredients(burger, ingredients)
        price = bun.price*2 + first_ingredient.price + second_ingredient.price

        assert burger.get_price() == price

    def test_get_receipt(self, burger, bun, first_ingredient, second_ingredient):
        burger.set_buns(bun)
        ingredients = (first_ingredient, second_ingredient)
        add_ingredients(burger, ingredients)

        price = bun.price * 2 + first_ingredient.price + second_ingredient.price
        receipt = (f'(==== {bun.name} ====)\n'
                   f'= {str(first_ingredient.type).lower()} {first_ingredient.name} =\n'
                   f'= {str(second_ingredient.type).lower()} {second_ingredient.name} =\n'
                   f'(==== {bun.name} ====)\n\n'
                   f'Price: {price}')

        assert burger.get_receipt() == receipt
