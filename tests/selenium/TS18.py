from BaseTest import BaseTest
from selenium.webdriver.common.by import By

class TS18(BaseTest):
    def test_remove_password(self):
        print("=============================================")
        print("Začíná test T18: Odstranění hesla")
        print("=============================================")
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
