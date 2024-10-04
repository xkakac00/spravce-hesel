from BaseTest import BaseTest
import logging

class TS10(BaseTest):
    def test_add_password(self):
        logging.info("=============================================")
        logging.info("Test T10: Add password - valid data. ")
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
        self.click_button("input[type='submit']", "success")
        
        
        
        
if __name__ == "__main__":
    import unittest
    unittest.main()
