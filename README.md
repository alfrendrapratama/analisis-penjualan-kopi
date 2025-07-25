# Analisis Penjualan dan Model Prediksi Kedai Kopi

Proyek ini bertujuan untuk menganalisis data penjualan dari sebuah kedai kopi untuk menemukan wawasan bisnis dan membangun model machine learning untuk memprediksi total nilai transaksi.

## 📁 Struktur Folder
```
flask-dasboardCoffeVisual/
├── .gitignore
├── app.py
├── LICENSE.txt
├── Laporan-Final-Project_Penjualan-Kopi .docx
├── README.md
├── data/
│   ├── Coffee Shop Sales.csv
│   └── Coffee Shop Sales.xlsx
├── notebooks/
│   └── CoffeeShopSales_Final-Project.ipynb
├── outputs/
│   ├── correlation_heatmap.png
│   ├── sales_by_day-of_week.png
│   ├── sales_by_hour.png
│   ├── sales_by_month.png
│   ├── sales_by_products_category.png
│   └── sales_by_store_location.png
└── templates/
    └── dashboard.html
```

## 🛠️ Tools & Library
* Python
* Flask
* Pandas
* Matplotlib & Seaborn
* Scikit-learn
* Jupyter Notebook / Google Colab

## 🚀 Cara Menjalankan Proyek
1. Clone repositori ini.
2. Pastikan semua library yang dibutuhkan sudah terinstal dengan menjalankan:
   ```
   pip install flask pandas matplotlib seaborn scikit-learn
   ```
3. Untuk menjalankan dashboard Flask:
   ```
   python app.py
   ```
   Lalu buka browser ke `http://127.0.0.1:5000/`
4. Untuk eksplorasi analisis, buka dan jalankan file notebook di dalam folder `notebooks/`.

## 📈 Temuan Kunci
* Puncak penjualan terjadi pada hari Senin dan akhir pekan, dengan jam sibuk pada pukul 08:00-10:00 dan 14:00-17:00.
* Kopi dan Teh adalah kategori produk terlaris.
* Model Regresi Linier yang dibangun berhasil memprediksi total penjualan dengan akurasi **R-squared 93.6%**.

---

Lisensi:
