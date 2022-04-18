import driver as driver
import self
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.GlobalConfig import GlobalConfig
from selenium import webdriver


class BrowserManager:

    driver = None

    def __init__(self):
        if BrowserManager.driver is None:
            BrowserManager.driver = self
        else:
            raise Exception("We can not creat another class")

    @staticmethod
    def getInstance():
        if not BrowserManager.driver:
            BrowserManager()
        return BrowserManager.driver

    @staticmethod
    def getDriver():
        if BrowserManager.driver is not None:
            runMode = GlobalConfig.readConfigValues("runMode")
            browserName = GlobalConfig.readConfigValues("browserName")

            if runMode == "Local":
                if browserName == 'Chrome':
                    print("Chrome Browser")
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                elif browserName == 'Firefox':
                    print("Firefox Browser..!")
                    return webdriver.Firefox(executable_path=GeckoDriverManager().install())
                elif browserName == 'Safari':
                    driver = webdriver.Safari()
                else:
                    print("Please Pass The Correct Browser Name..!")
                driver.implicitly_wait(5)
                driver.maximize_window()
                driver.get(GlobalConfig.readConfigValues("appURL"))

            elif runMode == 'Dcoker':
                print("Script Executing in Docker Container..!")
        return driver


