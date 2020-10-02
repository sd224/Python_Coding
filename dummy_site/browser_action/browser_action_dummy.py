from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dummy_site.test_data.data_dummy import *
import logging
import os
from datetime import datetime

logging.basicConfig(filename=os.path.join(LOG_DIR,"master.log"), level=logging.DEBUG,format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

class BrowserAction():
    def __init__(self, browser, wait_time):
        self.browser = browser
        self.spdriver = None
        self.get_spdriver()
        self.wait = WebDriverWait(self.spdriver, wait_time)

    def get_spdriver(self):
        if self.browser == "chrome":
            option_obj = webdriver.ChromeOptions()
            option_obj.headless = headless_execution
            self.spdriver = webdriver.Chrome(executable_path=chrome_driver_path, options=option_obj)
            self.spdriver.maximize_window()
            self.spdriver.implicitly_wait(10)
        elif self.browser == "firefox":
            self.spdriver = webdriver.Firefox(executable_path=firefox_driver_path)
            self.spdriver.maximize_window()
            self.spdriver.implicitly_wait(10)
        elif self.browser == "edge":
            self.spdriver = webdriver.Edge(executable_path=edge_driver_path)
            self.spdriver.maximize_window()
            self.spdriver.implicitly_wait(10)

    def click_element(self,selector):
        element = self.wait.until(EC.presence_of_element_located(selector))
        logger.debug(f"This the element on which click action would be performed : {selector}")
        element.click()

    def input_element(self,selector,value):
        logger.debug(f"This the element on which will put new data : {selector}")
        element = self.wait.until(EC.presence_of_element_located(selector))
        element.clear()
        element.send_keys(value)

    def get_element_text(self, selector):
        element = self.wait.until(EC.presence_of_element_located(selector))
        return element.text

    def take_a_screenshot(self,prefix):
        cur_time = str(datetime.time(datetime.now()))
        current_time = cur_time.replace(":","_").replace(".","_")
        file_name = f"{prefix}_{current_time}.png"
        if os.path.isdir(IMAGE_DIR):
            self.spdriver.save_screenshot(os.path.join(IMAGE_DIR,file_name))
        else:
            os.mkdir(IMAGE_DIR)
            self.spdriver.save_screenshot(os.path.join(IMAGE_DIR,file_name))

