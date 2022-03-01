from datetime import datetime
from email import header
from email.mime import image
from webbrowser import BaseBrowser
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import pywhatkit
import pyautogui as pg
import time
import keyboard as k
import config
import pandas as pd
import os
import json


class wordwhatsapp():
    def __init__(self):
        url='https://www.britannica.com/dictionary/eb/word-of-the-day'
        headers = {'UserAgent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'}
        r = requests.get(url, headers=headers)  
        
        self.soup = BeautifulSoup(r.text, 'html.parser')

  
    

    def extractword(self):
        word = self.soup.find('span', {'class': 'hw_txt'}).text
        
        definition = self.soup.find('div', {'class': 'midbs'}).text


        wordimage = self.soup.find('div', {'class': 'wod_img_act'})
        title = self.soup.find('div', {'class': 'wod_img_tit'}).text
        wordimage = wordimage.find('img')
        wordimage=wordimage.get('src')



        word_definition = {
                'word': word + '\n', 
                'definition': definition + '\n',
                'image_value':wordimage + '\n',
                'title': title + '\n'
                }
        for item in word_definition:
            word_definition[item].replace('[]', '')

        df = pd.DataFrame(word_definition, index=[1])
        dict_val= df.to_dict()
        
        word_definition = dict_val
        return word_definition

    def wordperday(self, word_definition):
        
        word_definition['word'][1]
        word_definition['definition'][1].replace('\n [noncount] [count, noncount]', '')

        stword = ['[count, noncount]','\n','[noncount]','[]']
        querywords = word_definition['definition'][1].split()

        resultwords  = [word for word in querywords if word.lower() not in stword]
        result = ' '.join(resultwords)

        import re
        meaning = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", result)
        meaning = meaning.replace('[]', '')
        meaning = meaning.replace('()', '')
        
    

        self.newlist = []
        self.newlist.append(word_definition['word'][1])
        self.newlist.append(f'{meaning} "\n"')
        self.newlist.append(word_definition['image_value'][1])
        self.newlist.append(word_definition['title'][1])

        return self.newlist  

    def sendwhatsapp(self,newword):
    
        try:
            time.sleep(5)
            actual_word = newword
            actual_word = ''.join(actual_word)

            pywhatkit.sendwhatmsg_instantly(config.mobile_number, actual_word)
        except Exception as e:
            print(e)
        return  



newobjectword = wordwhatsapp()
word_value = newobjectword.extractword()
print('this is from the dictionary  ', word_value)
newword = newobjectword.wordperday(word_value)
newobjectword.sendwhatsapp(newword)
        
        
        

