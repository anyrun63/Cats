from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://dog.ceo/api/breeds/image/random"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img #чтобы мусорщик не убрал
    window.mainloop()
