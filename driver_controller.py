from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager


# Класс родитель, для управления драйвером независимо от типа браузера.
class DriverController:
    def __init__(self, driver):
        self.__driver = driver

    def get_element(self, locator, timeout=10):
        return (WebDriverWait(self.__driver, timeout)
                .until(EC.visibility_of_element_located(locator)))

    def input_to_field(self, locator, value, field_name, timeout=10):
        (WebDriverWait(self.__driver, timeout)
         .until(EC.element_to_be_clickable(locator))
         .send_keys(value))
        print(f"Input '{field_name}'")

    def click_button(self, locator, button_name, timeout=10):
        (WebDriverWait(self.__driver, timeout)
         .until(EC.element_to_be_clickable(locator))
         .click())
        print(f"Click '{button_name}' button")

    def get_text(self, locator, timeout=10):
        return (WebDriverWait(self.__driver, timeout)
                .until(EC.visibility_of_element_located(locator))
                .text)

    def get_current_url(self):
        return self.__driver.current_url

    def run(self, url):
        self.__driver.get(url)
        self.__driver.maximize_window()

    def quit(self):
        self.__driver.quit()

    def change_window_size(self, width, height):
        self.__driver.set_window_size(width, height)


# Класс наследник, для инициализации и работы с браузером Chrome.
class ChromeDriverController(DriverController):
    def __init__(self, prefs):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", prefs)
        self.__driver = webdriver.Chrome(
            options=options,
            service=ChromeService(ChromeDriverManager().install())
        )
        super().__init__(self.__driver)


# Класс наследник, для инициализации и работы с браузером Firefox.
class FirefoxDriverController(DriverController):
    def __init__(self):
        self.__driver = webdriver.Firefox(service=FirefoxService(
            FirefoxDriverManager().install()))
        super().__init__(self.__driver)