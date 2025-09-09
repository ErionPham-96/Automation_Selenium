from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

def read_test_login_data(file_path):
    keywords = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            keywords.append((row['username'], row['password']))
    return keywords

test_login_data = read_test_login_data('./tests/test_data/login_data.csv')

def test_login(username, password):
    driver = webdriver.Chrome()
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[contains(@name, 'username')]").send_keys(username)
        driver.find_element(By.XPATH, "//input[contains(@name, 'password')]").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
        time.sleep(4)
        check_login = driver.find_element(By.XPATH, "//button[contains(@class, 'orangehrm-upgrade-button')]").is_displayed()
        print("Login successful for user:", username)
    except Exception as e:
        print("Login failed for user:", username, "Error:", e)
    finally:
        driver.quit()
if __name__ == "__main__":
    for username, password in test_login_data:
        test_login(username, password)