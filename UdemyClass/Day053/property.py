import requests
import os
from bs4 import BeautifulSoup
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

entry_form_url = "XXXXxxx"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

fake_zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

# Write your code below this line 
response = requests.get(url=fake_zillow_url, headers=header)
response.encoding = "utf-8"
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
print(soup.title.getText())
#print(soup.prettify())

property_list = soup.find_all(class_="StyledPropertyCardDataWrapper")

zillow_list = []

for property in property_list:
    #print(property.prettify())
    property_url = property.find(name="a")
    property_address = property.find('address', {'data-test': 'property-card-addr'})
    property_rent = property.find(class_="PropertyCardWrapper__StyledPriceLine")
    
    #print(property_url.get("href"))
    property_url_string = property_url.get("href")
    
    address_text = property_address.getText(strip=True)
     
    address_parts1 = address_text.split("|")
    address_parts2 = address_text.split(",", 1)
    if len(address_parts1) > 1:
        #print(address_parts1[1].strip())
        property_address_string = address_parts1[1].strip() 
    elif len(address_parts2) > 1:
        #print(address_parts2[1].strip())
        property_address_string = address_parts2[1].strip() 
        
    rent_string = property_rent.getText(strip=True)
    property_rent_string = ""
    
    for r in rent_string:
        if r == "$" or (r >= "0" and r <= "9"):
            property_rent_string += r
    
    #print(property_rent_string)
    print(f"Updating list: {property_url_string}|{property_address_string}|{property_rent_string}")
    zillow_list.append((property_url_string, property_address_string, property_rent_string))
            
    
    print("\n")
 
# access entry form 

print(f"Property List Size: {len(zillow_list)}")

for property_listing in zillow_list:
    print(property_listing) 
           
    # keep browser open after script ends
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True) 
        
    driver = webdriver.Chrome(options=chrome_options)  
        
    print("Calling Get")
    driver.get(entry_form_url)
        
    time.sleep(2)  
    
    addr_field = driver.find_elements(By.XPATH, "//input[@class='whsOnd zHQkBf']")[0]
    addr_field.send_keys(property_listing[1])
    
    rent_field = driver.find_elements(By.XPATH, "//input[@class='whsOnd zHQkBf']")[1]
    rent_field.send_keys(property_listing[2])
    
    link_field = driver.find_elements(By.XPATH, "//input[@class='whsOnd zHQkBf']")[2]
    link_field.send_keys(property_listing[0])    
            
    # click Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "span.NPEfkd.RveJvd.snByac")
    submit_button.click()
                 

    # Maximize the window
    #driver.maximize_window()  
    
    driver.quit()
    
    
        
        
 