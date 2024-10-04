from BaseTest import BaseTest
from selenium.webdriver.common.by import By
import logging

class TS18(BaseTest):
    def test_remove_password(self):
        logging.info("=============================================")
        logging.info("Test T18: Password Removal begins")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.fill_text("user_name","DonS")
        self.fill_text("password","P.lb.45_?1!")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/dashboard.php")
        self.click_menu_link("Remove passwords")
        self.check_url("http://localhost/spravce/public/delete_service.php")
        self.remove("remove")
        
        
if __name__ == "__main__":
    import unittest
    unittest.main()
