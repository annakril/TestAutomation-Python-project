import unittest
from selenium import webdriver
from test_data.data import DataBase


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(DataBase.executable_path)
        driver = self.driver
        driver.get(DataBase.url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
