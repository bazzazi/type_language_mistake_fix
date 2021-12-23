###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #

# Developer: Mohammad Ali Bazzazi (me)

########################### START ###########################

import pyautogui, pyperclip
from pynput.keyboard import Listener

def change(key):

    persian = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیئ؟"
    english = "Hhf\je[]ponbvcCsawqxzuytr;'glk,idm?"

    TranslateTable1 = str.maketrans(english, persian)
    TranslateTable2 = str.maketrans(persian,english)

    if str(key) == "Key.f8":
        print('done')
        pyautogui.hotkey('ctrl', 'x') # cut text
        text = pyperclip.paste()
        if text.isascii():
            NewText = text.translate(TranslateTable1)
        else:
            NewText = text.translate(TranslateTable2)
        
        pyperclip.copy(NewText)
        pyautogui.hotkey('ctrl', 'v')

with Listener(on_release=change) as listener:
    listener.join()
    
########################### END ###########################
