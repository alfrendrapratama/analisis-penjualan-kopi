# Analisis Penjualan dan Model Prediksi Kedai Kopi

Proyek ini bertujuan untuk menganalisis data penjualan dari sebuah kedai kopi untuk menemukan wawasan bisnis dan membangun model machine learning untuk memprediksi total nilai transaksi.

## 📁 Struktur Folder

## 📁 analisis-penjualan-kopi/

```
├── 📁 data/             (Berisi dataset mentah)
├── 📁 notebooks/        (Berisi file notebook analisis .ipynb)
├── 📁 outputs/          (Berisi semua hasil visualisasi .png)
├── 📄 .gitignore
├── 📄 LICENSE
├── 📄 Laporan-Final-Project_Penjualan-Kopi .docx
└── 📄 README.md
```

## 🛠️ Tools & Library
* Python
* Pandas
* Matplotlib & Seaborn
* Scikit-learn
* Jupyter Notebook / Google Colab

## 🚀 Cara Menjalankan Proyek
1. Clone repositori ini.
2. Pastikan semua library yang dibutuhkan sudah terinstal dengan menjalankan:
   `pip install pandas matplotlib seaborn scikit-learn`
3. Buka dan jalankan file notebook di dalam folder `notebooks/`.

## 📈 Temuan Kunci
* Puncak penjualan terjadi pada hari Senin dan akhir pekan, dengan jam sibuk pada pukul 08:00-10:00 dan 14:00-17:00.
* Kopi dan Teh adalah kategori produk terlaris.
* Model Regresi Linier yang dibangun berhasil memprediksi total penjualan dengan akurasi **R-squared 93.6%**.
