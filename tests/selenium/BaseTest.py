from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException,TimeoutException
from datetime import datetime
import unittest
import logging
import argparse


actual_time=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logging.basicConfig(filename=f"Logs/test_log_{actual_time}.log",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BaseTest(unittest.TestCase):

    # Class Attributes
    MAX_RETRIES=3
   
    def setUp(self):
        parser = argparse.ArgumentParser(description="Choose browser type")
        parser.add_argument('--typ_browser',type=str,help="Broser type:Firefox, Chrome,Edge",default="Firefox")
        args, unknown = parser.parse_known_args()
        self.browser=args.typ_browser

        attempt = 0

        while attempt < self.MAX_RETRIES:
          try:
              if self.browser == "Firefox":
                  self.driver = webdriver.Firefox()
                  self.driver.maximize_window()
                  logging.info("Web driver - Firefox - initialization successful ... [PASS]")
                  break
              elif self.browser == "Chrome":
                  self.driver = webdriver.Chrome()
                  self.driver.maximize_window()
                  logging.info("Web driver - Chrome - initialization successful ... [PASS]")
                  break
              elif self.browser == "Edge":
                  self.driver = webdriver.Edge()
                  self.driver.maximize_window()
                  logging.info("Web driver - Edge - initialization successful ... [PASS]")
                  break
              else:
                  logging.error("We dont support this browser ... [FAIL]")
          except WebDriverException as e:
              logging.error(f"It was detected fail with initialization webdriver ... [FAIL] {str(e)}")
              attempt = attempt + 1

              if attempt == self.MAX_RETRIES:
                  self.fail("Browser initialization failed after 3 attempts")
          
    def openurl(self, url):
        try:
            self.driver.get(url)
            current_url = self.driver.current_url
            if current_url == url:
                logging.info("The browser was opened on the requested page.... [PASS]")
            else:
                logging.error(f"The browser was not opened on the requested page .... [FAIL]")
                self.fail(f"Expected URL:{url}, found URL:{current_url}")
        except WebDriverException as e:
            logging.error(f"Failure with initializing webdriver ... [FAIL] {str(e)}")
            self.fail(f"Failed to open URL: {str(e)}")

    def fill_text(self, identifikator, text):
        try:
            element = self.driver.find_element(By.NAME, identifikator)
            element.clear()
            element.send_keys(text)
            value = element.get_attribute('value')
            if value == text:
                logging.info(f"The value {text} was successfully written to the  {identifikator} field .... [PASS]")
            else:
                logging.error(f"The value {text} WAS NOT written to the {identifikator} field .... [FAIL]")
        except NoSuchElementException as e:
            logging.error(f"The element {identifikator} was not found on the page !... [FAIL] {str(e)}")

    def click_button(self, name_button, status):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, name_button)
            element.click()
            if name_button=="input[type='reset']":
                logging.info("The button to reset the form has been pressed... [PASS]")
            elif name_button=="input[type='submit']":
                logging.info("The button to submit the form has been pressed... [PASS]")
            if status == "none":
                pass
            else:
                success_message = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, status))
                )
                if success_message.is_displayed():
                    logging.info(f"Text message: {success_message.text}")
                else:
                    logging.error("The required message is not visible!")
        except NoSuchElementException:
            logging.error(f"Element {name_button} not found on the page.")


    
    def check_url(self,expected_url=None):
        current_url=self.driver.current_url
        #print(current_url)
        if expected_url:
           if current_url == expected_url:
             logging.info(f"Redirect success check {expected_url} ... [PASS]")
           else:
                logging.error(f"Expected URL: {expected_url}, but found URL: {current_url} ... [FAIL]")
                self.fail(f"Expected URL: {expected_url}, but found URL: {current_url}")
        else:
            logging.error(f"Current url:{current_url}")

    def check_url_contains(self,url_substring):
        current_url=self.driver.current_url
        assert url_substring in current_url, f"Expected URL containing '{url_substring}', but the actual URL is '{url_substring}'"
        logging.info(f"URL contains '{url_substring}' ... [PASS]")

    def click_menu_link(self,link):
        try:
            link_element=self.driver.find_element(By.NAME,link)
            link_element.click()
            logging.info(f"The {link} in the dashboard menu was clicked... [PASS]")
        except NoSuchElementException:
            logging.error(f"The {link} in the menu was not found on the page ... [FAIL]")

    def edit(self,edit_name):
        try:
            element=self.driver.find_element(By.NAME,edit_name)
            element.click()
            logging.info("I can click on the edit link ... [PASS]")
        except NoSuchElementException:
            logging.error("Can't click on the edit link ... [FAIL]")
    
    def remove(self,remove_name):
        try:
            element=self.driver.find_element(By.NAME,remove_name)
            element.click()
            alert=self.driver.find_element(By.TAG_NAME,"p").text
            logging.info(f"Text message:{alert}")
        except NoSuchElementException:
            logging.error(f"Can't click on the remove link ... [FAIL]")
    
    

    def verify_changes(self,service_name,service_user_name,service_password):
        service_name_element=self.driver.find_element(By.XPATH, f"//td[text()='{service_name}']")
        service_user_name_element=self.driver.find_element(By.XPATH, f"//td[text()='{service_user_name}']")
        service_password_element=self.driver.find_element(By.XPATH, f"//td[text()='{service_password}']")

         # Ověřit, že všechny elementy byly nalezeny
        assert service_name_element is not None, f"Service name '{service_name}' not found"
        assert service_user_name_element is not None, f"User name '{service_user_name}' not found"
        assert service_password_element is not None, f"Password '{service_password}' not found"

        logging.info(f"ew amended records have been checked:{service_name}, {service_user_name}, {service_password}")
    
    def clear_text(self,identifikator):
        try:
            element=self.driver.find_element(By.NAME,identifikator)
            element.clear()
            logging.info(f"The value from {identifikator} ... [PASS]")
        except NoSuchElementException:
            logging.error(f"The element {identifikator} was not found on the page ... [FAIL]")
        

    def tearDown(self):
        if hasattr(self,'driver'):
            self.driver.quit()
            logging.info("Web driver successfully closed... [PASS]")