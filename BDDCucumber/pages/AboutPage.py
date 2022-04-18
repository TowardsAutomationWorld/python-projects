from selenium.webdriver.common.by import By


class AboutPage:
    sauceLabsLogo = (By.XPATH, "//a[@aria-label = 'Home']")

    def __init__(self, driver):
        self.driver = driver

    def validateAboutPageLanding(self):
        assert self.getPageTitle() == 'Cross Browser Testing, Selenium Testing, Mobile Testing | Sauce Labs'
        assert self.getPageURL() == 'https://saucelabs.com/'
        assert self.verify_element_displayed(self.sauceLabsLogo)
