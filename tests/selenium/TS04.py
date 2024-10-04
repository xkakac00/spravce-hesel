from BaseTest import BaseTest
import logging

class TS04(BaseTest):
    def test_register_required_fields(self):
        logging.info("=============================================")
        logging.info("Test TS04: Validation of mandatory form fields begins. ")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.click_button("input[type='submit']", "error")
        

if __name__ == "__main__":
    import unittest
    unittest.main()
