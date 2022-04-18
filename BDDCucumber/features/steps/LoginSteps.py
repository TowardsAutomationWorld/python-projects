import self
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from core.BrowserManager import BrowserManager

from pages.AboutPage import AboutPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

driver = BrowserManager.getInstance().getDriver()

homePage = HomePage(driver)
aboutPage = AboutPage(driver)
loginPage = LoginPage(driver)


@given('user launches the demo application')
def launchBrowser(context):
    # BrowserManager.getInstance().getDriver(self)
    print("Sample Text..!")


@when('user should land on the login page')
def landingLoginPage(context):
    loginPage.validateLoginPagelanding()


@then('user click on login button on the bottom of the section')
def loginButtonClick(context):
    loginPage.clickLoginButton()


@then('user close the application')
def closeTheApplication(context):
    driver.close()


@then('user enter username as "{userName}" in the user name field')
def userNameEnteredInUI(context, userName):
    loginPage.enterUsername(userName)


@then('user enter password as "{password}" in the password field')
def passwordEnteredInUI(context, password):
    loginPage.enterPassword(password)


@then('user should land on home page')
def homePageLanding(context):
    # homePage.validateHomePageLanding()
    print("Abs")