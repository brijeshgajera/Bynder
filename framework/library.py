from selenium import webdriver
from data.config import settings
from urllib.parse import urljoin


class CommonClass:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CommonClass()
        return cls.instance

    def __init__(self):

        if str(settings['browser']).lower() is "firefox":
            self.driver = webdriver.Firefox()
        elif str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome("../data/chromedriver.exe")
        else:
            self.driver = webdriver.Chrome("../data/chromedriver.exe")
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def getElement(self, element_type, path):
        if element_type == "xpath":
            search_field = self.driver.find_element_by_xpath(path)
        elif element_type == "id":
            search_field = self.driver.find_element_by_id(path)
        elif element_type == "class":
            search_field = self.driver.find_element_by_class_name(path)
        elif element_type == "name":
            search_field = self.driver.find_element_by_name(path)
        return search_field

    def input_text(self, element_type, path, value):
        search_field = self.getElement(element_type, path)
        search_field.send_keys(value)

    def input_click(self, element_type, path):
        search_field = self.getElement(element_type, path)
        search_field.click()

    def login(self, element_type, path, assert_value="", error_message=""):
        get_url = self.driver.current_url
        if assert_value in get_url:
            print("Successfully Logged In")
        else:
            search_field = self.getElement(element_type, path)
            search_field = search_field.text
            if error_message in search_field:
                print("Login Failed : " + search_field)



    def logout(self):
        self.input_click("xpath", "//a[contains(@class,'admin-dropdown profile')]")
        self.input_click("xpath","//button[@type='submit'][contains(.,'Logout')]")
