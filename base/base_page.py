from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import DEFAULT_TIMEOUT

class BasePage:
    
    def __init__(self, driver, timeout = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def find(self, locator):
        # Find an element in the DOM
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        # Wait until the element is clickable in the DOM and UI then click it
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def type(self, locator, text):
        self.find(locator).send_keys(text)
        
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_and_click(self, locator):
        element = self.find(locator)
        self.scroll_into_view(element)
        element.click()
    
    def is_selected(self, locator):
        element = self.find(locator)
        return element.is_selected()
    
    # def assert_success(self, timeout=12):
        # Wait for any toast to appear
        WebDriverWait(self.driver, timeout, 0.2).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'oxd-toast')]"))
        )
        # Merge all toasts text
        toasts = self.driver.find_elements(By.XPATH, "//div[contains(@class,'oxd-toast')]")
        texts = [t.text.strip() for t in toasts if t.text.strip()]
        ok = any(("Success" in txt) or ("Successfully" in txt) for txt in texts)
        assert ok, f"Toast found but not success. Found: {texts}"