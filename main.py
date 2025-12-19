import time

from login_page import LoginPage
from store_locators import StoreLocators
from driver_controller import ChromeDriverController, FirefoxDriverController


class Test:
    def __init__(self, driver):
        self.__driver = driver
        self._locators = StoreLocators()
        self.login = LoginPage(self.__driver)
        self.__is_authorized = False

    def start(self, url):
        self.__driver.run(url)

    def end(self, timeout=5):
        time.sleep(timeout)
        self.__driver.quit()

    def test_authorization(self):
        print("\nSTART TEST: Authorization")

        # Производим авторизацию.
        self.__is_authorized = self.login.authorization(
            "standard_user","secret_sauce")

        # Проверяем, заголовок текущей страницы.
        page_header_text = self.__driver.get_text(
            self._locators.CATALOG_HEADER)
        assert page_header_text == "Products", "FAILED: header is incorrect!"
        print("PASSED: header is correct!")
        print("END TEST: Authorization")

    def test_add_product_to_cart(self):
        print("\nSTART TEST: Add product to cart")

        # Авторизуемся, если пользователь не авторизован.
        if not self.__is_authorized:
            self.__is_authorized = self.login.authorization(
                "standard_user", "secret_sauce")

        # Добавляем первый товар в корзину.
        self.__driver.click_button(
            self._locators.PRODUCT_BUTTON_1, "Add to cart")

        # Проверяем, что счетчик корзины равен "1".
        cart_counter = self.__driver.get_text(self._locators.CART_COUNTER)
        assert cart_counter == '1', "FAILED: Product hasn't been added!"
        print("PASSED: Product has been added!")
        print("END TEST: Add product to cart")

    def test_enter_to_cart(self):
        print("\nSTART TEST: Enter to cart")

        # Авторизуемся, если пользователь не авторизован.
        if not self.__is_authorized:
            self.__is_authorized = self.login.authorization(
                "standard_user", "secret_sauce")

        # Нажимаем на кнопку корзины.
        self.__driver.click_button(self._locators.CART_BUTTON, "Cart")

        # Проверяем заголовок корзины.
        cart_header = self.__driver.get_text(self._locators.CART_HEADER)
        assert cart_header == "Your Cart", "FAILED: Cart header is incorrect!"
        print("PASSED: Cart header is correct!")

        # Проверяем URL корзины
        cart_url = "https://www.saucedemo.com/cart.html"
        assert self.__driver.get_current_url() == cart_url, \
            "FAILED: URL is incorrect!"
        print("PASSED: URL is correct!")
        print("END TEST: Enter to cart")


prefs = {
    "detach": True,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}
# Создаем экземпляр класса с драйвером Chrome
chrome_driver = ChromeDriverController(prefs)
# Создаем экземпляр класса Test для тестирования.
test = Test(chrome_driver)
# Запускаем браузера для тестирвания.
test.start("https://www.saucedemo.com/")
# Запускаем тест авторизации пользователя.
test.test_authorization()
# Запускаем тест добавления товара в корзину.
test.test_add_product_to_cart()
# Запускаем тест открытия страницы корзины.
test.test_enter_to_cart()
# Закрываем браузер после тестирования.
test.end()