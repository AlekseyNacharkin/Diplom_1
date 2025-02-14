import pytest
from Diplom_1.ingredient import Ingredient
from Diplom_1.tests.test_data import IngridientData


class TestIngredient:
    @pytest.mark.parametrize("type,name,price", IngridientData.VALUES)
    def test_get_price(self,type,name,price):
        ingredient = Ingredient(type,name,price)
        assert ingredient.get_price() == price
