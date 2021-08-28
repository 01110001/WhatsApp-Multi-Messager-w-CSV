import pandas
import webbrowser
import pyautogui
import time
message=". I hope you are doing well! I'm planning to change my number to 90_5554443322, please also add my new number. See you later :)"
file=pandas.read_csv("testInput.csv",error_bad_lines=False)
Data=file.to_dict('list')
webbrowser.open("https://")
for i in range(len(Data['Name'])):
    webbrowser.open("https://web.whatsapp.com/send?phone="+Data['Number'][i]+"&text="+"Hello, "+Data['Name'][i]+message)
    time.sleep(8)
    pyautogui.press('enter')
    time.sleep(7)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'w')
