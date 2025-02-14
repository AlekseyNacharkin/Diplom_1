
from Diplom_1.bun import Bun
from Diplom_1.burger import Burger
from Diplom_1.ingredient import Ingredient
from Diplom_1.tests.test_data import *

class TestBurgers():
    def test_set_burger_bun(self):
        bun = Bun(BurgerData.BUN_NAME, BurgerData.BUN_PRICE)
        ingredient = Ingredient(BurgerData.INGREDIENT_TYPE, BurgerData.INGREDIENT_NAME, BurgerData.INGREDIENT_PRICE)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == BurgerData.TOTAL

    def test_remove_ingredients(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerData.INGREDIENT_NAME, BurgerData.INGREDIENT_PRICE)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredients(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerData.INGREDIENT_NAME, BurgerData.INGREDIENT_PRICE)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, BurgerData.INGREDIENT_NAME_FOR_MOVE_INGREDIENT, BurgerData.INGREDIENT_PRICE_FOR_MOVE_INGREDIENT)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient1)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == ingredient

    def test_get_receipt(self):
        bun = Bun(BurgerData.BUN_NAME, BurgerData.BUN_PRICE)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,BurgerData.INGREDIENT_NAME, BurgerData.INGREDIENT_PRICE)
        ingredient1 = Ingredient(BurgerData.INGREDIENT_SAUCE, INGREDIENT_TYPE_FILLING, BurgerData.INGREDIENT_PRICE_FOR_MOVE_INGREDIENT)
        burger = Burger()
        burger.set_buns(bun) == bun
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient1)
        assert burger.get_receipt() == BurgerData.ASSERTION_TEXT