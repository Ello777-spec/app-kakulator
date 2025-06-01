import ttkbootstrap as ttkb
from PIL import Image, ImageTk
import os

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Mobil")
        self.root.geometry("600x500")
        self.dataPilih = {}

        ttkb.Label(root, text="pilih variable:").pack(pady=5)
        self.combo_cari = ttkb.Combobox(root,values=["percepatan", "kecepatan_awal", "kecepatan_akhir", "waktu"], bootstyle="primary")
        self.combo_cari.pack()
        self.combo_cari.bind("<<ComboboxSelected>>", self.tampil_input)


        self.main_frame = ttkb.Frame(root)
        self.main_frame.pack(pady=10)

        self.input_frame = ttkb.Frame(self.main_frame)
        self.input_frame.grid(row=0, column=0, padx=10)

        self.image_frame = ttkb.Frame(self.main_frame)
        self.image_frame.grid(row=0, column=1, padx=10)

        ttkb.Button(root, text="Hitung", command=self.hitung, bootstyle="info").pack(pady=5)
        
        self.hasil = ttkb.StringVar() # works like a ppt
        ttkb.Label(root, textvariable=self.hasil, bootstyle="primary").pack(pady=5)

    def tampil_input(self,event):
        self.dataPilih.clear()
        cari = self.combo_cari.get()

        for widget in self.input_frame.winfo_children():
            widget.destroy()
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        self.tampil_gambar(cari)

        if cari == "percepatan":
            for i, label in enumerate(["kecepatan_awal", "kecepatan_akhir", "waktu"]):
                ttkb.Label(self.input_frame, text=label + ":").grid(row=i, column=0)
                self.dataPilih[label.lower()] = ttkb.Entry(self.input_frame)
                self.dataPilih[label.lower()].grid(row=i, column=1)
        elif cari == "kecepatan_awal":
            for i, label in enumerate(["percepatan", "kecepatan_akhir", "waktu"]):
                ttkb.Label(self.input_frame, text=label + ":").grid(row=i, column=0)
                self.dataPilih[label.lower()] = ttkb.Entry(self.input_frame)
                self.dataPilih[label.lower()].grid(row=i, column=1)
        elif cari == "kecepatan_akhir":
            for i, label in enumerate(["percepatan", "kecepatan_awal", "waktu"]):
                ttkb.Label(self.input_frame, text=label + ":").grid(row=i, column=0)
                self.dataPilih[label.lower()] = ttkb.Entry(self.input_frame)
                self.dataPilih[label.lower()].grid(row=i, column=1)
        elif cari == "waktu":
            for i, label in enumerate(["percepatan", "kecepatan_awal", "kecepatan_akhir"]):
                ttkb.Label(self.input_frame, text=label + ":").grid(row=i, column=0)
                self.dataPilih[label.lower()] = ttkb.Entry(self.input_frame)
                self.dataPilih[label.lower()].grid(row=i, column=1)

    def tampil_gambar(self,sppeedd):
        path = f"img/{sppeedd}.png"
        if os.path.exists(path):
            img = Image.open(path)
            img = img.resize((300, 200))
            photo = ImageTk.PhotoImage(img)
            label_img = ttkb.Label(self.image_frame, image=photo)
            label_img.image = photo
            label_img.pack()
        else:
            ttkb.Label(self.image_frame, text="Gambar tidak ditemukan").pack()

    def hitung(self):
        cari = self.combo_cari.get()
        try:
            if cari == "percepatan":
                Vo = float(self.dataPilih['kecepatan_awal'].get())
                Vt = float(self.dataPilih['kecepatan_akhir'].get())
                T = float(self.dataPilih['waktu'].get())
                A = (Vt - Vo) / T
                self.hasil.set(f"percepatan: {A:.2f} m/s\u00B2")
            elif cari == "kecepatan_awal":
                A = float(self.dataPilih['percepatan'].get())
                Vt = float(self.dataPilih['kecepatan_akhir'].get())
                T = float(self.dataPilih['waktu'].get())
                Vo = Vt - A * T
                self.hasil.set(f"kecepatan_awal: {Vo:.2f} m/s")
            elif cari == "kecepatan_akhir":
                A = float(self.dataPilih['percepatan'].get())
                Vo = float(self.dataPilih['kecepatan_awal'].get())
                T = float(self.dataPilih['waktu'].get())
                Vt = Vo + A * T
                self.hasil.set(f"kecepatan_akhir: {Vt:.2f} m/s")
            elif cari == "waktu":
                A = float(self.dataPilih['percepatan'].get())
                Vo = float(self.dataPilih['kecepatan_awal'].get())
                Vt = float(self.dataPilih['kecepatan_akhir'].get())
                T = (Vt - Vo) / A
                self.hasil.set(f"waktu: {T:.2f} s")
            else:
                self.hasil.set("Pilih")
                return

        except Exception:
            self.hasil.set("Input tidak valid!")


if __name__ == "__main__":
    app = ttkb.Window(themename="vapor")
    MainApp(app)
    app.mainloop()