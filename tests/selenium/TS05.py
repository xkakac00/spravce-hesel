from BaseTest import BaseTest
import logging

class TS05(BaseTest):
    def test_required_fields_fullname_only(self):
        logging.info("=============================================")
        logging.info("Test TS05: Validation of required fields in the form - only FullName is filled in ")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("full_name","Don Salieri")
        self.click_button("input[type='submit']", "error")
        
        
if __name__ == "__main__":
    import unittest
    unittest.main()
