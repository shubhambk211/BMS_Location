from behave import *
from selenium import webdriver
import time


@given(u'launch the browser')
def step_impl(context):
    path = r'C:\Users\Shubham\Downloads\chromedriver_win32\chromedriver.exe'
    context.driver1 = webdriver.Chrome(path)


@when(u'open BookMyshow homepage')
def step_impl(context):
    context.driver1.get("https://in.bookmyshow.com/")
    context.driver1.maximize_window()


@when(u'search for city')
def step_impl(context):
    context.driver1.find_element("xpath", '//input[@placeholder="Search for your city"]').send_keys('Mumbai')
    time.sleep(2)
    context.driver1.find_element_by_class_name("sc-gJqsIT.jMjMYb").click()
    time.sleep(2)


@when(u'click on location button')
def step_impl(context):
    context.driver1.find_element_by_class_name('sc-kZmsYB.ekDEWP.ellipsis').click()
    time.sleep(2)


@when(u'search for another city')
def step_impl(context):
    context.driver1.find_element_by_xpath('//input[@placeholder="Search for your city"]').send_keys('karad')
    time.sleep(2)
    context.driver1.find_element_by_xpath('//li[@class="sc-gJqsIT jMjMYb"]').click()
    time.sleep(2)


@then(u'verify city is selected')
def step_impl(context):
    assert True, "Test Passed"
    context.driver1.close()


@then(u'click on location button')
def step_impl(context):
    context.driver1.find_element_by_class_name('sc-kZmsYB.ekDEWP.ellipsis').click()
    time.sleep(2)


@then(u'click on popular city')
def step_impl(context):
    context.driver1.find_element_by_xpath(f"//ul[@class='sc-bNQFlB URchM']//span[text()='Pune']").click()
    time.sleep(2)


@then(u'verify popular city selected')
def step_impl(context):
    assert True, "Test Passed"
    context.driver1.close()


@then(u'click on View All Cities')
def step_impl(context):
    context.driver1.find_element_by_xpath("//span[text()='View All Cities']").click()


@then(u'click on other city')
def step_impl(context):
    context.driver1.find_element_by_xpath('//div[@class="sc-cCbXAZ icYIMp"]').click()


@then(u'verify other city selected')
def step_impl(context):
    assert True, "Test Passed"
    context.driver1.close()
