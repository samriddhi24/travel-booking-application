import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
 
class TravelBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Booking App")

if __name__ == "__main__":
    root = tk.Tk()
    root["bg"]="white"
    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("profile-pic.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()
    #app = TravelBookingApp(root)
    root.mainloop()
