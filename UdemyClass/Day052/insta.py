from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# this is just going to get me banned....
  
print("Creating Chome Options")
        
# keep browser open after script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

print("Calling Webdriver")
driver = webdriver.Chrome(options=chrome_options)  
        
print("Calling Get")
driver.get("https://www.instagram.com/")
        
time.sleep(10)            

# Maximize the window
print("Maximizing Window")
driver.maximize_window()    


# driver.quit() # close all tabs  
       
        
