import  pyautogui
from datetime import datetime

f = datetime.now()
imagen = str(f.second)+".png"
Screenshot =  pyautogui.screenshot()

Screenshot.save(imagen)