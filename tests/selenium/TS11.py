from BaseTest import BaseTest

class TS11(BaseTest):
    def test_add_password(self):
        print("=============================================")
        print("Začíná test T11: Přidání hesla - s prázdnými poli ")
        print("=============================================")
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
