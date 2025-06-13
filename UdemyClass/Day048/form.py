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

driver.get("https://secure-retreat-92358.herokuapp.com")

# Maximize the window
driver.maximize_window()

firstnameinput = driver.find_element(By.NAME, value="fName")
firstnameinput.send_keys("Joe")

lastnameinput = driver.find_element(By.NAME, value="lName")
lastnameinput.send_keys("Smith")

emailinput = driver.find_element(By.NAME, value="email")
emailinput.send_keys("hehehe@gmail.com")

signupbutton = driver.find_elements(By.CSS_SELECTOR, value="div .sign-in-modal")
print(signupbutton[0].text)
print(signupbutton[1].text)
#signupbutton.click()

#driver.quit() # close all tabs