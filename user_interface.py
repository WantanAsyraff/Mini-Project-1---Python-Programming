#Jerin
import tkinter as tk
from tkinter import ttk

# Warna tema
BG_COLOR = "#f9f9f9"
HEADER_COLOR = "#4da6ff"
BUTTON_COLOR = "#5cdb95"
TEXT_COLOR = "#05386b"



window = tk.Tk()
window.title("pp")
window.geometry("600x400")
window.configure(bg=BG_COLOR)


header = tk.Label(window, text="fgh", font=("Helvetica", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
header.pack(pady=10)


main_frame = tk.Frame(window, bg=BG_COLOR)
main_frame.pack(pady=20)


tk.Label(main_frame, text="rgd", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_nama = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
entry_nama.grid(row=0, column=1, padx=10, pady=5)


tk.Label(main_frame, text="grd", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_kelas = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
entry_kelas.grid(row=1, column=1, padx=10, pady=5)


tk.Label(main_frame, text="rg", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_tarikh = tk.Entry(main_frame, font=("Helvetica", 12), width=30)
entry_tarikh.grid(row=2, column=1, padx=10, pady=5)


button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=20)

btn_simpan = tk.Button(button_frame, text="Save", font=("Helvetica", 12), bg=BUTTON_COLOR, fg="white", width=10)
btn_simpan.grid(row=0, column=0, padx=10)

btn_keluar = tk.Button(button_frame, text="Exit", font=("Helvetica", 12), bg="#ff6f61", fg="white", width=10, command=window.destroy)
btn_keluar.grid(row=0, column=1, padx=10)

window.mainloop()