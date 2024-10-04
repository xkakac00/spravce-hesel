from BaseTest import BaseTest
import logging

class TS07(BaseTest):
    def test_required_fields_fullname_only(self):
        logging.info("=============================================")
        logging.info("Test TS07: Validation of required fields in the form - only Password is filled in ")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("password", "P.lb.45_?1!")
        self.click_button("input[type='submit']", "error")
        
if __name__ == "__main__":
    import unittest
    unittest.main()
