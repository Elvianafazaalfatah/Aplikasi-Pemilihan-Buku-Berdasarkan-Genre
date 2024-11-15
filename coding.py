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
        
        
        # Halaman selamat datang
        self.halaman_awal = tk.Frame(self.root)
        self.halaman_awal.pack(fill="both", expand=True)

        label_selamat_datang = tk.Label(self.halaman_awal, text="Selamat datang di Aplikasi Pemilihan Buku Berdasarkan Genre\nSilahkan pilih opsi pencarian buku", font=("Arial", 12))
        label_selamat_datang.pack(pady=10)

        tombol_mulai = tk.Button(self.halaman_awal, text="Mulai", command=self.buka_halaman_login)
        tombol_mulai.pack(pady=10)
        
        # Halaman Sign Up dan Login
        self.halaman_login = tk.Frame(self.root)

        label_login = tk.Label(self.halaman_login, text="Masukkan akun anda", font=("Arial", 12))
        label_login.pack(pady=10)

        tk.Label(self.halaman_login, text="Username:").pack(pady=5)
        self.username_entry_login = tk.Entry(self.halaman_login)
        self.username_entry_login.pack(pady=5)

        tk.Label(self.halaman_login, text="Password:").pack(pady=5)
        self.password_entry_login = tk.Entry(self.halaman_login, show="*")
        self.password_entry_login.pack(pady=5)

        tk.Button(self.halaman_login, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.halaman_login, text="Sign Up", command=self.buka_halaman_signup).pack(pady=5)