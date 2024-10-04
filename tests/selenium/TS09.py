from BaseTest import BaseTest
import logging

class TS09(BaseTest):
    def test_login_no_fields_filled(self):
        logging.info("=============================================")
        logging.info("Test T09: Invalid user login begins ")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/login.php")
        self.click_button("input[type='submit']", "error")
     
        
if __name__ == "__main__":
    import unittest
    unittest.main()
