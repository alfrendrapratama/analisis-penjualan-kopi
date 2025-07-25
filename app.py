from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Folder untuk gambar output
OUTPUT_FOLDER = os.path.join(app.root_path, 'outputs')

@app.route('/')
def index():
    # Daftar gambar visualisasi yang ingin ditampilkan
    images = [
        'correlation_heatmap.png',
        'sales_by_day-of_week.png',
        'sales_by_hour.png',
        'sales_by_month.png',
        'sales_by_products_category.png',
        'sales_by_store_location.png'
    ]
    return render_template('dashboard.html', images=images)

@app.route('/outputs/<filename>')
def output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)