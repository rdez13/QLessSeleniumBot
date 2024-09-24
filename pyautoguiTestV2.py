import pyautogui
import time



x,y = pyautogui.locateCenterOnScreen("newTab.png", confidence= 0.9)
print(x,y)
#print(pyautogui.size())
#while True:
 #   print (pyautogui.position())
  #  time.sleep(1)



#popup to take input
channelName = pyautogui.prompt(text="", title="Enter channel name")
time.sleep(1)
pyautogui.moveTo(x/2,y/2, 1)
pyautogui.click()
#opens new tab
pyautogui.hotkey("command", "t")
#searches youtube
pyautogui.write("https://youtube.com/")
#clicks enter
pyautogui.hotkey("return")
time.sleep(3)
x1,y1 = pyautogui.locateCenterOnScreen("searchPic1.png", confidence=0.8)
pyautogui.moveTo(x1/2,y1/2)
time.sleep(1)
pyautogui.click()
pyautogui.write(channelName)
pyautogui.hotkey("return")
