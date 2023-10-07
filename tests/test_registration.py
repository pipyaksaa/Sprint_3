from random import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import LoginPageLocators

from conftest import driver
import random
import string

def generate_random_email():
    login = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com", "yourdomain.com"]
    domain = random.choice(domains)
    email = f"{login}@{domain}"
    return email

random_email = generate_random_email()

from locators import LoginPageLocators

class TestRegistration:
    def test_registration(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(LoginPageLocators.PERSONAL_CABINET_LINK))
        driver.find_element(*LoginPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK))
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_BUTTON))
        driver.find_element(*LoginPageLocators.NAME_INPUT).send_keys('Regina')
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_error_incorrect_password(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(LoginPageLocators.PERSONAL_CABINET_LINK))
        driver.find_element(*LoginPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK))
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_BUTTON))
        driver.find_element(*LoginPageLocators.NAME_INPUT).send_keys('')
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('123')
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))

