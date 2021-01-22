from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH_HERE"
TWITTER_EMAIL = "YOUR_EMAIL_HERE"
TWITTER_PWD = "YOUR_PWD_HERE"

TWITTER_LOGIN_URL = "https://twitter.com/login/"

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
print(f"up speed {bot.up}\ndown speed {bot.down}")
bot.tweet_at_provider(login=TWITTER_EMAIL, password=TWITTER_PWD, paid_up=PROMISED_UP, paid_down=PROMISED_DOWN)
