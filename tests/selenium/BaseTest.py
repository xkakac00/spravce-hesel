from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import unittest
import time

class BaseTest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        except WebDriverException as e:
            print("Nastala chyba při inicializace Webdriveru")

    def openurl(self, url):
        self.driver.get(url)
        current_url = self.driver.current_url
        if current_url == url:
            print("Prohlížeč byl otevřen na požadované stránce .... [PASS]")
        else:
            print("Prohlížeč nebyl otevřen na požadované stránce .... [FAIL]")

    def fill_text(self, identifikator, text):
        try:
            element = self.driver.find_element(By.NAME, identifikator)
            element.clear()
            element.send_keys(text)
            time.sleep(1)  # Přidání prodlevy, pro zajištění, že hodnota byla zadaná.
            value = element.get_attribute('value')
            if value == text:
                print(f"Hodnota {text} byla úspěšně zadaná do pole {identifikator} .... [PASS]")
            else:
                print(f"Hodnota {text} NEBYLA zadaná do pole {identifikator} .... [FAIL]")
        except NoSuchElementException:
            print(f"Prvek {identifikator} na stránce nebyl nalezen!")

    
    def click_button(self, name_button, status):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, name_button)
            element.click()
            if name_button=="input[type='reset']":
                print("Bylo stisknuto tlačítko pro vyresetovaní formuláře.")
            elif name_button=="input[type='submit']":
                print("Bylo stisknuto tlačítko pro odeslání formuláře.")
            if status == "none":
                pass
            else:
                success_message = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, status))
                )
                if success_message.is_displayed():
                    print("Text zprávy:", success_message.text)
                else:
                    print("Požadovaná hláška není viditelná!")
        except NoSuchElementException:
            print(f"Prvek {name_button} na stránce nebyl nalezen")


    def check_url(self,expected_url=None):
        current_url=self.driver.current_url
        #print(current_url)
        if expected_url:
            if current_url==expected_url:
                print(f"Kontrola úspěšnosti přesměrování {expected_url} ... [ PASS ]")
            else:
                assert current_url==expected_url, f"Očekávaná URL {expected_url}, ale aktuální url je {current_url}"
        else:
            print(f"Current url:{current_url}")

    def check_url_contains(self,url_substring):
        current_url=self.driver.current_url
        assert url_substring in current_url, f"Očekávaná URL obsahující '{url_substring}', ale aktuální URL je '{url_substring}'"
        print(f"URL obsahuje '{url_substring}' ... [PASS]")

    def click_menu_link(self,link):
        try:
            link_element=self.driver.find_element(By.NAME,link)
            link_element.click()
            print(f"Bylo kliknuto na {link} v menu dashboardu")
        except NoSuchElementException:
            print(f"Odkaz {link} v menu nebyl na stránce nalezen")

    def edit(self,edit_name):
        try:
            element=self.driver.find_element(By.NAME,edit_name)
            element.click()
        except NoSuchElementException:
            print(f"Nelze kliknout na edit link")
    
    def remove(self,remove_name):
        try:
            element=self.driver.find_element(By.NAME,remove_name)
            element.click()
            alert=self.driver.find_element(By.TAG_NAME,"p").text
            print(f"Text zprávy:{alert}")
        except NoSuchElementException:
            print(f"Nelze kliknout na remove link")
    
    

    def verify_changes(self,service_name,service_user_name,service_password):
        service_name_element=self.driver.find_element(By.XPATH, f"//td[text()='{service_name}']")
        service_user_name_element=self.driver.find_element(By.XPATH, f"//td[text()='{service_user_name}']")
        service_password_element=self.driver.find_element(By.XPATH, f"//td[text()='{service_password}']")

         # Ověřit, že všechny elementy byly nalezeny
        assert service_name_element is not None, f"Service name '{service_name}' not found"
        assert service_user_name_element is not None, f"User name '{service_user_name}' not found"
        assert service_password_element is not None, f"Password '{service_password}' not found"

        print(f"Byly zkontrolovány nové upravené záznamy: {service_name}, {service_user_name}, {service_password}")
    
    def clear_text(self,identifikator):
        try:
            element=self.driver.find_element(By.NAME,identifikator)
            element.clear()
            print(f"Byla odstraněna hodnota z {identifikator} ... [PASS]")
        except NoSuchElementException:
            print(f"Prvek {element} nebyl na stránce nalezen ... [FAIL]")
        

    