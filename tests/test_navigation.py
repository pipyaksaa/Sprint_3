# test_navigation.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import NavigationLocators
from conftest import driver

class TestNavigation:
    def test_logout(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            NavigationLocators.PERSONAL_CABINET_LINK))
        driver.find_element(*NavigationLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            NavigationLocators.LOGIN_HEADER))
        driver.find_element(*NavigationLocators.EMAIL_INPUT).send_keys('aaaa@aa.a')
        driver.find_element(*NavigationLocators.PASSWORD_INPUT).send_keys('aaaaaaaa')
        driver.find_element(*NavigationLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_matches("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(*NavigationLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationLocators.LOGOUT_BUTTON))
        driver.find_element(*NavigationLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(NavigationLocators.REGISTRATION_LINK))
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url

    def test_go_to_lk(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
            NavigationLocators.PERSONAL_CABINET_LINK))
        driver.find_element(*NavigationLocators.PERSONAL_CABINET_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationLocators.REGISTRATION_LINK))

    def test_go_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationLocators.REGISTRATION_LINK))
        driver.find_element(*NavigationLocators.CONSTRUCTOR_LINK).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            NavigationLocators.BURGER_TITLE))
