from BaseTest import BaseTest

class TS07(BaseTest):
    def test_required_fields_fullname_only(self):
        print("=============================================")
        print("Začíná test TS07: Validace povinných polí ve formuláři - vyplněno pouze Password ")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("password", "P.lb.45_?1!")
        self.click_button("input[type='submit']", "error")

if __name__ == "__main__":
    import unittest
    unittest.main()
