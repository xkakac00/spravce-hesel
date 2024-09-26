from BaseTest import BaseTest
import logging

class TS02(BaseTest):

    def test_register_existing_user(self):
        logging.info("=============================================")
        logging.info("Test TS02: Registering an existing user to the system begins")
        logging.info("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("full_name", "DonSalieri")
        self.fill_text("user_name", "DonS")
        self.fill_text("password", "P.lb.45_?1!")
        self.click_button("input[type='submit']", "error")
        self.close_session()

if __name__ == "__main__":
    import unittest
    unittest.main()
