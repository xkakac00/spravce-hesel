from BaseTest import BaseTest

class TS09(BaseTest):
    def test_login_no_fields_filled(self):
        print("=============================================")
        print("Začíná test T09: Neplatné přihlášení uživatele ")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.click_button("input[type='submit']", "error")
        
if __name__ == "__main__":
    import unittest
    unittest.main()
