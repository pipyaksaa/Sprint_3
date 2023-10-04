
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


def test_logout(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Вход')]")))
    driver.find_element(
        By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys('aaaa@aa.a')
    driver.find_element(
        By.XPATH, '//input[@type="password" and @name="Пароль"]').send_keys('aaaaaaaa')
    driver.find_element(
        By.XPATH, '//button[contains(text(), "Войти")]').click()
    WebDriverWait(driver, 3).until(EC.url_matches("https://stellarburgers.nomoreparties.site/"))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Выход')]")))
    driver.find_element(By.XPATH, '//button[contains(text(),"Выход")]').click()
    WebDriverWait(driver, 3).until(EC.url_matches("https://stellarburgers.nomoreparties.site/login"))



def test_go_to_lk(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))


def test_go_to_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(By.XPATH, ' //p[contains(text(),"Конструктор")]').click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')))
