import tkinter as tk
from tkinter import ttk


BG_COLOR = "#f9f9f9"
HEADER_COLOR = "#4da6ff"
BUTTON_COLOR = "#5cdb95"
TEXT_COLOR = "#b8c2cc"



window = tk.Tk()
window.title("pp")
window.geometry("600x400")
window.configure(bg=BG_COLOR)


header = tk.Label(window, text="fgh", font=("Helvetica", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
header.pack(pady=10)


main_frame = tk.Frame(window, bg=BG_COLOR)
main_frame.pack(pady=20)


tk.Label(main_frame, text="No. Bilik", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_no_bilik = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
entry_no_bilik.grid(row=0, column=1, padx=10, pady=5)

select_bilik = ttk.Combobox(main_frame ,="Pilih Saiz Bilik", values = ("2", "4"))
select_bilik.current(0)
select_bilik.grid(row=1, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Nama Pelapor", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky="w", padx=10, pady=5)
isi_nama = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
isi_nama.grid(row=2, column=1, padx=10, pady=5)


tk.Label(main_frame, text="Jenis Kerosakan", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, sticky="w", padx=10, pady=5)
jenis_kerosakan = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
jenis_kerosakan.grid(row=3, column=1, padx=10, pady=5)


button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=20)

btn_simpan = tk.Button(button_frame, text="Save", font=("Helvetica", 12), bg=BUTTON_COLOR, fg="white", width=10)
btn_simpan.grid(row=0, column=0, padx=10)

btn_keluar = tk.Button(button_frame, text="Exit", font=("Helvetica", 12), bg="#ff6f61", fg="white", width=10, command=window.destroy)
btn_keluar.grid(row=0, column=1, padx=10)

window.mainloop()