import sys
import tkinter as tk
from tkinter import ttk
import webbrowser
import subprocess
import pickle
from tkinter import scrolledtext

from bs4 import BeautifulSoup
import requests


class MinimalBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minimal Browser")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        style = ttk.Style()
        style.configure("TNotebook", background="white")
        style.configure("TFrame", background="white")
        style.configure("TLabel", background="white")
        style.configure("TButton", background="white")
        style.configure("TEntry", background="white")
        style.configure("Text", background="white")

        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="Search")

        self.search_label = ttk.Label(self.search_tab, text="Search:")
        self.search_label.pack()

        self.search_bar = ttk.Entry(self.search_tab, width=50)
        self.search_bar.pack()

        self.search_button = ttk.Button(self.search_tab, text="Search", command=self.navigate_to_url)
        self.search_button.pack()

        self.recommended_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.recommended_tab, text="Recommended")

        self.recommended_label = ttk.Label(self.recommended_tab, text="Recommended:")
        self.recommended_label.pack()

        self.youtube_button = ttk.Button(self.recommended_tab, text="YouTube", command=self.open_youtube)
        self.youtube_button.pack()

        self.music_button = ttk.Button(self.recommended_tab, text="Yandex.Music", command=self.open_yandex_music)
        self.music_button.pack()

        self.spotify_button = ttk.Button(self.recommended_tab, text="Spotify", command=self.open_spotify)
        self.spotify_button.pack()

        self.wikipedia_button = ttk.Button(self.recommended_tab, text="Wikipedia", command=self.open_wikipedia)
        self.wikipedia_button.pack()
        
        self.google_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.google_tab, text="Google")

        self.google_label = ttk.Label(self.google_tab, text="Google search:")
        self.google_label.pack()

        self.google_bar = ttk.Entry(self.google_tab, width=50)
        self.google_bar.pack()

        self.google_button = ttk.Button(self.google_tab, text="Search", command=self.navigate_to_google)
        self.google_button.pack()

        self.bing_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.bing_tab, text="Bing")

        self.bing_label = ttk.Label(self.bing_tab, text="Bing search:")
        self.bing_label.pack()

        self.bing_bar = ttk.Entry(self.bing_tab, width=50)
        self.bing_bar.pack()

        self.bing_button = ttk.Button(self.bing_tab, text="Search", command=self.navigate_to_bing)
        self.bing_button.pack()

        self.history_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.history_tab, text="History")

        self.search_history = tk.Listbox(self.history_tab, width=50, height=20)
        self.search_history.pack()

        self.clear_history_button = ttk.Button(self.history_tab, text="Clear history", command=self.clear_history)
        self.clear_history_button.pack()

        self.settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text="Settings")

        self.settings_label = ttk.Label(self.settings_tab, text="Settings:")
        self.settings_label.pack()

        self.clear_history_var = tk.IntVar()
        self.clear_history_checkbox = ttk.Checkbutton(self.settings_tab, text="Clear history on exit", variable=self.clear_history_var)
        self.clear_history_checkbox.pack()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        try:
            with open("history.pkl", "rb") as f:
                self.search_history.insert(tk.END, *pickle.load(f))
        except FileNotFoundError:
            pass

    def navigate_to_url(self):
        url = self.search_bar.get()
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url
        webbrowser.open_new_tab(url)
        self.search_history.insert(tk.END, url)
        self.search_history.see(tk.END)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Searching...")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, soup.title.string)
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Error: " + str(e))

    def navigate_to_google(self):
        url = self.google_bar.get()
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url
        webbrowser.open_new_tab(url)
        self.search_history.insert(tk.END, url)
        self.search_history.see(tk.END)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Searching...")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, soup.title.string)
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Error: " + str(e))

    def navigate_to_bing(self):
        url = self.bing_bar.get()
        if not url.startswith("http"):
            url = "https://www.bing.com/search?q=" + url
        webbrowser.open_new_tab(url)
        self.search_history.insert(tk.END, url)
        self.search_history.see(tk.END)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Searching...")
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, soup.title.string)
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Error: " + str(e))

    def open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com/")

    def open_yandex_music(self):
        webbrowser.open_new_tab("https://music.yandex.ru/")

    def open_spotify(self):
        webbrowser.open_new_tab("https://www.spotify.com/")

    def open_wikipedia(self):
        webbrowser.open_new_tab("https://www.wikipedia.org/")

    def clear_history(self):
        self.search_history.delete(0, tk.END)

    def on_closing(self):
        if self.clear_history_var.get():
            self.clear_history()
        else:
            with open("history.pkl", "wb") as f:
                pickle.dump(list(self.search_history.get(0, tk.END)), f)
        self.destroy()
root = MinimalBrowser()
root.protocol("WM_DELETE_WINDOW", root.on_closing)

required_libs = ["requests", "beautifulsoup4"]

for lib in required_libs:
    try:
        __import__(lib)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

root.mainloop()


