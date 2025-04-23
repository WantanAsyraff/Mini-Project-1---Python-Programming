# Wantan & Jerin
import tkinter as tk
from tkinter import ttk


BG_COLOR = "#f9f9f9"
HEADER_COLOR = "#4da6ff"
BUTTON_COLOR = "#5cdb95"
TEXT_COLOR = "#b8c2cc"



window = tk.Tk()
window.title("pp")
window.geometry("800x400")
window.configure(bg=BG_COLOR)


header = tk.Label(window, text="SISTEM ADUAN BILIK KAMSIS", font=("Helvetica", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
header.pack(pady=10)


main_frame = tk.Frame(window, bg=BG_COLOR)
main_frame.pack(pady=20)


# No Bilik
tk.Label(main_frame, text="No. Bilik", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_no_bilik = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
entry_no_bilik.grid(row=0, column=2, padx=10, pady=5)

combo_no_bilik = ttk.Combobox(main_frame, values = ("A", "B", "C", "D", "E", "F", "G", "H"))
combo_no_bilik.set("Pilih Blok")
combo_no_bilik.grid(row=0, column=1, padx=10, pady=5)

# Select bilik
select_bilik_label = ttk.Label(main_frame, text="Pilih Saiz Bilik", font=("Helvetica", 12), background=BG_COLOR, foreground=TEXT_COLOR)
select_bilik_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
select_bilik = ttk.Combobox(main_frame, values = ("1 orang", "2 orang", "4 orang"))

select_bilik.set("Pilih Saiz Bilik")
select_bilik.current(0)
select_bilik.grid(row=1, column=1, padx=10, pady=5)

# Nama
tk.Label(main_frame, text="Nama Pelapor", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky="w", padx=10, pady=5)
isi_nama = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
isi_nama.grid(row=2, column=2, padx=10, pady=5)

# Jenis aduan
tk.Label(main_frame, text="Jenis Kerosakan", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, sticky="w", padx=10, pady=5)
jenis_aduan = ttk.Combobox(main_frame, values=("Almari rosak", "Meja rosak", "Katil runtuh", "Kipas rosak", "Plug socket rosak", "Lain-lain"))
jenis_aduan.set("Pilih jenis aduan")
jenis_aduan.grid(row=3, column=1, padx=10, pady=5)

# Cadangan tambahan
tk.Label(main_frame, text="Cadangan Tambahan/Penerangan", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=4, column=0, sticky="w", padx=10, pady=5)
cadangan_tambahan = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
cadangan_tambahan.grid(row=4, column=2, padx=10, pady=5)

# butang hantar dan keluar
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=20)

btn_hantar = tk.Button(button_frame, text="Hantar", font=("Helvetica", 12), bg=BUTTON_COLOR, fg="white", width=10)
btn_hantar.grid(row=0, column=0, padx=10)

btn_keluar = tk.Button(button_frame, text="Keluar", font=("Helvetica", 12), bg="#ff6f61", fg="white", width=10, command=window.destroy)
btn_keluar.grid(row=0, column=1, padx=10)

window.mainloop()