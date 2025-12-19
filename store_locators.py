from selenium.webdriver.common.by import By


class StoreLocators:
    USERNAME = (By.XPATH, "//input[@name='user-name']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@name='login-button']")
    CATALOG_HEADER = (By.XPATH, "//span[text()='Products']")
    PRODUCT_BUTTON_1 = (
        By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]")
    CART_COUNTER = (By.XPATH, "//span[@class='shopping_cart_badge']")
    CART_BUTTON = (By.XPATH, "//a[@class='shopping_cart_link']")
    CART_HEADER = (By.XPATH, "//span[@class='title']")