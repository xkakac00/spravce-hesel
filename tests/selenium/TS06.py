from BaseTest import BaseTest

class TS06(BaseTest):
    def test_required_fields_fullname_only(self):
        print("=============================================")
        print("Začíná test TS06: Validace povinných polí ve formuláři - vyplněno pouze UserName ")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("user_name","DonS")
        self.click_button("input[type='submit']", "error")

if __name__ == "__main__":
    import unittest
    unittest.main()
