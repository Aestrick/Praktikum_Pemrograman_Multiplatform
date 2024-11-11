import tkinter as tk  # Mengimpor modul tkinter sebagai tk untuk membuat GUI
from tkinter import font  # Mengimpor modul font dari tkinter untuk mengatur font khusus

# Membuat jendela utama aplikasi
root = tk.Tk()  # Membuat jendela utama atau root untuk aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela
root.geometry("400x500")  # Mengatur ukuran jendela utama menjadi 400x500 piksel

# Mengatur font yang mewah
judul_font = font.Font(family="Helvetica", size=16, weight="bold")  # Membuat font untuk judul dengan gaya Helvetica, ukuran 16, dan tebal
input_font = font.Font(family="Arial", size=12)  # Membuat font untuk input dengan gaya Arial, ukuran 12
hasil_font = font.Font(family="Times New Roman", size=14, slant="italic")  # Membuat font untuk hasil dengan gaya Times New Roman, ukuran 14, dan miring

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=judul_font)  # Membuat label judul dengan teks dan font khusus
judul_label.pack(pady=10)  # Menempatkan label judul di jendela utama dan memberi jarak vertikal 10 piksel di atas dan di bawah

# List mata pelajaran
mata_pelajaran = [
    "Matematika", "Fisika", "Kimia", "Biologi",
    "Bahasa Indonesia", "Bahasa Inggris", "Sejarah",
    "Geografi", "Ekonomi", "Sosiologi"
]  # Membuat daftar mata pelajaran yang akan ditampilkan sebagai label di sebelah input nilai

# Input nilai mata pelajaran
entry_nilai = []  # Membuat list kosong untuk menyimpan entri input nilai
for pelajaran in mata_pelajaran:  # Melakukan loop melalui setiap mata pelajaran dalam list
    frame = tk.Frame(root)  # Membuat frame untuk menempatkan label dan entry input dalam satu baris
    frame.pack(pady=5)  # Menempatkan frame pada jendela utama dengan jarak vertikal 5 piksel di atas dan di bawahnya
    
    label = tk.Label(frame, text=pelajaran, font=input_font, width=15, anchor="w")  # Membuat label untuk nama mata pelajaran dengan lebar tetap 15 karakter dan rata kiri
    label.pack(side=tk.LEFT)  # Menempatkan label di sisi kiri dalam frame
    
    entry = tk.Entry(frame, font=input_font, width=10)  # Membuat entry input untuk nilai mata pelajaran dengan lebar 10 karakter
    entry.pack(side=tk.LEFT)  # Menempatkan entry di sisi kiri dalam frame, tepat di sebelah label
    
    entry_nilai.append(entry)  # Menambahkan entry ke list entry_nilai untuk akses mudah jika diperlukan

# Fungsi untuk tombol prediksi
def prediksi_prodi():
    # Mengubah teks dari label hasil_label menjadi "Prediksi Prodi: Teknologi Informasi"
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")

# Tombol "Hasil Prediksi"
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi, font=input_font)  # Membuat tombol dengan teks "Hasil Prediksi" dan fungsi yang dipanggil saat diklik
prediksi_button.pack(pady=20)  # Menempatkan tombol di jendela utama dengan jarak vertikal 20 piksel

# Label hasil prediksi
hasil_label = tk.Label(root, text="", font=hasil_font)  # Membuat label untuk hasil prediksi, dengan font khusus dan teks kosong sebagai default
hasil_label.pack(pady=20)  # Menempatkan label hasil di jendela utama dengan jarak vertikal 20 piksel

# Menjalankan aplikasi
root.mainloop()  # Menjalankan loop utama aplikasi untuk memulai GUI dan menunggu interaksi pengguna