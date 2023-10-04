from random import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

def test_registration(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(
        By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']").send_keys('Regina')
    driver.find_element(
        By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(random_email)
    driver.find_element(
        By.CSS_SELECTOR, "input[name='Пароль']").send_keys('123456')
    driver.find_element(
        By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()
    current_curl = driver.current_url
    current_curl == 'https://stellarburgers.nomoreparties.site'


def test_error_incorrect_password(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(
        By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']").send_keys('')
    driver.find_element(
        By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(random_email)
    driver.find_element(
        By.CSS_SELECTOR, "input[name='Пароль']").send_keys('123')
    driver.find_element(
        By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()
    driver.find_element(
        By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p")
