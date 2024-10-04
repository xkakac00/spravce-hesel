from BaseTest import BaseTest
from selenium.webdriver.common.by import By
import logging

class TS12(BaseTest):
    def test_add_password_reset(self):
        logging.info("=============================================")
        logging.info("Test TS12:Add password - reset form")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.fill_text("user_name","DonS")
        self.fill_text("password","P.lb.45_?1!")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/dashboard.php")
        self.click_menu_link("Add password")
        self.check_url("http://localhost/spravce/public/add_service.php")
        self.fill_text("service_name","Facebook")
        self.fill_text("service_user_name","DonS_F")
        self.fill_text("service_user_password","123456")
        self.click_button("input[type='reset']", "none")
        
        service_name=self.driver.find_element(By.NAME,"service_name").get_attribute('value')
        service_user_name=self.driver.find_element(By.NAME,"service_user_name").get_attribute('value')
        service_user_password=self.driver.find_element(By.NAME,"service_user_password").get_attribute('value')
        
        if service_name=='' and service_user_name=='' and service_user_password == '':
            logging.info("Values in the form have been deleted.... [PASS]")
        else:
            logging.error("The values in the form have not been deleted..... [FAIL]")

    
        
if __name__ == "__main__":
    import unittest
    unittest.main()
