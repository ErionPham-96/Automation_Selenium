from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_find_element():
    
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    try:
        # Opening the URL
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Wait for the page to load
        time.sleep(3)
        # Finding the locator in the webpage
        find_username = driver.find_element(By.XPATH, "//input[@name = 'username']")
        time.sleep(3)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Closing the browser
        driver.quit()
    