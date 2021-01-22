from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        self.driver.find_element_by_css_selector(".js-start-test").click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_css_selector(".download-speed").text)
        self.up = float(self.driver.find_element_by_css_selector(".upload-speed").text)


    def tweet_at_provider(self, login, password, paid_up, paid_down):
        self.driver.get("https://www.twitter.com/login/")
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        pwd = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(login)
        pwd.send_keys(password)
        pwd.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {paid_down}down/{paid_up}up"
        tweet_block = self.driver.find_element_by_css_selector(".public-DraftStyleDefault-block")
        tweet_block.send_keys(tweet)
        tweet_block.send_keys(Keys.ENTER)
