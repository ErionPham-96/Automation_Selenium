import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to read keywords form csv file
def read_csv(file_path):
    keywords = []
    with open(file_path, mode = 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            keywords.append(row['keyword'])
    return keywords

# Path to the CSV file
file_path = 'basics/test_data/data_search.csv'

# Main test function
def test_search_keywords():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://www.google.com")
        time.sleep(4)
        # Read keywords from CSV
        keywords = read_csv(file_path)
        
        # Search each keyword and print the first result
        for kw in keywords:
            search_box = driver.find_element(By.XPATH, "//textarea[contains(@name, 'q')]")
            search_box.clear()  # Clear previous input
            search_box.send_keys(kw)  # Input new keyword
            search_box.submit()  # Submit the search form
            time.sleep(4)   # Wait for results to load
            first_result = driver.find_element(By.CSS_SELECTOR, "h3").text
            print(f"Keyword: {kw} -> First result: {first_result}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()