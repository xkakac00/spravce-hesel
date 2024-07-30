from BaseTest import BaseTest

class TS08(BaseTest):
    def test_login_valid_user(self):
        print("=============================================")
        print("Začíná test TS08: Přihlášení uživatele. ")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.fill_text("user_name","DonS")
        self.fill_text("password","P.lb.45_?1!")
        self.click_button("input[type='submit']", "none")
        self.check_url("http://localhost/spravce/public/dashboard.php")
if __name__ == "__main__":
    import unittest
    unittest.main()
