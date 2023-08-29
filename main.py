import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
 
class TravelBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Booking App")

        '''self.destination_var = tk.StringVar(value=list(self.destinations.keys()))
        self.destination_label = tk.Label(root, text="Select Destination:")
        self.destination_label.pack()

        self.destination_menu = tk.OptionMenu(root, self.destination_var, *self.destinations.keys())
        self.destination_menu.pack()

        self.book_button = tk.Button(root, text="Book Now", command=self.book_destination)
        self.book_button.pack()

    def book_destination(self):
        selected_destination = self.destination_var.get()
        if selected_destination in self.destinations:
            price = self.destinations[selected_destination]["price"]
            messagebox.showinfo("Booking Confirmation", f"You've booked {selected_destination} for ${price}. Enjoy your trip!")
        else:
            messagebox.showwarning("Booking Error", "Selected destination not available.")
'''
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
