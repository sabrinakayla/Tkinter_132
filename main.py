import tkinter as tk
from tkinter import messagebox

def hitung_prediksi():
    if not entry_nama.get().strip():
        messagebox.showwarning("Peringatan", "Silakan masukkan nama siswa terlebih dahulu!")
        return
    for i, ent in enumerate(entry_nilai):
        if not ent.get().strip():
            messagebox.showwarning("Peringatan", f"Nilai {mapel_list[i]} belum diisi!")
            return
    lbl_hasil.config(text="Teknologi Informasi", fg="#2563eb")
    lbl_status.config(text=f"Selamat {entry_nama.get()}, kamu cocok di prodi ini!", fg="#16a34a")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("520x700")
root.configure(bg="#f8fafc")
root.resizable(False, False)

# Judul
tk.Label(root, text="PREDIKSI PRODI PILIHAN", font=("Segoe UI", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(pady=(15, 2))
tk.Label(root, text="Masukkan nilai mata pelajaran untuk memprediksi prodi", font=("Segoe UI", 9), bg="#f8fafc", fg="#64748b").pack(pady=(0, 10))

# Container Form
frame_form = tk.Frame(root, bg="#ffffff", bd=1, relief="solid", padx=20, pady=15)
frame_form.pack(padx=25, pady=5, fill="both", expand=True)

# Input Nama
tk.Label(frame_form, text="Nama Siswa", font=("Segoe UI", 9, "bold"), bg="#ffffff", fg="#334155").grid(row=0, column=0, sticky="w", pady=(0, 5))
entry_nama = tk.Entry(frame_form, font=("Segoe UI", 10), bg="#f8fafc", relief="solid", bd=1)
entry_nama.grid(row=0, column=1, columnspan=3, sticky="ew", pady=(0, 5), ipady=3)

tk.Frame(frame_form, height=1, bg="#e2e8f0").grid(row=1, column=0, columnspan=4, sticky="ew", pady=10)

# Input 10 Nilai
mapel_list = [f"Mapel {i}" for i in range(1, 11)]
entry_nilai = []

for i, mapel in enumerate(mapel_list):
    r, c = (i // 2) + 2, (i % 2) * 2
    tk.Label(frame_form, text=mapel, font=("Segoe UI", 9), bg="#ffffff", fg="#475569").grid(row=r, column=c, sticky="w", padx=(0, 5), pady=4)
    ent = tk.Entry(frame_form, font=("Segoe UI", 9), width=8, bg="#f8fafc", relief="solid", bd=1, justify="center")
    ent.grid(row=r, column=c + 1, sticky="w", padx=(0, 10), pady=4, ipady=2)
    entry_nilai.append(ent)

frame_form.columnconfigure((1, 3), weight=1)

# Tombol & Hasil
tk.Button(root, text="Hasil Prediksi", font=("Segoe UI", 10, "bold"), bg="#2563eb", fg="white", bd=0, cursor="hand2", command=hitung_prediksi).pack(pady=15, ipadx=20, ipady=6)

frame_hasil = tk.Frame(root, bg="#eff6ff", bd=1, relief="solid")
frame_hasil.pack(padx=25, pady=(0, 20), fill="x")

tk.Label(frame_hasil, text="Hasil Prediksi Prodi:", font=("Segoe UI", 9), bg="#eff6ff", fg="#64748b").pack(pady=(10, 0))
lbl_hasil = tk.Label(frame_hasil, text="-", font=("Segoe UI", 14, "bold"), bg="#eff6ff", fg="#1e293b")
lbl_hasil.pack(pady=2)
lbl_status = tk.Label(frame_hasil, text="Klik 'Hasil Prediksi' untuk melihat hasil", font=("Segoe UI", 8, "italic"), bg="#eff6ff", fg="#94a3b8")
lbl_status.pack(pady=(0, 10))

root.mainloop()