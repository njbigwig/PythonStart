import internetspeedtwitterbot
import time

PROMISED_DOWN = 2000
PROMISED_UP = 300
CHROME_DRIVER_PATH = "?"




mybot = internetspeedtwitterbot.InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

for attempts in range(1,2):
    mybot.get_internet_speed()
    mybot.tweet_at_provider()
    time.sleep(30)
    
mybot.closewindows()

