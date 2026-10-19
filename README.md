Penjelasan Struktur:

1. `main.py` File utama yang dijalankan untuk menampilkan jendela GUI aplikasi dan tempat interaksi utama dengan user.

* `import tkinter as tk`: Perintah buat ngambil modul Tkinter supaya komponen GUI bisa dipakai.
* `def hasil_prediksi()`: Fungsi buat ngatur aksi pas tombol diklik, isinya buat ngubah teks luaran jadi "Prodi Pilihan: Teknologi Informasi" apa pun input yang diberikan.
* `tk.Tk()`: Buat bikin jendela utama aplikasi (main window).
* `tk.Label()`: Buat nampilin teks di layar, seperti judul aplikasi dan label luaran hasil prediksi.
* `tk.Frame()`: Wadah atau kontainer buat ngelompokkan dan merapikan susunan 10 input mata kuliah.
* `tk.Entry()`: Kolom teks satu baris buat nerima masukan nilai dari user untuk masing-masing mata kuliah.
* `tk.Button()`: Tombol bertuliskan "Hasil Prediksi" yang kalau diklik bakal manggil fungsi `hasil_prediksi()`.
* `root.mainloop()`: Perintah penutup buat ngejalanin event loop utama supaya jendela aplikasinya tetap terbuka dan merespons interaksi user.