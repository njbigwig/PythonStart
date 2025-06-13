from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Edge()

# keep browser open after script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# satisfy bot detection
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
chrome_options.add_argument("accept-language=en-US,en;q=0.9")
chrome_options.add_argument("referer=https://www.google.com/")
chrome_options.add_argument("upgrade-insecure-requests=1")

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/dp/B09J1TB35S?ref=ppx_yo2ov_dt_b_fed_asin_title")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price is ${price_dollar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="field-keywords")
print(f"{search_bar.tag_name} = {search_bar.get_attribute("placeholder")}")

search_bar2 = driver.find_element(By.ID, value="twotabsearchtextbox")
print(f"{search_bar2.tag_name} = {search_bar2.get_attribute("placeholder")}")

# driver.close() # close active tab

driver.quit() # close all tabs
