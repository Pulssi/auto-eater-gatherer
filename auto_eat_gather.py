import PIL
import pytesseract
import pyautogui
import time
import random
import cv2
import numpy as np

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
eat_until_full = False
clicked = False
next_eleven = False
combat = True
gather = False


while True:
    if(start_combat):
        # FOR COMBAT TRAINING
        
        pyautogui.screenshot("hp.png", region=(190, 85, 115, 30))
        pyautogui.screenshot("food.png", region=(1677, 467, 50, 29))
        time.sleep(1)
        
        # Grayscale hp image
        img = PIL.Image.open('hp.png').convert('L')
        inverted_image = PIL.ImageOps.invert(img)
        inverted_image.save('hp_inverted.png')
        
        # Grayscale food image
        img = PIL.Image.open('food.png').convert('L')
        inverted_image = PIL.ImageOps.invert(img)
        inverted_image.save('food_inverted.png')
        
        #ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)
        
        # Older versions of pytesseract need a pillow image
        # Convert back if needed
        # img = PIL.Image.fromarray(img.astype(np.uint8))

        # Simple image to string
        hp_value = pytesseract.image_to_string(PIL.Image.open('hp_inverted.png'), config='--psm 7 -c tessedit_char_whitelist=0123456789/')
        food_value = pytesseract.image_to_string(PIL.Image.open('food_inverted.png'), config='--psm 7 -c tessedit_char_whitelist=0123456789')
        print("HP: " + hp_value)
        print("FOOD: " + food_value)
        
        try:
            food = int(food_value)
        #    if(food < 2):
        #        print("OUT OF FOOD --> QUITTING")
        #        pyautogui.moveTo(543, 12)
        #        pyautogui.click()
        #        break
        except Exception:
            print("COULDN'T READ THE FOOD VALUE")
        
        try:
            nums = hp_value.split("/")
            hp = int(nums[0])
            #heal_limit = random.randrange(600, 1800)
            sleep_time = random.randrange(2,3)
            if(hp > 2100):
                eat_until_full = False
            if(hp < 2000 or eat_until_full):
                eat_until_full = True
                x_rand = random.randrange(-30, 30)
                y_rand = random.randrange(-30, 30)
                pyautogui.moveTo(1730+x_rand, 520+y_rand)
                pyautogui.click()
                time.sleep(sleep_time)
        except Exception:
            print("COULDN'T READ THE HP VALUE")
   

    elif(start_gather):
        # FOR GATHERING

        pyautogui.screenshot("gather.png", region=(890, 162, 28, 18))
        time.sleep(1)

        # Grayscale image and then invert the colors so the color of numbers go from white to black
        # ORC has trouble recognising white chracters
        img = PIL.Image.open('gather.png').convert('L')
        inverted_image = PIL.ImageOps.invert(img)

        inverted_image.save('new_name.png')
        # ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)
        
        # Older versions of pytesseract need a pillow image
        # Convert back if needed
        # img = Image.fromarray(img.astype(np.uint8))


        # Difficult numbers [2, 11(!!), 43, 44, 63, 64, 84, 91, 94, 97]
        # Empties [2(?), 11]

        # Simple image to string
        gather_value = pytesseract.image_to_string(PIL.Image.open('new_name.png'), config='--psm 7 -c tessedit_char_whitelist=0123456789')
        print(gather_value)
        
        try:
            gather = int(gather_value)
            clicked = False
            if(gather == 10):
                next_eleven = True
            elif(gather > 11):
                next_eleven = False
        #        if(gather > 90):
        #            x_rand = random.randrange(-30, 30)
        #            y_rand = random.randrange(-30, 30)
        #            pyautogui.moveTo(1730+x_rand, 520+y_rand)
        #            pyautogui.click()
        #            time.sleep(3)
        except Exception:
            print("Parse Error")
            if(gather_value == "" and clicked == False and next_eleven == False):
                x_rand = random.randrange(-20, 20)
                y_rand = random.randrange(-20, 20)
                pyautogui.moveTo(965+x_rand, 652+y_rand)
                pyautogui.click()
                
                time.sleep(1+random.random())
                
                x_rand = random.randrange(-20, 20)
                y_rand = random.randrange(-20, 20)
                pyautogui.moveTo(1209+x_rand, 633+y_rand)
                pyautogui.click()
                
                clicked = True
            pass

        '''CHECK MOUSE POSITION'''    

        print(pyautogui.position())
        time.sleep(.5)

    
'''POSITIONS'''

# CLOSE
# 543, 12

# HP BAR    
# 190, 85
# 305, 115

# FOOD_AMOUNT
# 1677, 467
# 1726, 496

# FOOD
# 1730, 520
    
# GATHER BAR
# 890, 162
# 915, 180