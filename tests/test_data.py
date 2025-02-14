from datetime import date

from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunData:
    BUNTESTVALUE = [("булочка", 1),(1,"3")]

class IngridientData:
    VALUES = [("соус","табаско", 250.5)]
    #PRICEVALUES = [1, 2.3, "2,3", date(2021, 1, 1), True]

class BurgerData:
    ASSERTION_TEXT = ('(==== булочка 1 ====)\n''= sauce начинка =\n''= соус FILLING =\n''(==== булочка 1 ====)\n''\n''Price: 21.72')
    bun_name = "булочка 1"
    bun_price = 4.20
    ingredient_type = INGREDIENT_TYPE_FILLING
    ingredient_name = "начинка"
    ingredient_price = 3.33
    ingredient_name_for_move_ingredient = "начиночка"
    ingredient_price_for_move_ingredient = 9.99
    ingredient_sauce = "соус"
class DatabaseData():
    EXPEXTED_BUNS = [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ]

    EXPEXTED_INGREDIENTS = [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]
