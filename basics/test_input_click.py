from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_input_click():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    try:
        # Opening the URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        
        # Finding the locator in the webpage and clicking and sending input
        find_username = driver.find_element(By.XPATH, "//input[@name='username']")
        find_username.send_keys("Admin")
        find_password = driver.find_element(By.XPATH, "//input[@name='password']")
        find_password.send_keys("admin123")
        
        # Clicking the login button
        find_login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        find_login_button.click()
        
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Closing the browser
        driver.quit()
        