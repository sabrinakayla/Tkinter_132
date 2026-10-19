import tkinter as tk

def hasil_prediksi():
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x600")
root.configure(padx=20, pady=20)

label_judul = tk.Label(
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Helvetica", 14, "bold")
)
label_judul.pack(pady=(0, 15))

frame_input = tk.Frame(root)
frame_input.pack(fill="x", pady=5)

matkul_list = [
    "Pemrograman Multiplatform",
    "Perancangan Berorientasi Objek",
    "Algoritma dan Struktur Data",
    "Probabilitas dan Statistika",
    "Switching dan Wireless",
    "Teknologi Server",
    "Implementasi Basis Data",
    "Administrasi Basis Data",
    "Dasar Jaringan",
    "Pemrograman Dasar"
]

entries = []

for i, matkul in enumerate(matkul_list):
    lbl = tk.Label(frame_input, text=f"Nilai {matkul}:", anchor="w")
    lbl.grid(row=i, column=0, sticky="w", pady=2, padx=5)
    
    entry = tk.Entry(frame_input, width=15)
    entry.grid(row=i, column=1, sticky="e", pady=2, padx=5)
    entries.append(entry)

frame_input.columnconfigure(0, weight=1)
frame_input.columnconfigure(1, weight=1)

btn_prediksi = tk.Button(
    root, 
    text="Hasil Prediksi", 
    command=hasil_prediksi,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 10, "bold"),
    padx=10,
    pady=5
)
btn_prediksi.pack(pady=15)

label_hasil = tk.Label(
    root, 
    text="", 
    font=("Helvetica", 12, "bold"),
    fg="#1E88E5"
)
label_hasil.pack(pady=5)

root.mainloop()