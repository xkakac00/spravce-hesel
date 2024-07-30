from BaseTest import BaseTest

class TS02(BaseTest):

    def test_register_existing_user(self):
        print("=============================================")
        print("Začíná test TS02: Registrace existujího uživatele do systému")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("full_name", "DonSalieri")
        self.fill_text("user_name", "DonS")
        self.fill_text("password", "P.lb.45_?1!")
        self.click_button("input[type='submit']", "error")

if __name__ == "__main__":
    import unittest
    unittest.main()
