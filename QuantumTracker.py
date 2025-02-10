import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
import os
import json

class QuantumTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("QuantumTracker - Theme Customizer")
        self.root.geometry("400x300")

        self.theme_data = {}
        self.load_themes()

        self.create_widgets()

    def create_widgets(self):
        self.theme_label = tk.Label(self.root, text="Choose a Theme to Apply:")
        self.theme_label.pack(pady=10)

        self.theme_listbox = tk.Listbox(self.root)
        self.theme_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.update_theme_list()

        self.apply_button = tk.Button(self.root, text="Apply Theme", command=self.apply_theme)
        self.apply_button.pack(pady=5)

        self.customize_button = tk.Button(self.root, text="Create/Customize Theme", command=self.customize_theme)
        self.customize_button.pack(pady=5)

    def load_themes(self):
        if os.path.exists("themes.json"):
            with open("themes.json", "r") as file:
                self.theme_data = json.load(file)

    def save_themes(self):
        with open("themes.json", "w") as file:
            json.dump(self.theme_data, file, indent=4)

    def update_theme_list(self):
        self.theme_listbox.delete(0, tk.END)
        for theme in self.theme_data:
            self.theme_listbox.insert(tk.END, theme)

    def apply_theme(self):
        selected_theme = self.theme_listbox.get(tk.ACTIVE)
        if selected_theme:
            theme_colors = self.theme_data[selected_theme]
            self.root.config(bg=theme_colors.get("bg", "#FFFFFF"))
            messagebox.showinfo("Theme Applied", f"Applied theme: {selected_theme}")

    def customize_theme(self):
        new_theme_name = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if new_theme_name:
            bg_color = colorchooser.askcolor(title="Choose Background Color")[1]
            if bg_color:
                self.theme_data[os.path.basename(new_theme_name)] = {"bg": bg_color}
                self.save_themes()
                self.update_theme_list()
                messagebox.showinfo("Theme Created", f"Created new theme: {os.path.basename(new_theme_name)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumTracker(root)
    root.mainloop()