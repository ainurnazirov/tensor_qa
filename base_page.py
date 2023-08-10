from selenium.webdriver import Chrome

class BasePage:
    def __init__(self):
        self.driver = Chrome()


    def get_element(self, locator, timeout = 10):
        self.driver.implicitly_wait(timeout)
        return self.driver.find_element(*locator)


    def is_element_present(self, locator, timeout = 10):
        element = self.get_element(locator, timeout)
        return element.is_displayed()


    def enter_text(self, locator, text, timeout = 10):
        element = self.get_element(locator, timeout)
        element.clear()
        element.send_keys(text)


    def press_button(self, locator, button, timeout = 10):
        element = self.get_element(locator, timeout)
        element.send_keys(button)


    def click_element(self, locator, timeout = 10):
        element = self.get_element(locator, timeout)
        element.click()


    def get_text(self, locator, timeout = 10):
        element = self.get_element(locator, timeout)
        return element.text


    def get_value(self, locator, timeout = 10):
        element = self.get_element(locator, timeout)
        return element.get_attribute('value')


    def get_source(self, locator, timeout = 10):
        element = self.get_element(locator, timeout)
        return element.get_attribute('src')


    def quit(self):
        self.driver.quit()
