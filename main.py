import pyautogui as pt
import time
import pyperclip
# import randomrt 


# TO get the message from the chat

def get_received_message()->str:
    global x,y
    
    position = pt.locateOnScreen('Capture.PNG',confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y,duration=1) 
    
    pt.tripleClick(509,628,duration=1)
    pt.hotkey('ctrl', 'c')
    message = pyperclip.paste()  
    return message.strip()

def respose_message(message:str):
    #   pt.moveTo(559,736)
    pt.leftClick(535,697,duration=1)
    if message.lower() == "hmm":
        response = "Hmmm"
    if message.lower() == "hi":
        response = "Hello"
    if message.lower() == "hello":
        response = "Hi"    
    elif message.lower() == "ok":
        response = "Tula bolach nahiye ka ?"
    elif message.lower() == "good night":
        response = "Good night !"
    elif message.lower() == "good morning":
        response = "Good morning"
    else:
        response = message
    pyperclip.copy(response) 
    pt.hotkey('ctrl', 'v')
    pt.hotkey('enter')
    

def check_messages():
    position = pt.locateOnScreen('2.JPG',confidence=0.8)
    if position: 
        x = position[0]
        y = position[1]
        pt.moveTo(x,y,duration=1)
        pt.leftClick()
        return True
    else:
        return False
              
if __name__=="__main__":
    time.sleep(3)
    
    position1 = pt.locateOnScreen("Capture.PNG", confidence=0.8)
    
    x   = position1[0]
    y   = position1[1]
    while True:
        if check_messages():
            received_message        = get_received_message()  
            time.sleep(2)
            respose_message(received_message)
        else:
            time.sleep(5)
            
