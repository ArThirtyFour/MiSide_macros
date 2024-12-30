from time import sleep
from pynput.mouse import Listener ,Button
from pystyle import Write , Colors , Colorate
from mouse_keyboard import check_mouse , button_macros
from logo import vivod_ascii

spisok = {
    'left' : Button.left,
    'right' : Button.right,
    'middle' : Button.middle,
    'm1' : Button.x1,
    'm2' : Button.x2
}

vivod_ascii()
language = Write.Input("Choose language (RU/EN):", Colors.purple_to_blue, interval=0).lower()
if language == 'ru':



    button = Write.Input('''
Привет, эта программа создана для макроса на дабл escape на Miside
нажми одну кнопку, на которую хочешь привязать бинд, и нажимай Enter.
Если хочешь на клавишу мыши , то пиши для таких клавиш следующее
left - левая
right - правая
middle - колесико
и m1 и т.д для доп.кнопок мыши
А если просто клавишу на клавиатуре , просто пиши ее (Если это специфичная клавиша по типу Tab , пиши именно "tab" и т.д с такими кнопками)
Поле для ввода клавиши ->''', Colors.purple_to_blue, interval=0).lower()
    print(Colorate.Horizontal(Colors.purple_to_blue , '''
    Скрипт активирован! 
    Теперь при нажатии будет сразу прожиматься дабл Escape
    Как только он тебе не будет  , закрывай его.
    Скрипт сделан:
    Discord: angel_internet
    Telegram: @OMG_KawaiiAngelChan
    ''', 1 ))
    if button in spisok.keys():
        button = spisok[button]
        check_mouse(button)
    else:
        button_macros(button)
        



elif language == 'en':
    button = Write.Input('''
Hello, this program is created for the double escape macro on Miside
Click one button to which you want to attach a bind and press Enter.
If you want to use a mouse key, then write the following for such keys:
left - left button
right - right button
middle - wheel 
and m1, etc. for additional mouse buttons
And if it’s just a key on the keyboard, just write it (If it’s a specific key like Tab, write “tab”, etc. with such buttons)
Key input field ->''', Colors.purple_to_blue, interval=0).lower()
    print(Colorate.Horizontal(Colors.purple_to_blue , '''
    Script activated! 
    Now you will press hotkey -> double Escape will immediately be pressed
    As soon as you don't need it, close this program
    Script maded by:
    Discord: angel_internet
    Telegram: @OMG_KawaiiAngelChan
    ''',1))
    if button in spisok.keys():
        button = spisok[button]
        check_mouse(button)
    else:
        button_macros(button)
else:
    print(Colorate.Horizontal(Colors.purple_to_blue , 'Wrong language. Please rewrite again!',1))
    sleep(5)

