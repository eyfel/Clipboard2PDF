import tkinter as tk
from PIL import ImageGrab, Image
import pytesseract
import os
import time
import keyboard
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_screenshot(image):
    text = pytesseract.image_to_string(image)
    kod = ""
    for line in text.split('\n'):
        if 'KOD' in line:
            kod = line.split(':')[-1].strip()
            break

    output_dir = r'C:\Users\a\OneDrive\Masaüstü\dxf2pdf'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'{kod}.pdf')
    image.save(output_path, 'PDF', resolution=100.0)
    print(f'Saved: {output_path}')

def take_screenshot():
    pyautogui.hotkey('win', 'shift', 's')

def check_clipboard():
    last_image = None
    root = tk.Tk()
    root.withdraw()

    while True:
        try:
            clipboard_image = ImageGrab.grabclipboard()

            if clipboard_image and clipboard_image != last_image:
                print("New screenshot detected")
                process_screenshot(clipboard_image)
                last_image = clipboard_image

            time.sleep(0.2)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(0.2)

keyboard.add_hotkey('<', take_screenshot)

check_clipboard()
