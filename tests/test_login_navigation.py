from locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver


class TestLogin:
    def test_login_by_enter_by_account(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK))
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url

    def test_login_by_personal_kabinet(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(LoginPageLocators.PERSONAL_CABINET_LINK))
        driver.find_element(*LoginPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK))
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url

    def test_login_by_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_BUTTON))
        driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_LINK))
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url

    def test_login_by_forget_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_LINK))
        driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_LINK))
        assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url
