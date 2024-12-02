import pandas as pd
import tkinter as tk
from tkinter import Tk, Label, ttk, Frame, Button, messagebox
from PIL import Image, ImageTk
import csv
import os

class AplikasiRekomendasiBuku:
    def _init_(self, root):
        self.root = root
        self.current_user = None
        self.root.title("Aplikasi Rekomendasi Buku")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.root.resizable(True, True) 
        
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
        
        # Memuat dan mengatur gambar latar belakang
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        bg_awal = Image.open("tubes2/resource/halaman utama.png")
        bg_awal = bg_awal.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_awal = ImageTk.PhotoImage(bg_awal)
        
        self.canvas_awal = tk.Canvas(self.halaman_awal, width=screen_width, height=screen_height)
        self.canvas_awal.pack(fill="both", expand=True)
        self.canvas_awal.create_image(0,0, image=self.bg_image_awal, anchor="nw")
        
        # Tambahkan bayangan untuk tombol
        shadow_x1 = screen_width // 2 - 10
        shadow_y1 = screen_height - 295
        shadow_x2 = screen_width // 2 + 185
        shadow_y2 = shadow_y1 + 55
        self.canvas_awal.create_oval(shadow_x1, shadow_y1, shadow_x2, shadow_y2, fill="#995a3a", outline="")  # Bayangan tombol

        # Tambahkan tombol berbentuk oval
        oval_width = 200  # Lebar oval
        oval_height = 50  # Tinggi oval
        button_x1 = (screen_width // 2 + 80) - (oval_width // 2)  # Posisi kiri oval
        button_y1 = screen_height - 300  # Posisi atas oval
        button_x2 = (screen_width // 2 + 80) + (oval_width // 2)  # Posisi kanan oval
        button_y2 = button_y1 + oval_height  # Posisi bawah oval

        # Gambar oval
        self.oval_button = self.canvas_awal.create_oval(button_x1, button_y1, button_x2, button_y2, fill="white", outline="")

        # Tambahkan teks di tengah oval
        self.canvas_awal.create_text((button_x1 + button_x2) // 2, (button_y1 + button_y2) // 2, text="Mulai", font=("Courier", 20, "bold"), fill="#995a3a")

        self.canvas_awal.tag_bind(self.oval_button, "<Enter>", lambda event: self.canvas_awal.itemconfig(self.oval_button, fill="#fdb899"))
        self.canvas_awal.tag_bind(self.oval_button, "<Leave>", lambda event: self.canvas_awal.itemconfig(self.oval_button, fill="#ffffff"))
        self.canvas_awal.tag_bind(self.oval_button, "<Button-1>", lambda event: self.buka_halaman_login())
        
        # Halaman Sign Up dan Login
        self.halaman_login = tk.Frame(self.root)
        
        bg_login = Image.open("tubes2/resource/halaman login.png")
        bg_login = bg_login.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_login = ImageTk.PhotoImage(bg_login)
        
        self.canvas_login = tk.Canvas(self.halaman_login, width=screen_width, height=screen_height)
        self.canvas_login.pack(fill="both", expand=True)
        self.canvas_login.create_image(0,0, image=self.bg_image_login, anchor="nw")
        
        self.label_login = tk.Label(self.halaman_login, text="Masukkan akun anda", font=("Courier", 20, "bold"), bg="#ffeeea", fg="#ff8b67")
        self.canvas_login.create_window(screen_width // 2, screen_height // 2 - 400, window=self.label_login)

        self.label_username = tk.Label(self.halaman_login, text="Username:", font=("Courier", 15, "bold"), bg="#ffeeea", fg="#ff8b67")
        self.canvas_login.create_window(screen_width // 2, screen_height // 2 - 360, window=self.label_username)
        
        self.username_entry_login = tk.Entry(self.halaman_login)
        self.canvas_login.create_window(screen_width // 2, screen_height // 2 - 320, window=self.username_entry_login)

        self.label_password = tk.Label(self.halaman_login, text="Password:", font=("Courier", 15, "bold"), bg="#ffeeea", fg="#ff8b67")
        self.canvas_login.create_window(screen_width // 2, screen_height // 2 - 280, window=self.label_password)
        
        self.password_entry_login = tk.Entry(self.halaman_login, show="*")
        self.canvas_login.create_window(screen_width // 2, screen_height // 2 - 240, window=self.password_entry_login)

        self.button_login = tk.Button(self.halaman_login, text="Log in", font=("Courier", 12, "bold"), command=self.login)
        self.canvas_login.create_window(screen_width // 2, screen_height // 2 - 190, window=self.button_login)
        
        self.button_signup = tk.Button(self.halaman_login, text="Sign up", font=("Courier", 12, "bold"), command=self.buka_halaman_signup)
        self.canvas_login.create_window(screen_width // 2, screen_height // 2 - 140, window=self.button_signup)
    
        self.button_login.bind("<Enter>", lambda event: self.button_login.config(bg="#dc5765"))
        self.button_login.bind("<Leave>", lambda event: self.button_login.config(bg="#ffffff"))
        self.button_signup.bind("<Enter>", lambda event: self.button_signup.config(bg="#dc5765"))
        self.button_signup.bind("<Leave>", lambda event: self.button_signup.config(bg="#ffffff"))
        
        # Halaman Sign Up
        self.halaman_signup = tk.Frame(self.root)
        
        bg_signup = Image.open("tubes2/resource/halaman signup.png")
        bg_signup = bg_signup.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_signup = ImageTk.PhotoImage(bg_signup)
        
        self.canvas_signup = tk.Canvas(self.halaman_signup, width=screen_width, height=screen_height)
        self.canvas_signup.pack(fill="both", expand=True)
        self.canvas_signup.create_image(0,0, image=self.bg_image_signup, anchor="nw")
        
        self.label_signup = tk.Label(self.halaman_signup, text="Sign up", font=("Courier", 20, "bold"), bg="#ffeeea", fg="#ff8b67")
        self.canvas_signup.create_window(screen_width // 2, screen_height // 2 - 400, window=self.label_signup)

        self.label_signup_username = tk.Label(self.halaman_signup, text="Username:", font=("Courier", 15, "bold"), bg="#ffeeea", fg="#ff8b67")
        self.canvas_signup.create_window(screen_width // 2, screen_height // 2 - 360, window=self.label_signup_username)
        
        self.username_entry_signup = tk.Entry(self.halaman_signup)
        self.canvas_signup.create_window(screen_width // 2, screen_height // 2 - 320, window=self.username_entry_signup)
    
        self.label_signup_pass = tk.Label(self.halaman_signup, text="Password:", font=("Courier", 15, "bold"), bg="#ffeeea", fg="#ff8b67")
        self.canvas_signup.create_window(screen_width // 2, screen_height // 2 - 280, window=self.label_signup_pass)
        
        self.password_entry_signup = tk.Entry(self.halaman_signup, show="*")
        self.canvas_signup.create_window(screen_width // 2, screen_height // 2 - 240, window=self.password_entry_signup)
        
        self.button_sign_up = tk.Button(self.halaman_signup, text="Sign up", font=("Courier", 12, "bold"), command=self.signup)
        self.canvas_signup.create_window(screen_width // 2, screen_height // 2 - 190, window=self.button_sign_up)

        self.button_sign_up.bind("<Enter>", lambda event: self.button_sign_up.config(bg="#dc5765"))
        self.button_sign_up.bind("<Leave>", lambda event: self.button_sign_up.config(bg="#ffffff"))
       
        # Halaman pemilihan jumlah genre
        self.halaman_pilihan_genre = tk.Frame(self.root)
        
        bg_pilihan = Image.open("tubes2/resource/halaman pilihan.png")
        bg_pilihan = bg_pilihan.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_pilihan = ImageTk.PhotoImage(bg_pilihan)
        
        self.canvas_pilihan = tk.Canvas(self.halaman_pilihan_genre, width=screen_width, height=screen_height)
        self.canvas_pilihan.pack(fill="both", expand=True)
        self.canvas_pilihan.create_image(0,0, image=self.bg_image_pilihan, anchor="nw")
        
        self.label_pilihan_genre = tk.Label(self.halaman_pilihan_genre, text="Pilih Metode Pencarian Buku Berdasarkan Genre", font=("Courier", 20, "bold"),  bg="#ffeeea", fg="#995a3a")
        self.canvas_pilihan.create_window(screen_width // 2, screen_height // 2 - 100, window=self.label_pilihan_genre)

        self.tombol_satu_genre = tk.Button(self.halaman_pilihan_genre, text="Cari Buku Berdasarkan Satu Genre", font=("Courier", 15, "bold"), command=self.buka_halaman_satu_genre, fg="#d97051")
        self.canvas_pilihan.create_window(screen_width // 2, screen_height // 2 - 50, window=self.tombol_satu_genre)
    
        self.tombol_dua_genre = tk.Button(self.halaman_pilihan_genre, text="Cari Buku Berdasarkan Dua Genre", font=("Courier", 15, "bold"), command=self.buka_halaman_dua_genre, fg="#d97051")
        self.canvas_pilihan.create_window(screen_width // 2, screen_height // 2 + 10, window=self.tombol_dua_genre)
        
        self.tombol_satu_genre.bind("<Enter>", lambda event: self.tombol_satu_genre.config(bg="#9ea7fa"))
        self.tombol_satu_genre.bind("<Leave>", lambda event: self.tombol_satu_genre.config(bg="#ffffff"))
        self.tombol_dua_genre.bind("<Enter>", lambda event: self.tombol_dua_genre.config(bg="#9ea7fa"))
        self.tombol_dua_genre.bind("<Leave>", lambda event: self.tombol_dua_genre.config(bg="#ffffff"))

        # Halaman pencarian satu genre
        self.halaman_satu_genre = tk.Frame(self.root)
        
        bg_satugenre = Image.open("tubes2/resource/halaman satu genre.png")
        bg_satugenre = bg_satugenre.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_satugenre = ImageTk.PhotoImage(bg_satugenre)
        
        self.canvas_satugenre = tk.Canvas(self.halaman_satu_genre, width=screen_width, height=screen_height)
        self.canvas_satugenre.pack(fill="both", expand=True)
        self.canvas_satugenre.create_image(0,0, image=self.bg_image_satugenre, anchor="nw")
        
        self.label_genre1 = tk.Label(self.halaman_satu_genre, text="Pilih Genre:", font=("Courier", 20, "bold"), bg="#ffeeea", fg="#995a3a")
        self.canvas_satugenre.create_window(screen_width // 2, screen_height // 2 - 280, window=self.label_genre1)

        self.kombobox_genre1 = ttk.Combobox(self.halaman_satu_genre, values=self.genres)
        self.canvas_satugenre.create_window(screen_width // 2, screen_height // 2 - 245, window=self.kombobox_genre1)
        
        self.tombol_rekomendasi1 = tk.Button(self.halaman_satu_genre, text="Rekomendasikan Buku", font=("Courier", 15, "bold"), command=self.rekomendasi_buku_satu_genre, fg="#d97051")
        self.canvas_satugenre.create_window(screen_width // 2, screen_height // 2 - 200, window=self.tombol_rekomendasi1)
        
        self.tombol_rekomendasi1.bind("<Enter>", lambda event: self.tombol_rekomendasi1.config(bg="#9ea7fa"))
        self.tombol_rekomendasi1.bind("<Leave>", lambda event: self.tombol_rekomendasi1.config(bg="#ffffff"))

        self.area_hasil1 = tk.Text(self.halaman_satu_genre, wrap="word", height=20, width=90)
        self.canvas_satugenre.create_window(screen_width // 2, screen_height // 2, window=self.area_hasil1)
        self.area_hasil1.config(state="disabled")

        self.tombol_kembali1 = tk.Button(self.halaman_satu_genre, text="Kembali", font=("Courier", 15, "bold"), command=self.kembali_ke_pilihan_genre, fg="#d97051")
        self.canvas_satugenre.create_window(screen_width // 2, screen_height // 2 + 200, window=self.tombol_kembali1)
        self.tombol_kembali1.bind("<Enter>", lambda event: self.tombol_kembali1.config(bg="#9ea7fa"))
        self.tombol_kembali1.bind("<Leave>", lambda event: self.tombol_kembali1.config(bg="#ffffff"))

        
        self.tombol_selesai1 = tk.Button(self.halaman_satu_genre, text="Lanjut", font=("Courier", 15, "bold"), command=self.buka_halaman_riwayat, fg="#d97051")
        self.canvas_satugenre.create_window(screen_width // 2, screen_height // 2 + 250, window=self.tombol_selesai1)
        self.tombol_selesai1.bind("<Enter>", lambda event: self.tombol_selesai1.config(bg="#9ea7fa"))
        self.tombol_selesai1.bind("<Leave>", lambda event: self.tombol_selesai1.config(bg="#ffffff"))

        # Halaman pencarian dua genre
        self.halaman_dua_genre = tk.Frame(self.root)
        
        bg_duagenre = Image.open("tubes2/resource/halaman dua genre.png")
        bg_duagenre = bg_duagenre.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_duagenre = ImageTk.PhotoImage(bg_duagenre)
        
        self.canvas_duagenre = tk.Canvas(self.halaman_dua_genre, width=screen_width, height=screen_height)
        self.canvas_duagenre.pack(fill="both", expand=True)
        self.canvas_duagenre.create_image(0,0, image=self.bg_image_duagenre, anchor="nw")
        
        self.label_genre2_1 = tk.Label(self.halaman_dua_genre, text="Pilih Genre 1:", font=("Courier", 15, "bold"), bg="#ffeeea", fg="#995a3a")
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2 - 350, window=self.label_genre2_1)

        self.kombobox_genre2_1 = ttk.Combobox(self.halaman_dua_genre, values=self.genres)
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2 - 315, window=self.kombobox_genre2_1)
      
        self.label_genre2_2 = tk.Label(self.halaman_dua_genre, text="Pilih Genre 2:", font=("Courier", 15, "bold"), bg="#ffeeea", fg="#995a3a")
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2 - 280, window=self.label_genre2_2)
       
        self.kombobox_genre2_2 = ttk.Combobox(self.halaman_dua_genre, values=self.genres)
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2 - 245, window=self.kombobox_genre2_2)
        
        self.tombol_rekomendasi2 = tk.Button(self.halaman_dua_genre, text="Rekomendasikan Buku", font=("Courier", 15, "bold"), command=self.rekomendasi_buku_dua_genre, fg="#d97051")
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2 - 200, window=self.tombol_rekomendasi2)
        
        self.tombol_rekomendasi2.bind("<Enter>", lambda event: self.tombol_rekomendasi2.config(bg="#9ea7fa"))
        self.tombol_rekomendasi2.bind("<Leave>", lambda event: self.tombol_rekomendasi2.config(bg="#ffffff"))
       
        self.area_hasil2 = tk.Text(self.halaman_dua_genre, wrap="word", height=20, width=90)
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2, window=self.area_hasil2)
        self.area_hasil2.config(state="disabled")

        self.tombol_kembali2 = tk.Button(self.halaman_dua_genre, text="Kembali", font=("Courier", 15, "bold"), command=self.kembali_ke_pilihan_genre, fg="#d97051")
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2 + 200, window=self.tombol_kembali2)
        
        self.tombol_kembali2.bind("<Enter>", lambda event: self.tombol_kembali2.config(bg="#9ea7fa"))
        self.tombol_kembali2.bind("<Leave>", lambda event: self.tombol_kembali2.config(bg="#ffffff"))
        
        self.tombol_selesai2 = tk.Button(self.halaman_dua_genre, text="Lanjut", font=("Courier", 15, "bold"), command=self.buka_halaman_riwayat, fg="#d97051")
        self.canvas_duagenre.create_window(screen_width // 2, screen_height // 2 + 250, window=self.tombol_selesai2)
        
        self.tombol_selesai2.bind("<Enter>", lambda event: self.tombol_selesai2.config(bg="#9ea7fa"))
        self.tombol_selesai2.bind("<Leave>", lambda event: self.tombol_selesai2.config(bg="#ffffff"))
        
        # Halaman Riwayat
        self.halaman_riwayat = tk.Frame(self.root)
        
        bg_riwayat = Image.open("tubes2/resource/halaman riwayat.png")
        bg_riwayat = bg_riwayat.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_riwayat = ImageTk.PhotoImage(bg_riwayat)
        
        self.canvas_riwayat = tk.Canvas(self.halaman_riwayat, width=screen_width, height=screen_height)
        self.canvas_riwayat.pack(fill="both", expand=True)
        self.canvas_riwayat.create_image(0,0, image=self.bg_image_riwayat, anchor="nw")
        
        self.label_riwayat_buku = tk.Label(self.halaman_riwayat, text="Riwayat Buku", font=("Courier", 20, "bold"), bg="#ffeeea", fg="#995a3a")
        self.canvas_riwayat.create_window(screen_width // 2, screen_height // 2 - 200, window=self.label_riwayat_buku)

        self.hasil_riwayat_buku = tk.Text(self.halaman_riwayat, wrap="word", height=20, width=90)
        self.canvas_riwayat.create_window(screen_width // 2, screen_height // 2, window=self.hasil_riwayat_buku)
        self.hasil_riwayat_buku.config(state="disabled")
        
        self.tombol_selesai = tk.Button(self.halaman_riwayat, text ="Selesai", font=("Courier", 15, "bold"), command=self.buka_halaman_terima_kasih, fg="#d97051")
        self.canvas_riwayat.create_window(screen_width // 2, screen_height // 2 + 200, window=self.tombol_selesai)
        
        self.tombol_selesai.bind("<Enter>", lambda event: self.tombol_selesai.config(bg="#9ea7fa"))
        self.tombol_selesai.bind("<Leave>", lambda event: self.tombol_selesai.config(bg="#ffffff"))
        
        # Halaman terima kasih
        self.halaman_terima_kasih = tk.Frame(self.root)
        
        bg_terimakasih = Image.open("tubes2/resource/halaman terima kasih.png")
        bg_terimakasih = bg_terimakasih.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_image_terimakasih = ImageTk.PhotoImage(bg_terimakasih)
        
        self.canvas_terimakasih = tk.Canvas(self.halaman_terima_kasih, width=screen_width, height=screen_height)
        self.canvas_terimakasih.pack(fill="both", expand=True)
        self.canvas_terimakasih.create_image(0,0, image=self.bg_image_terimakasih, anchor="nw")
    
        self.label_terima_kasih = tk.Label(self.halaman_terima_kasih, text="Terima kasih telah menggunakan Aplikasi Pemilihan Buku Berdasarkan Genre", font=("Courier", 20, "bold"), bg="#ffeeea", fg="#995a3a")
        self.canvas_terimakasih.create_window(screen_width // 2 + 50, screen_height // 2 - 200, window=self.label_terima_kasih)
        
        self.tombol_keluar = tk.Button(self.halaman_terima_kasih, text="Keluar", font=("Courier", 15, "bold"), command=quit, fg="#d97051")
        self.canvas_terimakasih.create_window(screen_width // 2 + 50, screen_height // 2 + 220, window=self.tombol_keluar)
        
        self.tombol_keluar.bind("<Enter>", lambda event: self.tombol_keluar.config(bg="#9ea7fa"))
        self.tombol_keluar.bind("<Leave>", lambda event: self.tombol_keluar.config(bg="#ffffff"))
        
        
        
    def buka_halaman_login(self):
        self.halaman_awal.pack_forget()
        self.halaman_login.pack(fill="both", expand=True)
        
    def login(self):
        username = self.username_entry_login.get()
        password = self.password_entry_login.get()

        # Verifikasi data pengguna
        with open(self.user_data_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    self.current_user = username
                    messagebox.showinfo("Info", "Log in berhasil!")
                    self.halaman_login.pack_forget()
                    self.halaman_pilihan_genre.pack(fill="both", expand=True)
                    return
                # Panggil fungsi untuk melihat rekomendasi terdahulu
                    self.lihat_rekomendasi_terdahulu()
                    return
        
        messagebox.showerror("Error", "Username atau password salah.\nSilakan Sign Up jika belum memiliki akun")
        
    def buka_halaman_signup(self):
        self.halaman_login.pack_forget()
        self.halaman_signup.pack(fill="both", expand=True)

    def signup(self):
        username = self.username_entry_signup.get()
        password = self.password_entry_signup.get()
        
        if not username or not password:
            messagebox.showwarning("Peringatan", "Silakan masukkan username dan password.")
            return
        
        # Cek apakah username sudah ada
        with open(self.user_data_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username:
                    messagebox.showerror("Error", "Username sudah terdaftar. Silakan pilih username lain.")
                    return
        
        # Menyimpan data pengguna baru
        with open(self.user_data_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        
        messagebox.showinfo("Info", "Registrasi berhasil. Silakan login.")
        self.halaman_signup.pack_forget()
        self.halaman_login.pack(fill="both", expand=True)
        
    
    def muatan_buku(self):
        """Memuat data buku dari file CSV."""
        self.books_df = pd.read_csv('resource/books.csv', encoding='ISO-8859-1')
        self.genres = self.books_df['genre'].unique().tolist()
        unique_genres = set()
        for genres in self.books_df['genre']:
            for genre in genres.split(', '):
                unique_genres.add(genre)

        self.genres = list(unique_genres)

    def buka_pilihan_genre(self):
        # Sembunyikan halaman login
        self.halaman_login.pack_forget()
        self.halaman_signup.pack_forget()
        # Tampilkan halaman pilihan genre
        self.halaman_pilihan_genre.pack(fill="both", expand=True)

    def buka_halaman_satu_genre(self):
        # Sembunyikan halaman pilihan genre
        self.halaman_pilihan_genre.pack_forget()
        # Tampilkan halaman satu genre
        self.halaman_satu_genre.pack(fill="both", expand=True)

    def buka_halaman_dua_genre(self):
        # Sembunyikan halaman pilihan genre
        self.halaman_pilihan_genre.pack_forget()
        # Tampilkan halaman dua genre
        self.halaman_dua_genre.pack(fill="both", expand=True)

    def kembali_ke_pilihan_genre(self):
        # Sembunyikan halaman pencarian genre (baik satu atau dua)
        self.halaman_satu_genre.pack_forget()
        self.halaman_dua_genre.pack_forget()
        
        # Tampilkan halaman pilihan genre
        self.halaman_pilihan_genre.pack(fill="both", expand=True)
        
        # Panggil fungsi untuk melihat rekomendasi terdahulu
        self.lihat_rekomendasi_terdahulu()


    def rekomendasi_buku_satu_genre(self):
        genre1 = self.kombobox_genre1.get()

        if not genre1:
            messagebox.showwarning("Peringatan", "Silakan pilih satu genre.")
            return

        # Filter buku berdasarkan genre1
        buku_terfilter = self.books_df[self.books_df['genre'] == genre1]

        # Tampilkan hasil rekomendasi
        self.tampilkan_hasil(self.area_hasil1, buku_terfilter)
        

    def rekomendasi_buku_dua_genre(self):
        genre1 = self.kombobox_genre2_1.get()
        genre2 = self.kombobox_genre2_2.get()

        if not genre1 or not genre2:
            messagebox.showwarning("Peringatan", "Silakan pilih dua genre.")
            return

        # Filter buku berdasarkan genre1 dan genre2
        buku_terfilter = self.books_df[self.books_df['genre'].str.contains(genre1) & self.books_df['genre'].str.contains(genre2)]

        # Tampilkan hasil rekomendasi
        self.tampilkan_hasil(self.area_hasil2, buku_terfilter)
        
        
    def tampilkan_hasil(self, area_hasil, buku_terfilter):
        area_hasil.config(state="normal")
        area_hasil.delete(1.0, "end")

        if buku_terfilter.empty:
            area_hasil.insert("end", "Tidak ada buku yang cocok dengan genre yang dipilih.")
        else:
            for _, row in buku_terfilter.iterrows():
                area_hasil.insert(
         "end",
        f"Judul     : {row['title']}\n"
        f"Penulis   : {row['author']}\n"
        f"Genre     : {row['genre']}\n\n"
    )

        area_hasil.config(state="disabled")
        # simpan hasil rekomendasi ke CSV
        self.simpan_rekomendasi(buku_terfilter, 'rekomendasi_buku.csv')
        
    def buka_halaman_riwayat(self):
        # Sembunyikan halaman 
        self.halaman_awal.pack_forget()
        self.halaman_satu_genre.pack_forget()
        self.halaman_dua_genre.pack_forget()
        self.halaman_pilihan_genre.pack_forget()
        
        # Tampilkan halaman riwayat
        self.halaman_riwayat.pack(fill="both", expand=True)
        
        

    def simpan_rekomendasi(self, buku_terfilter, filename):
        """Simpan hasil rekomendasi ke file CSV, termasuk username pengguna."""
        if buku_terfilter.empty or not self.current_user:
            return
        
        #mengecek file sudah tersedia atau belum
        file_baru = not os.path.exists(filename)
        
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file_baru:
                writer.writerow(['username', 'title', 'author', 'genre'])
            for _, row in buku_terfilter.iterrows():
                writer.writerow([self.current_user, row['title'], row['author'], row['genre']])
                
        print(f"Rekomendasi disimpan untuk pengguna{self.current_user}")
                
    def lihat_rekomendasi_terdahulu(self):
        """Menampilkan rekomendasi buku sebelumnya berdasarkan username pengguna."""
        if not os.path.exists('rekomendasi_buku.csv'):
            return  
        rekomendasi_terdahulu = []

        # Baca file rekomendasi dan filter berdasarkan username
        with open('rekomendasi_buku.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == self.current_user:
                    rekomendasi_terdahulu.append(f"Judul: {row['title']}, Penulis: {row['author']}, Genre: {row['genre']}")

        # Tampilkan hasil di area teks halaman riwayat
        self.hasil_riwayat_buku.config(state="normal")
        self.hasil_riwayat_buku.delete(1.0, "end")

        if rekomendasi_terdahulu:
            self.hasil_riwayat_buku.insert("end", "Rekomendasi Sebelumnya:\n\n")
            self.hasil_riwayat_buku.insert("end", "\n".join(rekomendasi_terdahulu))
        else:
            self.hasil_riwayat_buku.insert("end", "Belum ada rekomendasi sebelumnya untuk pengguna ini.")

        self.hasil_riwayat_buku.config(state="disabled")
        
    def buka_halaman_terima_kasih(self):
        # Sembunyikan halaman 
        self.halaman_awal.pack_forget()
        self.halaman_satu_genre.pack_forget()
        self.halaman_dua_genre.pack_forget()
        self.halaman_pilihan_genre.pack_forget()
        self.halaman_riwayat.pack_forget()
        
        # Tampilkan halaman terima kasih
        self.halaman_terima_kasih.pack(fill="both", expand=True)
    
    
# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiRekomendasiBuku(root)
    root.mainloop()        