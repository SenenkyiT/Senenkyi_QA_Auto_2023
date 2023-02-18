from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

# Клас для перевірки GitHub
class SignInPage(BasePage):
    URL = 'https://github.com/login'
    
    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо неправильне ім'я користувача або поштову адресу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title



# Клас для перевірки BBC news
class SignInPageOtherPage(BasePage):
    #URL = 'https://account.bbc.com/signin?realm=%2F&clientId=Account&context=international&isCasso=false&action=sign-in&redirectUri=https%3A%2F%2Fsession.bbc.co.uk%2Fsession%2Fcallback%3Frealm%3D%2F&service=IdSignInService&nonce=r9VGeboZ-SuheB70SK9VtbrsChA6P88uQxk0'
    URL = 'https://account.bbc.com/signin'
    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPageOtherPage.URL)

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "user-identifier-input")

        # Вводимо неправильне ім'я користувача або поштову адресу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password-input")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.ID, "submit-button")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title