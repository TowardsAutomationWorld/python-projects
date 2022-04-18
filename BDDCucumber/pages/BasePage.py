from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import InvalidSelectorException as exception
from selenium.webdriver.support import expected_conditions as exConditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    # def __init__(self, driver):
    #     self.driver = BrowserManager.getDriver()

    @staticmethod
    def elementClick(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(exConditions.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
        except exception as e:
            print("Exception! Can't click on the element")

    @staticmethod
    def inputSendKeys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(exConditions.visibility_of_element_located(by_locator)).send_keys(text)
        except exception as e:
            print("Exception! Can't click on the element")

    @staticmethod
    def getElementText(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(exConditions.visibility_of_element_located(by_locator))
        return element.text

    @staticmethod
    def getPageTitle(self):
        return self.driver.title

    @staticmethod
    def getPageURL(self):
        return self.driver.url

    @staticmethod
    def getElementAttribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 10).until(exConditions.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    @staticmethod
    def verifyElementDisplayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(exConditions.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except:
            return False

    @staticmethod
    def closeBroswer(self):
        self.driver.close()
