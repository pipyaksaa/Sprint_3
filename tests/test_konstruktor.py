import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ConstructorLocators
from conftest import driver


class TestConstructor:
    def test_constructor_navigation_to_loaf(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorLocators.BURGER_TITLE))
        driver.find_element(*ConstructorLocators.STARTERS_MENU).click()
        assert expected_conditions.visibility_of_element_located(ConstructorLocators.MEAT_OPTION)(
            driver), "Мясо бессмертных моллюсков Protostomia не видно после перехода."

    def test_constructor_navigation_to_sous(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorLocators.BURGER_TITLE))
        driver.find_element(*ConstructorLocators.SAUCES_MENU).click()
        assert expected_conditions.visibility_of_element_located(ConstructorLocators.SPICY_X_SAUCE)(
            driver), "Соус Spicy-X не видно после перехода."

    def test_constructor_navigation_to_filling(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ConstructorLocators.BURGER_TITLE))
        driver.find_element(*ConstructorLocators.STARTERS_MENU).click()
        assert expected_conditions.visibility_of_element_located(ConstructorLocators.MEAT_OPTION)(
            driver), "Мясо бессмертных моллюсков Protostomia не видно после перехода."
