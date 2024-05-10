import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        self.label = tk.Label(master, text="Enter city:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.button.pack()

    def get_weather(self):
        # Fetch weather information here
        city = self.entry.get()
        # Call function to fetch weather using API and display it
        messagebox.showinfo("Weather Info", f"Display weather info for {city}")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
