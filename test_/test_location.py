from POM.location import Location
from Data import reading_object
import pytest

data_obj = reading_object.read_data()


@pytest.mark.parametrize("city_",data_obj)
class TestLocation:
    def test_location(self,_driver,city_):
        lp = Location(_driver)
        lp.enter_city_name(city_)
        lp.changecity()
        lp.enter_city_name1(city_)
        lp.choose_city1()
        lp.popular_city()
        lp.all_city()