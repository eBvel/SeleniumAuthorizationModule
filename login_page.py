from store_locators import StoreLocators
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException


class LoginPage:

    def __init__(self, driver):
        self.__driver = driver
        self._locators = StoreLocators()

    def authorization(self, username, password):
        try:
            # Заполняем поля и нажимаем кнопку Login.
            self.__driver.input_to_field(
                self._locators.USERNAME, username, "Username")
            self.__driver.input_to_field(
                self._locators.PASSWORD, password, "Password")
            self.__driver.click_button(self._locators.LOGIN_BUTTON, "Login")
            catalog_url = "https://www.saucedemo.com/inventory.html"
            # Возвращаем TRUE, если текущий URL равен URL каталога.
            assert self.__driver.get_current_url() == catalog_url
            print("PASSED: URL is correct!")
            return True
        except NoSuchElementException as no_such_message:
            print(f"ERROR: {no_such_message}")
            return False
        except InvalidSelectorException as invalid_selector_message:
            print(f"ERROR: {invalid_selector_message}")
            return False
        except AssertionError as assertion_error:
            print(f"FAILED: URL is incorrect!\n"
                  f"ERROR: Invalid username or password!\n{assertion_error}")
            return False