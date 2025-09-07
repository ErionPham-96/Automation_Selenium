from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_element():
    
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    # Opening the URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Wait for the page to load
    driver.explicit
    # Finding the locator in the webpage
    find_username = driver.find_element(By.XPATH, "//input[@name = 'username']")
    
    # Checking the element is displayed or not
    assert "OrangeHRM" in driver.title
    
    # Closing the browser
    driver.quit()
    