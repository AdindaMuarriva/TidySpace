# TidySpace

TidySpace adalah website katalog dan pemesanan furniture modern berbasis Django.
Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Proyek Perangkat Lunak.

---

# ✨ Fitur Utama

* Katalog furniture modern
* Halaman detail produk
* Sistem keranjang belanja (cart)
* Pengaturan quantity produk
* Halaman checkout
* Integrasi pemesanan WhatsApp
* Tampilan UI modern & responsive
* Custom tampilan Django Admin
* Manajemen produk melalui admin panel

---

# 🛠 Tech Stack

* Python
* Django
* HTML5
* CSS3
* JavaScript
* SQLite

---

# 📂 Struktur Project

```bash
TidySpace/
│
├── katalog/
├── produk/
├── orders/
├── static/
├── templates/
├── media/
└── manage.py
```

---

# ⚙️ Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone https://github.com/AdindaMuarriva/TidySpace.git
cd TidySpace
```

---

## 2. Membuat Virtual Environment

```bash
python -m venv venv
```

---

## 3. Mengaktifkan Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependency

```bash
pip install -r requirements.txt
```

---

## 5. Jalankan Migration

```bash
python manage.py migrate
```

---

## 6. Membuat Superuser

```bash
python manage.py createsuperuser
```

---

## 7. Menjalankan Server

```bash
python manage.py runserver
```

Buka di browser:

```bash
http://127.0.0.1:8000
```

---

# 🛒 Alur Pemesanan

1. User melihat katalog produk
2. User menambahkan produk ke cart
3. User mengatur quantity produk
4. User menuju halaman checkout
5. User mengisi form checkout
6. Sistem membuat ringkasan pesanan
7. User diarahkan ke WhatsApp untuk konfirmasi pemesanan

---

# 🔑 Admin Panel

Halaman admin:

```bash
http://127.0.0.1:8000/admin
```

Admin dapat:

* Menambahkan produk
* Mengatur stok produk
* Mengubah harga produk

---

# 📸 Tampilan Sistem

### Home Page

Landing page modern dengan tampilan furniture premium minimalis.

### Product Catalog

Katalog produk dengan desain clean dan elegant.

### Cart & Checkout

Sistem cart sederhana dengan integrasi checkout WhatsApp.

---

