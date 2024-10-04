from BaseTest import BaseTest
import logging

class TS06(BaseTest):
    def test_required_fields_fullname_only(self):
        logging.info("=============================================")
        logging.info("Test TS06:Validation of mandatory form fields - only UserName is filled in ")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("user_name","DonS")
        self.click_button("input[type='submit']", "error")
        

if __name__ == "__main__":
    import unittest
    unittest.main()
