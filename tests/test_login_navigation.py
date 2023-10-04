from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


def test_login_by_enter_by_account(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")))
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))


def test_login_by_personal_kabinet(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]")))
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")))


def test_login_by_registration_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")))
    driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Войти")]')))


def test_login_by_forget_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"Войти")]')))
    driver.find_element(By.XPATH, '//a[contains(text(),"Войти")]').click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Войти")]')))
