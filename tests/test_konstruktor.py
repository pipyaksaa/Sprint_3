import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


def test_constructor_navigation_to_loaf(driver):
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')))
    driver.find_element(By.XPATH, '//span[contains(text(),"Начинки")]').click()
    time.sleep(3)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//p[contains(text(),"Мясо бессмертных моллюсков Protostomia")]')))
    driver.find_element(By.XPATH, '//span[contains(text(),"Булки")]').click()
    time.sleep(3)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]')))

def test_constructor_navigation_to_sous(driver):
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')))
    driver.find_element(By.XPATH, '//span[contains(text(),"Соусы")]').click()
    time.sleep(3)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//p[contains(text(),"Соус Spicy-X")]')))\


def test_constructor_navigation_to_filling(driver):
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')))
    driver.find_element(By.XPATH, '//span[contains(text(),"Начинки")]').click()
    time.sleep(3)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, '//p[contains(text(),"Мясо бессмертных моллюсков Protostomia")]')))
