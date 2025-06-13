from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

# https://gist.github.com/TheMuellenator/e131152b991844bb8fae5581c9a8c94e

# keep browser open after script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# satisfy bot detection
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
chrome_options.add_argument("accept-language=en-US,en;q=0.9")
chrome_options.add_argument("referer=https://www.google.com/")
chrome_options.add_argument("upgrade-insecure-requests=1")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Maximize the window
driver.maximize_window()

# need to select English language first
englishselect = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
englishselect.click()



for x in range(0,100000):
    try:
        cookie = driver.find_element(By.CSS_SELECTOR, "button")
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
    except StaleElementReferenceException:
        print("Stale element, retrying...")



#driver.quit() # close all tabs