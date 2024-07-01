class TestIngredient:

    def test_get_price(self, first_ingredient):
        assert first_ingredient.get_price() == first_ingredient.price

    def test_get_name(self, first_ingredient):
        assert first_ingredient.get_name() == first_ingredient.name

    def test_get_type(self, first_ingredient):
        assert first_ingredient.get_type() == first_ingredient.type
