from datetime import datetime
from turtle import width
from webbrowser import BaseBrowser
import requests
from bs4 import BeautifulSoup
import pywhatkit
import pyautogui as pg
import time
import keyboard as k
import config


# url = 'https://www.dictionary.com/e/word-of-the-day/'
url='https://www.britannica.com/dictionary/eb/word-of-the-day'


def get_word_of_the_day():
    """
    Returns the word of the day as a string
    """
    r = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    word = soup.find('span', {'class': 'hw_txt'}).text
    return word

def sendwhatsapp(word):

    
    # pywhatkit.add_driver_path('/Users/masoodahamed/chromedriver')
    # pywhatkit.sendwhatmsg(f'config.mobile_number, "hello{word}, 02, 06, True')
    try:
        time.sleep(5)
        pywhatkit.sendwhatmsg_instantly(config.mobile_number, "hello - test messaging",wait_time=60)
        print('message sent successfully')
    # pywhatkit.sendwhatmsg_instantly(config.mobile_number, "hello - test messaging", 15,True, 4)
    # pg.click()
  
        # pg.press("enter")
    except Exception as e:
        print(e)
        HEIGHT,WIDTH = pg.size()
        print(HEIGHT,WIDTH)
    return  

def pressingenter():
    from selenium import webdriver 
    import config 
    from webbrowser import web


    # from selenium.webdriver.chrome.service import Service
    # chromedriver = config.chromedriver
    # option = webdriver.ChromeOptions()
    # option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    # s = Service(chromedriver)
    # driver = webdriver.Chrome(service=s, options=option)

    xpath_value = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div'
    
    
    # .find_element_by_xpath(xpath_value).click() 
    




if __name__ == '__main__':
    # word = get_word_of_the_day()
    # print(word)
    sendwhatsapp('hello')
    # pressingenter()



