import keyboard
import time
def esc():
    keyboard.press('esc')  # Первое нажатие
    keyboard.release('esc')
    time.sleep(0.1)  # Небольшая пауза между нажатиями
    keyboard.press('esc')  # Второе нажатие
    keyboard.release('esc')

language = input('Choose language (RU/EN):').lower()
if language == 'ru':
    button = input('Привет, эта программа создана для макроса на дабл escape на Miside, нажми одну кнопку, на которую хочешь привязать бинд, и нажимай Enter. \nВведи кнопку здесь (Если это специфичная клавиша по типу Tab , пиши именно "tab" и т.д с такими кнопками)-> ').lower()
    print('''
    Скрипт активирован! 
    Теперь при нажатии будет сразу прожиматься дабл Escape
    Как только он тебе не будет  , закрывай его.
    Скрипт сделан:
    Discord: angel_internet
    Telegram: @OMG_KawaiiAngelChan
    ''')
    while True:
        event = keyboard.read_event()  
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == button:
                esc()
elif language == 'en':
    button = input('Hello, this program is created for a macros for Miside, click one button on which you need to bind, and press Enter. \n Enter the button here (If this a special button for example Tab then write "Tab" and etc. for this buttons)-> ').lower()
    print('''
    Script activated! 
    Now you will press hotkey -> double Escape will immediately be pressed
    As soon as you don't need it, close this program
    Script maded by:
    Discord: angel_internet
    Telegram: @OMG_KawaiiAngelChan
    ''')
    while True:
        event = keyboard.read_event()  
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == button:
                esc()
else:
    print('Wrong language')

