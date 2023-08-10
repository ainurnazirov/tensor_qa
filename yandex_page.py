from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage

class YandexPage(BasePage):
    SEARCH_FIELD = (By.NAME, "text")
    SUGGEST_TABLE = (By.CSS_SELECTOR, ".mini-suggest__popup")
    SEARCH_RESULTS_PAGE = (By.CSS_SELECTOR, "#search-result")
    FIRST_LINK = (By.CSS_SELECTOR, "#search-result .organic__url")
    MENU = (By.CSS_SELECTOR, ".services-suggest__list-item-more")
    IMAGES_CATEGORY = (By.LINK_TEXT, "Картинки")
    FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item__link img")
    IMAGE = (By.CSS_SELECTOR, '.MMImage-Origin')
    BUTTON_FORWARD = (By.CSS_SELECTOR, '.CircleButton_type_next')
    BUTTON_BACK = (By.CSS_SELECTOR, '.CircleButton_type_prev')


    def open_search_page(self):
        self.driver.get('https://ya.ru/')


    def is_search_field_present(self):
        return self.is_element_present(self.SEARCH_FIELD)


    def enter_search_query(self, query):
        self.enter_text(self.SEARCH_FIELD, query)


    def is_suggest_table_present(self):
        return self.is_element_present(self.SUGGEST_TABLE)


    def press_enter(self):
        self.press_button(self.SEARCH_FIELD, Keys.RETURN)


    def compare_first_link(self, url):
        return self.get_element(self.FIRST_LINK).get_attribute("href") == url


    def is_search_results_page_present(self):
        return self.is_element_present(self.SEARCH_RESULTS_PAGE)


    def is_menu_button_present(self):
        self.click_element(self.SEARCH_FIELD)
        return self.is_element_present(self.MENU)


    def open_images_page(self):
        self.click_element(self.MENU)
        self.click_element(self.IMAGES_CATEGORY)


    def verify_url(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.driver.current_url == url


    def open_first_category(self):
        self.click_element(self.FIRST_CATEGORY)
        return self.get_text(self.FIRST_CATEGORY)


    def check_category_name(self, name_of_category):
        return self.get_value(self.SEARCH_FIELD) == name_of_category


    def open_first_image(self):
        self.click_element(self.FIRST_IMAGE)


    def get_image_source(self):
        return self.get_source(self.IMAGE)


    def is_image_opened(self):
        return self.get_element(self.IMAGE)


    def click_button_forward(self):
        self.click_element(self.BUTTON_FORWARD)


    def click_button_back(self):
        self.click_element(self.BUTTON_BACK)


    def is_image_remained_the_same(self, image_src):
        return self.get_image_source() == image_src
