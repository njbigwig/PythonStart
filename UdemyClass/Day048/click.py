from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



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


# Maximize the window
driver.maximize_window()

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#article_count.click()

find_link = driver.find_element(By.LINK_TEXT, value ="Wikivoyage")
#find_link.click()

# need to wait for element to be rendered
searchit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search")))
searchit.send_keys("Python", Keys.ENTER)





#driver.quit() # close all tabs