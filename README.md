# stock-dashboard-
# 📊 Stock Dashboard Pro — News & Sector Driven

Dashboard interaktif untuk analisis saham berbasis harga, berita, dan sektor.  
Menggunakan data dari Yahoo Finance, visualisasi interaktif Streamlit, dan metrics saham penting.

---

## 1️⃣ Deskripsi Project
- Tujuan: Membantu investor memahami performa saham, hubungan dengan berita, dan perbandingan per sektor.
- Inovasi: Menggabungkan data harga saham, sentimen berita, dan informasi sektor untuk insight multi-dimensi.

---

## 2️⃣ Struktur Kode
| File | Fungsi |
|------|--------|
| `data_loader.py` | Download & preprocess data saham |
| `metrics.py` | Hitung return, sharpe ratio, beta, max drawdown, portfolio |
| `visualizations.py` | Fungsi plotting: harga, return, cumulative, korelasi |
| `utils.py` | Fungsi tambahan seperti scoring performa saham |
| `app.py` | Main Streamlit app, gabungkan semua module |
| `images/` | Screenshot dashboard untuk dokumentasi |

---

## 3️⃣ Fitur Dashboard
- Filter saham berdasarkan ticker dan rentang tahun
- Pilihan periode: Tahunan, Kuartalan, Mingguan
- Visualisasi harga saham, return log, cumulative return, korelasi antar saham
- Portfolio vs Benchmark (IHSG)
- Insight scoring: Overperform, Moderate, Underperform

---

## 4️⃣ Screenshot
![Tab Harga](images/tab_harga.png)
![Tab Return](images/tab_return.png)
![Tab Korelasi](images/tab_korelasi.png)

---

## 5️⃣ Instalasi & Run
1. Clone repo:
```bash
git clone https://github.com/username/stock-dashboard.git
cd stock-dashboard
