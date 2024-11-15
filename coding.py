import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

class AplikasiRekomendasiBuku:
    def __init__(self, root):
        self.root = root
        self.current_user = None
        self.root.title("Aplikasi Rekomendasi Buku")
        self.root.geometry("1000x500")
        
        # data pengguna dari file CSV
        self.user_data_file = 'users.csv'
        if not os.path.exists(self.user_data_file):
            with open(self.user_data_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["username", "password"])
                

        # Memuat data buku
        self.muatan_buku()