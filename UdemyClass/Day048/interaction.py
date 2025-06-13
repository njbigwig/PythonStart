from selenium import webdriver
from selenium.webdriver.common.by import By



# keep browser open after script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# satisfy bot detection
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
chrome_options.add_argument("accept-language=en-US,en;q=0.9")
chrome_options.add_argument("referer=https://www.google.com/")
chrome_options.add_argument("upgrade-insecure-requests=1")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count_block = driver.find_element(By.ID, "articlecount")

article_info_counts = article_count_block.find_elements(By.CSS_SELECTOR, "li")

for article_info_count in article_info_counts:
    print(f"{article_info_count.text}")

# by using a single find_element - we only need the first stat, but the order has changed
class_solution = driver.find_elements(By.CSS_SELECTOR, value="div sign-in-modal")
print(f"{class_solution[1].text}")

driver.quit() # close all tabs