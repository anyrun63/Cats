from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from bottle import response


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status() #для обработки исключений
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img  # чтобы мусорщик не убрал

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

update_button = Button(text="Обновить", command=set_image)
update_button.pack()

url = "https://dog.ceo/api/breeds/image/random"
img = load_image(url)
set_image()

window.mainloop()
