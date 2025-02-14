from Diplom_1.database import Database
from Diplom_1.tests.test_data import *

class TestDatabase:

    def test_database_values_buns(self):
        database = Database()
        actual_buns = [(bun.name, bun.price) for bun in database.available_buns()]
        assert actual_buns == DatabaseData.EXPEXTED_BUNS

    def test_database_values_ingredients(self):
        database = Database()
        actual_ingredients = [(ingredient.type,ingredient.name, ingredient.price) for ingredient in database.available_ingredients()]
        assert actual_ingredients == DatabaseData.EXPEXTED_INGREDIENTS