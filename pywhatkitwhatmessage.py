def sendwhatsapp(newword):
    import pywhatkit
    import time
    import config
    import pyautogui as pg

    try:
        time.sleep(5)
        actual_word = newword
        
        # pywhatkit.sendwhatmsg(f'config.mobile_number, "hello", 02, 06, True')
        pywhatkit.sendwhatmsg_instantly(config.mobile_number, actual_word)
        print('message sent successfully')
    except Exception as e:
        print(e)
        HEIGHT,WIDTH = pg.size()
        print(HEIGHT,WIDTH)
    return  

sendwhatsapp('hello')