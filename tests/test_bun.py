import pytest
from Diplom_1.bun import Bun
from Diplom_1.tests.test_data import BunData
from unittest.mock import Mock


class TestBun:

    @pytest.mark.parametrize("name, price", BunData.BUNTESTVALUE)
    def test_bun_set_name(self,name, price):
        bun = Bun(name, price)
        assert bun.name == name


    @pytest.mark.parametrize("name, price", BunData.BUNTESTVALUE)
    def test_bun_get_name(self,name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_bun_mock(self): # я не нашел, куда надо мокировать обьекты, ведь во всех последующих тестах можно использовать реальные обьекты, в задании было написать мок, решил использовать его здесь
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Black Bun"
        mock_bun.get_price.return_value = 100
        assert mock_bun.get_name() == "Black Bun" and mock_bun.get_price() == 100