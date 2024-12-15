#===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
#Study-Only License
#
#Copyright (c) 2024 KyleGoertzen242
#
#All rights reserved.
#
#This software is provided solely for educational and study purposes. You may not use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the Software. The Software is not intended for production, commercial, or any other practical use.
#
#No permission is granted for any kind of use or redistribution of the Software beyond its intended study purpose. The Software is provided "as is", without any warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claims, damages, or other liabilities, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.
#
#By accessing or using this Software, you agree that you do so at your own risk. If you wish to use, copy, or distribute this Software beyond study purposes, you must obtain explicit written permission from the copyright holder.
#
#Study-Only License
#
#Copyright (c) 2024 KyleGoertzen242
#
#All rights reserved.
#
#This software is provided solely for educational and study purposes. It is not intended for use in production environments, commercial applications, or any other practical usage. The primary goal is to allow users to learn from or experiment with the code in a controlled environment.
#
#You may not use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the Software. Redistribution and use in any form, including modification or derivative works, are strictly prohibited. The Software is not intended for any practical, commercial, or real-world deployment.
#
#The Software is provided "as is," with no warranties or guarantees of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claims, damages, or other liabilities arising from the use of the Software.
#
#By accessing or using this Software, you agree to do so at your own risk. If you wish to use, copy, or distribute the Software for purposes other than study or educational purposes, you must obtain explicit written permission from the copyright holder.
#
#Study-Only License
#
#Copyright (c) 2024 KyleGoertzen242
#
#All rights reserved.
#
#This software is provided solely for educational, research, and study purposes. It is not intended for use in production environments, commercial applications, or any other practical usage. The software is meant as a learning resource, and by using it, you agree to do so solely for study and research. 
#
#You may not use, copy, modify, merge, publish, distribute, sublicense, or sell copies of the Software. Redistribution and usage in any form, including modification or derivative works, are strictly prohibited. The Software is not intended for any practical, commercial, or real-world deployment.
#
#**Purpose**: This code is shared as part of a study or research project and should not be used in production environments. It is provided to allow users to explore and understand the concepts presented within it, but is not suitable for real-world applications.
#
#**No Liability**: The Software is provided "as is," without any warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claims, damages, or other liabilities arising from the use or misuse of the Software.
#
#**Use at Your Own Risk**: By accessing, using, or attempting to modify this software, you agree that you are doing so at your own risk. You are fully responsible for any consequences, errors, or damages that may arise from using this software.
#
#**Restrictions on Use**: If you wish to use, copy, or distribute this Software for any purpose beyond educational, research, or study, you must first obtain explicit written permission from the copyright holder. No rights are granted beyond those specified in this license.
#
#This license applies to the entire repository, including the code, documentation, and any other associated files.
#====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

import pyautogui
import cv2
import numpy as np
import random
import time
import math

def detect_image(template_image_paths):
    best_match_location = None
    best_match_confidence = 0
    
    for template_image_path in template_image_paths:
        template = pyautogui.locateOnScreen(template_image_path)
        
        if template is not None and template[2] * template[3] > best_match_confidence:
            best_match_location = template
            best_match_confidence = template[2] * template[3]

    if best_match_location is not None:
        return best_match_location.left, best_match_location.top, best_match_location.width, best_match_location.height
    else:
        return None

def draw_box(image, x, y, w, h):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

def ease_out_quad(t, b, c, d):
    t /= d
    return -c * t*(t-2) + b

def click_element(location):
    x, y, w, h = location
    target_x = x + w // 2 + random.randint(-1, 2)
    target_y = y + h // 2 + random.randint(-1, 2)
    
    duration = random.uniform(6, 12)
    steps = int(duration)  # 60 steps per second
    
    for i in range(steps):
        t = i / steps
        pyautogui.moveTo(
            ease_out_quad(t, pyautogui.position().x, target_x - pyautogui.position().x, 1),
            ease_out_quad(t, pyautogui.position().y, target_y - pyautogui.position().y, 1),
            duration=0
        )
        time.sleep(1/60)
    pyautogui.click(button='left')

def main():
    template_image_spell = ['spell.png']
    template_image_item = ['item.png']
    template_image_book = ['book.png']
    start_time = time.monotonic()
    
    while True:
        if time.monotonic() - start_time > 90:
            break
            
        if time.monotonic() - start_time > 20:
            book_location = detect_image(template_image_book)
            if book_location is not None:
                click_element(book_location)
                time.sleep(random.uniform(0.029, 0.059))
                click_element(book_location)
                start_time = time.monotonic()
                continue
            
        while True:                
            time.sleep(random.uniform(0.006, 0.0095))
            spell_location = detect_image(template_image_spell)

            if spell_location is not None:
                click_element(spell_location)
                start_time = time.monotonic()
                break
            else:
                if time.monotonic() - start_time > 10:
                    break
                else:
                    continue
        
        while True:
            time.sleep(random.uniform(0.006, 0.0095))
            item_location = detect_image(template_image_item)

            if item_location is not None:
                click_element(item_location)
                start_time = time.monotonic()
                break
            else:
                if time.monotonic() - start_time > 10:
                    break
                else:
                    continue

if __name__ == "__main__":
    main()
