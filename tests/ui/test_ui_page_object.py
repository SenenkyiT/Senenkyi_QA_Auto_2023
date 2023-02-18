from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import SignInPageOtherPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Створення об'єкту сторінки
    sign_in_page = SignInPage()

    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # Виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("test_user@fakemail.com", "IncorrectPassword")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()

# Тест для перевірки BBC news
@pytest.mark.other_ui
def test_check_incorrect_username_page_object_other_page():
    # Створення об'єкту сторінки
    sign_in_page_alternative = SignInPageOtherPage()

    # Відкриваємо сторінку https://account.bbc.com/signin
    sign_in_page_alternative.go_to()

    # Виконуємо спробу увійти в систему BBC
    sign_in_page_alternative.try_login("test_user@fakemail.com", "IncorrectPassword")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page_alternative.check_title("BBC – Sign in")

    # Закриваємо браузер
    sign_in_page_alternative.close()
