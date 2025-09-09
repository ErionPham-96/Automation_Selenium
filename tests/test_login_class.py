from selenium.webdriver.common.by import By
import time
import csv
from base.base_test import BaseTest as basetest
import pytest

def read_test_login_data(file_path):
    keywords = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            keywords.append((row['username'], row['password']))
    return keywords 

test_login_data = read_test_login_data('./test_data/login_data.csv')

class TestLogin(basetest):
    @pytest.mark.parametrize("username, password", test_login_data)
    def test_login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[contains(@name, 'username')]").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[contains(@name, 'password')]").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
        time.sleep(4)
        check_login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'orangehrm-upgrade-button')]").is_displayed()
        print("Login successful for user:", username)
    