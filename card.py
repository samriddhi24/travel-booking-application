import tkinter as tk

class CardLayoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Layout Example")
        
        self.cards = []  # List to hold card frames
        self.current_card = 0
        
        # Creating card frames
        i=0
        card_frame = tk.Frame(self.root, width=300, height=200, bg=f'#{i}{i}{i}')
        card_frame.grid(row=0, column=i, padx=10, pady=10)
        self.cards.append(card_frame)
        card_frame.grid_remove()  # Hide all card frames initially
        
        self.cards[self.current_card].grid()  # Show the first card
        
        self.button_next = tk.Button(self.root, text="Next", command=self.show_next_card)
        self.button_next.grid(row=1, column=0, pady=10)

    def show_next_card(self):
        # Hide the current card
        self.cards[self.current_card].grid_remove()
        
        # Show the next card (looping back to the first if at the end)
        self.current_card = (self.current_card + 1) % len(self.cards)
        self.cards[self.current_card].grid()

if __name__ == "__main__":
    root = tk.Tk()
    app = CardLayoutApp(root)
    root.mainloop()