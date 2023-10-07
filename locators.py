from selenium.webdriver.common.by import By

class ConstructorLocators:
    BURGER_TITLE = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    STARTERS_MENU = (By.XPATH, '//span[contains(text(),"Начинки")]')
    MEAT_OPTION = (By.XPATH, '//p[contains(text(),"Мясо бессмертных моллюсков Protostomia")]')
    SAUCES_MENU = (By.XPATH, '//span[contains(text(),"Соусы")]')
    SPICY_X_SAUCE = (By.XPATH, '//p[contains(text(),"Соус Spicy-X")]')


class NavigationLocators:
    PERSONAL_CABINET_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(),'Вход')]")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password" and @name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]')
    REGISTRATION_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    CONSTRUCTOR_LINK = (By.XPATH, '//p[contains(text(),"Конструктор")]')
    BURGER_TITLE = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    PERSONAL_CABINET_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")


class LoginPageLocators:
    PERSONAL_CABINET_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input[@type="text"]')
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'p.input__error.text_type_main-default')