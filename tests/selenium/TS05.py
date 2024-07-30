from BaseTest import BaseTest

class TS05(BaseTest):
    def test_required_fields_fullname_only(self):
        print("=============================================")
        print("Začíná test TS05: Validace povinných polí ve formuláři - vyplněno pouze FullName ")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("full_name","Don Salieri")
        self.click_button("input[type='submit']", "error")

if __name__ == "__main__":
    import unittest
    unittest.main()
