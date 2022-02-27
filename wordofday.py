from datetime import datetime
from email.mime import image
from webbrowser import BaseBrowser
import requests
from bs4 import BeautifulSoup
import pywhatkit
import pyautogui as pg
import time
import keyboard as k
import config
import pandas as pd
import os



def extractword():
    url='https://www.britannica.com/dictionary/eb/word-of-the-day'

    r = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    word = soup.find('span', {'class': 'hw_txt'}).text
    definition = soup.find('div', {'class': 'midbs'}).text

        

    word_definition = {
            'word': word, 
            'definition': definition
            }

    df = pd.DataFrame(word_definition, index=[1])

    dict_val= df.to_dict()
    # word_definition ={
    #     'word': {1: 'precipitation'}, 
    #     'definition': {1: '\n\n\n\n1 [noncount] : water that falls to the ground as rain, snow, etc.\n\n\n\n\n\n\nThe weather forecast calls for some sort of frozen precipitation tomorrow—either snow or sleet.\n\na 50 percent chance of precipitation\n\n\n\n\n\n\n\n\n2 [count, noncount] technical : the process of separating a solid substance from a liquid\n\n\n\n\n\n\nMinerals are separated from the seawater by precipitation.\n\n\n\n\n\n'}
    #     }

    word_definition = dict_val
    return word_definition

def wordperday(word_definition):
    word_definition['word'][1]
    word_definition['definition'][1].replace('\n [noncount] [count, noncount]', '')

    stword = ['[count, noncount]','\n','[noncount]','[]']
    querywords = word_definition['definition'][1].split()

    resultwords  = [word for word in querywords if word.lower() not in stword]
    result = ' '.join(resultwords)

    import re
    meaning = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", result)

    newilst = []
    newilst.append(word_definition['word'][1])
    newilst.append(meaning)

    return newilst

def sendwhatsapp(newword):
 
    try:
        time.sleep(5)
        actual_word = newword
        actual_word = ''.join(actual_word)

        pywhatkit.sendwhatmsg_instantly(config.mobile_number, actual_word)
    except Exception as e:
        print(e)
    return  



if __name__ == '__main__':
    word_value = extractword()
    newword = wordperday(word_value)
    sendwhatsapp(newword)



