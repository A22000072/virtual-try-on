
# Virtual Try-On

Virtual Try-On adalah aplikasi sederhana berbasis Python yang memungkinkan pengguna mencoba aksesoris virtual (seperti topi dan kacamata) secara real-time menggunakan webcam. Aplikasi ini menggunakan **OpenCV** dan **Mediapipe** untuk mendeteksi wajah dan menempatkan aksesoris virtual.

## 🚀 Fitur
- Deteksi wajah secara real-time menggunakan **Mediapipe**.
- Penempatan aksesoris virtual, seperti topi dan kacamata, pada wajah pengguna.
- Skalabilitas untuk menambahkan aksesoris lainnya.

## 🛠️ Teknologi yang Digunakan
- **Python 3.9+**
- **OpenCV**: Untuk pemrosesan gambar.
- **Mediapipe**: Untuk deteksi wajah.
- **NumPy**: Untuk manipulasi array.
- **Pillow**: Untuk manipulasi gambar dengan transparansi.

## 📂 Struktur Direktori
```
virtual-try-on/
├── assets/
│   ├── hat.png        # Gambar topi virtual
│   ├── glasses.png    # Gambar kacamata virtual
├── main.py            # Script utama
├── README.md          # Dokumentasi proyek
```

## 🧰 Instalasi dan Penggunaan

### 1. Clone Repository
Clone proyek ini ke komputer lokalmu:
```bash
git clone https://github.com/a22000072/virtual-try-on.git
cd virtual-try-on
```

### 2. Buat Virtual Environment
Gunakan virtual environment agar dependensi tetap terisolasi:
```bash
python3 -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate     # Untuk Windows
```

### 3. Instal Dependensi
Instal semua library yang diperlukan:
```bash
pip install opencv-python mediapipe numpy pillow
```

### 4. Jalankan Aplikasi
Jalankan script utama:
```bash
python3 main.py
```

## 🔧 Cara Kerja
1. Aplikasi membuka webcam dan mendeteksi wajah menggunakan **Mediapipe Face Detection**.
2. Setelah wajah terdeteksi, bounding box wajah digunakan untuk menentukan posisi topi dan kacamata virtual.
3. Gambar aksesoris virtual di-overlay pada frame webcam menggunakan **OpenCV** dengan mempertimbangkan transparansi (alpha channel).

## 🖼️ Contoh Output
Tambahkan gambar atau video GIF dari aplikasi saat berjalan:
![Contoh Output](https://via.placeholder.com/600x300.png?text=Contoh+Virtual+Try-On)

## 🚀 Pengembangan Lebih Lanjut
- **Menambahkan lebih banyak aksesoris**: Seperti masker, anting, atau rambut.
- **Deteksi tubuh penuh**: Untuk mencoba pakaian virtual (gunakan **Mediapipe Pose**).
- **Snapshot**: Tambahkan tombol untuk mengambil foto hasil try-on.
- **Web Deployment**: Integrasikan aplikasi ini ke dalam web menggunakan **Flask** atau **Streamlit**.

## 📝 Lisensi
Proyek ini menggunakan lisensi **MIT**. Silakan lihat file `LICENSE` untuk informasi lebih lanjut.

## 🤝 Kontribusi
Kontribusi sangat diterima! Jika kamu ingin menambahkan fitur atau melaporkan bug, silakan buat **pull request** atau buka **issue**.

## 📬 Kontak
Jika ada pertanyaan atau saran, hubungi saya melalui [GitHub](https://github.com/a22000072).
