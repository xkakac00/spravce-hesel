from BaseTest import BaseTest
from selenium.webdriver.common.by import By

class TS03(BaseTest):
    def test_reset_button(self):
        print("=============================================")
        print("Začíná test TS03: Resetování formuláře.")
        print("=============================================")
        self.openurl("http://localhost/spravce/public/register.php")
        self.fill_text("full_name", "DonSalieri")
        self.fill_text("user_name", "DonS")
        self.fill_text("password", "P.lb.45_?1!")
        self.click_button("input[type='reset']","none")
        
        fullname=self.driver.find_element(By.NAME,"full_name").get_attribute('value')
        username=self.driver.find_element(By.NAME,"user_name").get_attribute('value')
        password=self.driver.find_element(By.NAME,"password").get_attribute('value')
        
        if fullname=='' and username=='' and password == '':
            print ("Hodnoty ve formuláři byly smazané.... [PASS]")
        else:
            print("Hodnoty smazané ve formuláři nebyly.... [FAIL]")


if __name__ == "__main__":
    import unittest
    unittest.main()
