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
        
        # Halaman Sign Up
        self.halaman_signup = tk.Frame(self.root)
        
        label_signup = tk.Label(self.halaman_signup, text="Sign Up", font=("Arial", 12))
        label_signup.pack(pady=10)

        tk.Label(self.halaman_signup, text="Username:").pack(pady=5)
        self.username_entry_signup = tk.Entry(self.halaman_signup)
        self.username_entry_signup.pack(pady=5)

        tk.Label(self.halaman_signup, text="Password:").pack(pady=5)
        self.password_entry_signup = tk.Entry(self.halaman_signup, show="*")
        self.password_entry_signup.pack(pady=5)

        tk.Button(self.halaman_signup, text="Sign Up", command=self.signup).pack(pady=5)
        tk.Button(self.halaman_signup, text="Kembali ke Login", command=self.buka_halaman_login).pack(pady=5)
        
        # Halaman pemilihan jumlah genre
        self.halaman_pilihan_genre = tk.Frame(self.root)
        
        label_pilihan_genre = tk.Label(self.halaman_pilihan_genre, text="Pilih Metode Pencarian Buku Berdasarkan Genre", font=("Arial", 12))
        label_pilihan_genre.pack(pady=10)

        self.tombol_satu_genre = tk.Button(self.halaman_pilihan_genre, text="Cari Buku Berdasarkan Satu Genre", command=self.buka_halaman_satu_genre)
        self.tombol_satu_genre.pack(pady=5)

        self.tombol_dua_genre = tk.Button(self.halaman_pilihan_genre, text="Cari Buku Berdasarkan Dua Genre", command=self.buka_halaman_dua_genre)
        self.tombol_dua_genre.pack(pady=5)
        
        # Area untuk menampilkan rekomendasi terdahulu
        self.area_hasil_terdahulu = tk.Text(self.halaman_pilihan_genre, wrap="word", height=10, width=50)
        self.area_hasil_terdahulu.pack(pady=10)
        self.area_hasil_terdahulu.config(state="disabled")

        # Halaman pencarian satu genre
        self.halaman_satu_genre = tk.Frame(self.root)
        self.label_genre1 = tk.Label(self.halaman_satu_genre, text="Pilih Genre:")
        self.label_genre1.pack(pady=5)

        self.kombobox_genre1 = ttk.Combobox(self.halaman_satu_genre, values=self.genres)
        self.kombobox_genre1.pack(pady=5)

        self.tombol_rekomendasi1 = tk.Button(self.halaman_satu_genre, text="Rekomendasikan Buku", command=self.rekomendasi_buku_satu_genre)
        self.tombol_rekomendasi1.pack(pady=10)

        self.area_hasil1 = tk.Text(self.halaman_satu_genre, wrap="word", height=10, width=40)
        self.area_hasil1.pack(pady=10)
        self.area_hasil1.config(state="disabled")

        self.tombol_kembali1 = tk.Button(self.halaman_satu_genre, text="Kembali", command=self.kembali_ke_pilihan_genre)
        self.tombol_kembali1.pack(pady=5)
        
        self.tombol_selesai1 = tk.Button(self.halaman_satu_genre, text="Selesai", command=self.buka_halaman_terima_kasih)
        self.tombol_selesai1.pack(pady=5)
