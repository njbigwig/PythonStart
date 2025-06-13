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

driver.get("https://www.python.org/")

# could have found Class = "medium-widget event-widget last"
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

group_blocks = driver.find_elements(By.CLASS_NAME, value="shrubbery")

event_dictionary = {}

for group_block in group_blocks:
    section_blocks = group_block.find_elements(By.CLASS_NAME, value="widget-title")

    for section_block in section_blocks:
        if section_block.text == "Upcoming Events":
            print("Found Upcoming Events:")
            eventdates = group_block.find_elements(By.TAG_NAME, value="time")
            eventnames = group_block.find_elements(By.TAG_NAME, value="a")
            
            for idx in range(0,len(eventdates)):
                event_dictionary[str(idx)] = {"time": eventdates[idx].text, "name": eventnames[idx+1].text}
                #print(f"{idx} {eventdates[idx].text} {eventnames[idx+1].text}")
            
            print(event_dictionary)
            # for eventdate in eventdates:
            #     print(eventdate.text)
                
            # for eventname in eventnames:
            #     print(eventname.text)  
   

driver.quit() # close all tabs