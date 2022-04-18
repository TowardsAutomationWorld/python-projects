from selenium.webdriver.common.by import By

from pages.AboutPage import AboutPage


class HomePage:
    cartIcon = (By.XPATH, "//a[@class = 'shopping_cart_link']")
    menuIcon = (By.XPATH, "//button[@id = 'react-burger-menu-btn']")
    aboutLink = (By.XPATH, "//a[@id = 'about_sidebar_link']")

    def __init__(self, driver):
        self.driver = driver

    def validateHomePageLanding(self):
        assert self.driver.title == 'Swag Labs'
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'
        # assert self.verify_element_displayed(self.cartIcon)

    def clickOnAboutLink(self):
        self.aboutLink.click()
        return AboutPage(self.context)
