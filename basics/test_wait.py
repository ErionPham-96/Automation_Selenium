from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wait():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    try:
        # Open the webpage
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        # Wait for the username field to be present
        wait = WebDriverWait(driver, 10)
        find_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]')))
        print("Element found:", find_element)
    finally:
        # Close the browser
        driver.quit()
