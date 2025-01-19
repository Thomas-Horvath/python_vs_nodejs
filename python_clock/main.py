import tkinter as tk
from time import strftime

# Ablak létrehozása
root = tk.Tk()
root.geometry('800x600')
root.configure(bg='#222222')
root.title("Digital Clock")

# Óra címke
clock_label = tk.Label(root, font=("Arial", 48), background="#222222", foreground="lime")
clock_label.pack(anchor="center")

# Idő frissítése
def update_clock():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Frissítés 1 másodpercenként

# Indítás
update_clock()
root.mainloop()
