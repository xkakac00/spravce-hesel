from BaseTest import BaseTest
from selenium.webdriver.common.by import By

class TS16(BaseTest):
    def test_edit_passwords_without_servicename(self):
        print("=============================================")
        print("Začíná test T16: Editace hesla – Service user name není vyplněno..")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.fill_text("user_name","DonS")
        self.fill_text("password","P.lb.45_?1!")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/dashboard.php")
        self.click_menu_link("Show all password")
        self.check_url("http://localhost/spravce/public/view_services.php")
        self.edit("edit")
        self.check_url_contains("edit_service.php")
        self.fill_text("service_name","www.seznam.cz")
        self.clear_text("service_user_name")
        self.fill_text("service_user_password","TestPassword")
        self.click_button("input[type='submit']", "error")
        
        
if __name__ == "__main__":
    import unittest
    unittest.main()
