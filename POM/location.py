import time

import pytest

from Data import reading_object
bms_obj = reading_object.read_locators()


class Location:
    def __init__(self,driver):
        self.driver = driver

    def enter_city_name(self,city_):

        self.driver.find_element(*bms_obj['txt_cityname']).send_keys(city_[0])
        time.sleep(5)
        self.driver.find_element(*bms_obj['select_city']).click()
        time.sleep(5)

    def changecity(self):
        self.driver.find_element(*bms_obj['change_city']).click()
        time.sleep(5)

    def enter_city_name1(self,city_):

        self.driver.find_element(*bms_obj['txt_cityname']).send_keys(city_[1])
        time.sleep(5)

    def choose_city1(self):
        self.driver.find_element(*bms_obj['select_city']).click()

    def popular_city(self):

        list1 = ["Mumbai", "Delhi-NCR", "Bengaluru"]

        for city in list1:
            time.sleep(5)
            self.driver.find_element(*bms_obj['change_city']).click()

            self.driver.find_element_by_xpath(f"//ul[@class='sc-bNQFlB URchM']//span[text()='{city}']").click()

    def all_city(self):
        time.sleep(5)
        self.driver.find_element(*bms_obj['change_city']).click()
        self.driver.find_element(*bms_obj['all_city']).click()
        self.driver.find_element(*bms_obj['other_city']).click()
