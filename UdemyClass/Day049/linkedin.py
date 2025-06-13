from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time


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


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4175131997&distance=25&f_AL=true&f_SB2=6&geoId=90000091&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

# Maximize the window
driver.maximize_window()

time.sleep(5)

logintype = driver.find_elements(By.CSS_SELECTOR, value="div .sign-in-modal")
for login in logintype:
    if login.text == "Sign in":
        login.click()
        
time.sleep(5)

firstname_input = driver.find_element(By.ID, "base-sign-in-modal_session_key")
firstname_input.send_keys("blah@blah.com")

password_input = driver.find_element(By.ID, "base-sign-in-modal_session_password")
password_input.send_keys("blah")

sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-id='sign-in-form__submit-btn']")
sign_in_button.click()

time.sleep(5)

job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")

for job in job_listings:
    
    print(job.text)
    try:
        job.click()
        time.sleep(2)
        
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-save-button"))
            #EC.element_to_be_clickable((By.CSS_SELECTOR, "button.save-job-button"))
        )
        save_button.click()
    except Exception as e:
        print(f"Error: {e}")




#driver.quit() # close all tabs