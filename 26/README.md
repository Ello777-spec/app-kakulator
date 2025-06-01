# Kalkulator Mobil 🧮
App simple yang untuk membantu hitung **percepatan**, **kepercepatan** **awal**, **kepercepatan** **akhir**, dan **waktu**

## 📸 Demo Highlight
![screenshot](path/to/https://cdn.corenexis.com/view/?img=d/ju1/0WmEZA.png)

## ✨ Fitur
- Pilih rumus untuk cari percapatan, kecapatan awal, kecapatan akhir, atau waktu.
- Masukkan variable-variable masing-masing untuk cari variable-nya.
- Hitung **hasilnya** automatis.
- Ada gambar yang saya buat sendiri **:D**

## 🛠 Teknologi

- **Python**: 3.13.2
- **[ttkbootstrap](https://ttkbootstrap.readthedocs.io/)**: v1.13.8 — tema modern untuk Tkinter.
- **Pillow (PIL)**: v10.4.0 — untuk membuka dan menampilkan gambar.

## 📂 Direktori
```
.
├── app_pj.py
├── README.md
├── requirements.txt
└── sppeedd.png
```

## 🚀 Cara Menjalankan

1. **Pastikan Python 3.13.2 sudah terinstal** di sistem.
2. **Aktifkan virtual environment/ opsional**:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows

2. **Install dependensi:**
    ```
    pip install -r requirements.txt
    ```

2. **Jalankan aplikasi:**
    ```
    python main.py
    ```


Pastikan input angka valid. Aplikasi akan menolak input kosong atau non-numerik.

📄 Lisensi
Proyek ini bebas digunakan untuk keperluan pembelajaran, tugas sekolah, atau pengembangan lebih lanjut. Tidak ada batasan lisensi khusus.

<!-- cmds :
pip freeze > requirements.txt
pip install -r requirements.txt
env_name/scripts/activate
deactivate -->
