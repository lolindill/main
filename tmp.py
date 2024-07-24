import tkinter as tk
from tkinter import ttk

class GameDataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Slay The Spire Data Input")
        
        # Create a frame for the form
        form_frame = ttk.Frame(self.root, padding="10")
        form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Define labels and entries for data input
        self.create_label_entry(form_frame, "Player Health:", 0)
        self.create_label_entry(form_frame, "Enemy Health:", 1)
        self.create_label_entry(form_frame, "Player Energy:", 2)
        self.create_label_entry(form_frame, "Enemy Energy:", 3)
        self.create_label_entry(form_frame, "Player Cards:", 4)
        self.create_label_entry(form_frame, "Enemy Cards:", 5)
        self.create_label_entry(form_frame, "Action Taken:", 6)

        # Add buttons for submission and resetting
        self.submit_button = ttk.Button(form_frame, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=7, column=0, pady=10, sticky=(tk.W, tk.E))

        self.reset_button = ttk.Button(form_frame, text="Reset", command=self.reset_form)
        self.reset_button.grid(row=7, column=1, pady=10, sticky=(tk.W, tk.E))
    
    def create_label_entry(self, parent, label_text, row):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, pady=5)
        
        entry = ttk.Entry(parent, width=40)
        entry.grid(row=row, column=1, pady=5)
        
        setattr(self, f"entry_{label_text.replace(' ', '_').replace(':', '')}", entry)
    
    def submit_data(self):
        # Collect data from entries
        data = {
            "Player Health": self.entry_Player_Health.get(),
            "Enemy Health": self.entry_Enemy_Health.get(),
            "Player Energy": self.entry_Player_Energy.get(),
            "Enemy Energy": self.entry_Enemy_Energy.get(),
            "Player Cards": self.entry_Player_Cards.get(),
            "Enemy Cards": self.entry_Enemy_Cards.get(),
            "Action Taken": self.entry_Action_Taken.get(),
        }
        # For demonstration, just print the data
        print("Data submitted:", data)
        # Here you can add code to handle the data (e.g., save to file, send to server, etc.)
    
    def reset_form(self):
        # Clear all entry fields
        for entry in self.root.winfo_children():
            if isinstance(entry, ttk.Entry):
                entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameDataGUI(root)
    root.mainloop()
