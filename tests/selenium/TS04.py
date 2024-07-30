from BaseTest import BaseTest

class TS04(BaseTest):
    def test_register_required_fields(self):
        print("=============================================")
        print("Začíná test TS04: Validace povinných polí ve formuláři. ")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.click_button("input[type='submit']", "error")
      

if __name__ == "__main__":
    import unittest
    unittest.main()
