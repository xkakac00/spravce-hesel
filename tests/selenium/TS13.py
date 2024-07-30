from BaseTest import BaseTest
from selenium.webdriver.common.by import By

class TS13(BaseTest):
    def test_edit_passwords(self):
        print("=============================================")
        print("Začíná test T13: Editace hesla")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.fill_text("user_name","DonS")
        self.fill_text("password","P.lb.45_?1!")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/dashboard.php")
        self.click_menu_link("Show all password")
        self.check_url("http://localhost/spravce/public/view_services.php")
        self.edit("edit")
        self.check_url("http://localhost/spravce/public/edit_service.php?id=*")
        self.fill_text("service_name","spartapraha")
        self.fill_text("service_user_name","DonSalieri")
        self.fill_text("service_user_password","mistrligy")
        
 


        
        
if __name__ == "__main__":
    import unittest
    unittest.main()
