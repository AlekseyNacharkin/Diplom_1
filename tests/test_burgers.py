
from Diplom_1.bun import Bun
from Diplom_1.burger import Burger
from Diplom_1.ingredient import Ingredient
from Diplom_1.tests.test_data import *

class TestBurgers():
    def test_set_burger_bun(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price)
        ingredient = Ingredient(BurgerData.ingredient_type, BurgerData.ingredient_name, BurgerData.ingredient_price)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 11.73

    def test_remove_ingredients(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerData.ingredient_name, BurgerData.ingredient_price)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredients(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerData.ingredient_name, BurgerData.ingredient_price)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, BurgerData.ingredient_name_for_move_ingredient, BurgerData.ingredient_price_for_move_ingredient)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient1)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == ingredient

    def test_get_receipt(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,BurgerData.ingredient_name, BurgerData.ingredient_price)
        ingredient1 = Ingredient(BurgerData.ingredient_sauce, INGREDIENT_TYPE_FILLING, BurgerData.ingredient_price_for_move_ingredient)
        burger = Burger()
        burger.set_buns(bun) == bun
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient1)
        assert burger.get_receipt() == BurgerData.ASSERTION_TEXT