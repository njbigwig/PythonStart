from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

SPEED_TEST_DELAY = 60

TWITTER_EMAIL = "hehehe@gmail.com"
TWITTER_PASSWORD = "XXXXXXXXXXXXX"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.up = 0
        self.down = 0
        
        print("Creating Chome Options")
        
        # keep browser open after script ends
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        # satisfy bot detection
        # self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
        # self.chrome_options.add_argument("accept-language=en-US,en;q=0.9")
        # self.chrome_options.add_argument("referer=https://www.google.com/")
        # self.chrome_options.add_argument("upgrade-insecure-requests=1")
        # self.chrome_options.add_argument("--ssl-version-max=tls1.2")
        self.chrome_options.add_argument("--ignore-certificate-errors")        
        
        print("Calling Webdriver")
        self.driver = webdriver.Chrome(options=self.chrome_options)  
        
        print("Calling Get")
        self.driver.get("https://www.speedtest.net/")
        
        time.sleep(10)            

        # Maximize the window
        print("Maximizing Window")
        self.driver.maximize_window()      
       
        
    def get_internet_speed(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, value="start-text") 
        print(f"Found {len(buttons)} elements")
         
        for button in buttons:
            
            if button.text == "GO":
                print("Clicking GO to start...")
                button.click()   
                 
        time.sleep(SPEED_TEST_DELAY) 
        print("Test results ready!")
        
        self.driver.switch_to.default_content()
        
        
        self.down = int(float(self.driver.find_element(By.CLASS_NAME, "download-speed").text))
        print(f"DL: {self.down}")
        
        self.up = int(float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text))
        print(f"UL: {self.up}")      
        
    
    
    def tweet_at_provider(self):
        print("Calling Webdriver")
        twitter_driver = webdriver.Chrome(options=self.chrome_options)  
        
        print("Calling Get")
        twitter_driver.get("https://www.x.com")
        
        time.sleep(10)            

        # Maximize the window
        print("Maximizing Window")
        twitter_driver.maximize_window() 
        
        time.sleep(10)  
        
        print("Clicking X.com Sign in button")
        sign_in_button = twitter_driver.find_element(By.XPATH, "//span[text()='Sign in']")
        print(f"{sign_in_button.text}")
        sign_in_button.click()
        
        # wait for the user name field and send data
        print("Waiting to enter X.com email")
        username_field = WebDriverWait(twitter_driver, 20).until(EC.element_to_be_clickable((By.NAME, "text")))
        username_field.send_keys(TWITTER_EMAIL)
        
        # click Next button
        print("Clicking X.com Next button")
        next_button = twitter_driver.find_element(By.XPATH, "//span[text()='Next']")
        next_button.click()
        
        # need to confirm name
        # print("Confirming X.com user name")
        # input_field = twitter_driver.find_element(By.CLASS_NAME, "r-30o5oe")
        # input_field.send_keys("xxxxxxx")
        # time.sleep(5)  
        
        # wait for the password field and send data
        password_field = WebDriverWait(twitter_driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
        password_field.send_keys(TWITTER_PASSWORD)
        
        # click the login button
        login_button = twitter_driver.find_element(By.XPATH, "//span[text()='Log in']")
        login_button.click()
        
        # Post
        print("Getting side menu post")
        post_button = WebDriverWait(twitter_driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='SideNav_NewTweet_Button']")))
        post_button.click()
        
        time.sleep(5)
        
        xfinity_post = f"@XfinitySupport Gigabit X2 promises 2100/300, getting {self.down}/{self.up}, cannot change speeds on your website, come on!"
   
        print(f"Adding text to my post {xfinity_post}")
        tweet_box = twitter_driver.find_element("xpath", "//div[@data-testid='tweetTextarea_0']")
        tweet_box.click()
        tweet_box.send_keys(xfinity_post + Keys.RETURN)   
        
        time.sleep(5)
        
        print("Post it!!!!!")
        post_button = twitter_driver.find_element("xpath", "//span[text()='Post']")
        post_button.click()

    
    def closewindows(self):
        self.driver.quit() # close all tabs
        