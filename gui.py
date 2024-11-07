import tkinter as tk
from tkinter import messagebox
import requests

def register():
    username = username_entry.get()
    password = password_entry.get()
    response = requests.post('http://127.0.0.1:3000/api/signup', json={'username': username, 'password': password})
    if response.status_code == 201:
        messagebox.showinfo("Success", "User registered successfully")
    else:
        messagebox.showerror("Error", response.text)

def login():
    username = username_entry.get()
    password = password_entry.get()
    response = requests.post('http://127.0.0.1:3000/api/login', json={'username': username, 'password': password})
    if response.status_code == 200:
        balance = response.json().get('balance')
        messagebox.showinfo("Success", f"Login successful. Balance: {balance}")
    else:
        messagebox.showerror("Error", response.text)

root = tk.Tk()
root.title("Banking App")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Register", command=register).pack()
tk.Button(root, text="Login", command=login).pack()

root.mainloop()
