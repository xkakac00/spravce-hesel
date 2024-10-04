from BaseTest import BaseTest
import logging

class TS11(BaseTest):
    def test_add_password(self):
        logging.info("=============================================")
        logging.info("Test TS11: Adding a password - with empty fields")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.fill_text("user_name","DonS")
        self.fill_text("password","P.lb.45_?1!")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/dashboard.php")
        self.click_menu_link("Add password")
        self.check_url("http://localhost/spravce/public/add_service.php")
        self.click_button("input[type='submit']", "error")
        
        
        
        
if __name__ == "__main__":
    import unittest
    unittest.main()
