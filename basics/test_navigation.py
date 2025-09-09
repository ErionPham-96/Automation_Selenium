from selenium import webdriver

def test_navigation():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    
    try:
        # Navigate to a webpage
        driver.get('https://www.google.com')
        print('Page title is:', driver.title)
        
        # Test forward, back, and refresh navigation
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        print('Navigated to OrangeHRM, title is:', driver.title)
        driver.back()
        print('Went back, title is:', driver.title)
        driver.forward()
        print('Went forward, title is:', driver.title)
        driver.refresh()
        print('Page refreshed, title is:', driver.title)
        
    finally:
        # Close the browser
        driver.quit()