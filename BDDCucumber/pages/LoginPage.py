from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.HomePage import HomePage


class LoginPage:
    userNameEle = (By.ID, "user-name")
    passwordEle = (By.ID, "password")
    loginButton = (By.XPATH, "//input[@id = 'login-button']")
    accountLockedMessage = (By.XPATH, "//h3[contains(text(), 'has been locked out')]")
    loginBotImage = (By.CLASS_NAME, "bot_column")
    swagLabLogo = (By.CLASS_NAME, "login_logo")
    emptyUserNameMessage = (By.XPATH, "//h3[contains(text(), 'Username is ')]")
    emptyUserNameMessage = (By.XPATH, "//h3[contains(text(), 'Password is ')]")

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, user):
        BasePage.inputSendKeys(self, self.userNameEle, user)

    def enterPassword(self, pwd):
        BasePage.inputSendKeys(self, self.passwordEle, pwd)

    def clickLoginButton(self):
        BasePage.elementClick(self, self.loginButton)
        return HomePage(self)

    def validateTitle(self):
        assert self.get_title() == "Swag Labs"

    def validateInvalidCreds(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Epic sadface: Username and password do not match any " \
                                                               "user in this service "

    def validateEmptyUsername(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Epic sadface: Username is required"

    def validateEmptyPassword(self):
        assert self.getElementText(self.MSG_INVALIDCREDS) == "Epic sadface: Password is required"

    def validateAccountLockMessage(self):
        assert self.getElementText(self.accountLockedMessage) == "Epic sadface: Sorry, this user has been locked out."

    def validateLoginPagelanding(self):
        print("Login Page Landing..!")
