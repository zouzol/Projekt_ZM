import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import notatnik
import tkintermapview


# ======= Listy danych ==========
tereny = []
punkty = []
pracownicy = []

root = tk.Tk()
root.title("System zarządzania terenami zalewowymi i punktami monitoringu")
root.geometry('1400x800')

notebook = ttk.Notebook(root)
frame_teren = Frame(notebook)
frame_punkt = Frame(notebook)
frame_pracownik = Frame(notebook)
notebook.add(frame_teren, text="Tereny zalewowe")
notebook.add(frame_punkt, text="Punkty monitoringu")
notebook.add(frame_pracownik, text="Pracownicy")
notebook.pack(expand=1, fill='both')