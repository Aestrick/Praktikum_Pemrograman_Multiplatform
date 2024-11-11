import tkinter as tk
from tkinter import font

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")

# Mengatur font yang mewah
judul_font = font.Font(family="Helvetica", size=16, weight="bold")
input_font = font.Font(family="Arial", size=12)
hasil_font = font.Font(family="Times New Roman", size=14, slant="italic")

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=judul_font)
judul_label.pack(pady=10)

# List mata pelajaran
mata_pelajaran = [
    "Matematika", "Fisika", "Kimia", "Biologi",
    "Bahasa Indonesia", "Bahasa Inggris", "Sejarah",
    "Geografi", "Ekonomi", "Sosiologi"
]

# Input nilai mata pelajaran
entry_nilai = []
for pelajaran in mata_pelajaran:
    frame = tk.Frame(root)
    frame.pack(pady=5)
    
    label = tk.Label(frame, text=pelajaran, font=input_font, width=15, anchor="w")
    label.pack(side=tk.LEFT)
    
    entry = tk.Entry(frame, font=input_font, width=10)
    entry.pack(side=tk.LEFT)
    
    entry_nilai.append(entry)

# Fungsi untuk tombol prediksi
def prediksi_prodi():
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")

# Tombol "Hasil Prediksi"
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi, font=input_font)
prediksi_button.pack(pady=20)

# Label hasil prediksi
hasil_label = tk.Label(root, text="", font=hasil_font)
hasil_label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
