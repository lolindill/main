import tkinter as tk
from tkinter import ttk

class DataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slay The Spire Data Entry")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Create and place labels and entry fields for data collection
        ttk.Label(self.root, text="Player Health:").grid(column=0, row=0, padx=10, pady=5)
        self.player_health = tk.DoubleVar()
        ttk.Entry(self.root, textvariable=self.player_health).grid(column=1, row=0, padx=10, pady=5)
        
        ttk.Label(self.root, text="Enemy Health:").grid(column=0, row=1, padx=10, pady=5)
        self.enemy_health = tk.DoubleVar()
        ttk.Entry(self.root, textvariable=self.enemy_health).grid(column=1, row=1, padx=10, pady=5)
        
        ttk.Label(self.root, text="Player Energy:").grid(column=0, row=2, padx=10, pady=5)
        self.player_energy = tk.DoubleVar()
        ttk.Entry(self.root, textvariable=self.player_energy).grid(column=1, row=2, padx=10, pady=5)
        
        ttk.Label(self.root, text="Action Chosen:").grid(column=0, row=3, padx=10, pady=5)
        self.action_chosen = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.action_chosen).grid(column=1, row=3, padx=10, pady=5)

        # Submit button
        self.submit_button = ttk.Button(self.root, text="Submit", command=self.submit_data)
        self.submit_button.grid(column=1, row=4, padx=10, pady=10)
    
    def submit_data(self):
        # Retrieve data from the fields
        data = {
            'player_health': self.player_health.get(),
            'enemy_health': self.enemy_health.get(),
            'player_energy': self.player_energy.get(),
            'action_chosen': self.action_chosen.get()
        }
        
        # Save or process the data here
        print(data)  # For now, just print the data. Replace with actual data handling code.

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryApp(root)
    root.mainloop()
