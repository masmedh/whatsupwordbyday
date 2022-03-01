from pywhatkit import sendwhatmsg
from wordofday import *

class newimage(wordwhatsapp):
    def __init__(self):
        pass

    def wordperday(self, word_definition):
        self.word_definition = word_definition

        #This belwo one works as well
        # super(newimage, self).wordperday(word_definition) 
        
        super().wordperday(word_definition) #This works as well therefore either 
        #above or this statement can be used to call the super function

        word_definition['image_value'][1] = 'masood'
        self.newlist[2]=word_definition['image_value'][1]
        self.newlist[3]='another word masood'

        
        return self.newlist



parentclass = wordwhatsapp()
word_value = parentclass.extractword()
# print('this is from the dictionary  ', word_value)

newchildclass = newimage()
newword = newchildclass.wordperday(word_value)
print(newword)
parentclass.sendwhatsapp(newword)
