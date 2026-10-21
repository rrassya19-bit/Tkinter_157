import tkinter as tk

BG = "#0F1318"
KARTU = "#171C23"
KOTAK = "#222A34"
TEKS = "#E6EDF3"
ABU = "#8B949E"
GARIS = "#39424E"
AKSEN = "#3B6FB6"
AKSEN_HOVER = "#2E5A94"
AKSEN_TERANG = "#8AB4F8"
MERAH = "#F47067"

teksAwal = "Hasil prediksi akan tampil di sini"
daftarEntry = []

def resetHasil(*args):
    hasil.config(text=teksAwal, fg=ABU)
    for e in daftarEntry:
        e.config(highlightbackground=GARIS)

def hasilPrediksi(event=None):
    kosong = False
    diluar = False
    for e in daftarEntry:
        nilai = e.get().strip().replace(",", ".")
        try:
            angka = float(nilai)
            if angka < 0 or angka > 100:
                diluar = True
                e.config(highlightbackground=MERAH)
            else:
                e.config(highlightbackground=GARIS)
        except ValueError:
            kosong = True
            e.config(highlightbackground=MERAH)
    if kosong:
        hasil.config(text="Lengkapi 10 nilai berupa angka terlebih dahulu", fg=MERAH)
    elif diluar:
        hasil.config(text="Nilai harus berada di antara 0 sampai 100", fg=MERAH)
    else:
        hasil.config(text="Prodi Pilihan: Teknologi Informasi", fg=AKSEN_TERANG)

def tombolMasuk(e):
    B.config(bg=AKSEN_HOVER)

def tombolKeluar(e):
    B.config(bg=AKSEN)

def fokusMasuk(e):
    if e.widget.cget("highlightbackground") != MERAH:
        e.widget.config(highlightbackground=AKSEN)

def fokusKeluar(e):
    if e.widget.cget("highlightbackground") != MERAH:
        e.widget.config(highlightbackground=GARIS)

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.resizable(False, False)
top.config(bg=BG)

utama = tk.Frame(top, bg=BG)
utama.pack(padx=36, pady=30)

