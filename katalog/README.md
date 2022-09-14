# TUGAS 2

### Deployment Link
---- [Heroku](https://pbp-tugas2-mrh.herokuapp.com/) ----
[Katalog](https://pbp-tugas2-mrh.herokuapp.com/katalog) ----

## Bagan
![Blank diagram (12)](https://user-images.githubusercontent.com/90910827/190218417-a9715656-483d-477a-aabf-9cfd699c3245.png)

User akan memberikan suatu request kepada URLs, kemudian akan diteruskan melalui views. Pada tahap ini, fungsi yang bersesuaian dengan request akan dipanggil. Kemudian views.py akan mengambil data dari models.py. Setelah itu, tahapan diakhiri dengan mengembalikan response yang kemudian akan dirender dan ditampilkan kepada client.

## Virtual Environment
### Mengapa menggunakan virtual environment
Dengan menggunakan virtual environment, maka project yang sedang dikerjakan akan terisolasi dari project lain. Dengan menggunakan virtual environment packages serta dependencies yang digunakan tidak akan tercampur antar project. Sehingga penggunaannya akan berguna apabila terdapat beberapa project yang memerlukan package dengan version berbeda

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Ya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, apabila kita tidak menggunakan virtual environment, maka bisa saja terjadi perubahan yang tidak diinginkan, jika kita melakukan update terhadap packages atau dependencies yang digunakan pada projek Django.

## Implementasi Poin 1 - 4
### 1. views.py 
Pada file ini dibuat suatu fungsi bernama show_katalog yang menerima argument berupa request. Disini fungsi akan mengambil data yang disimpan pada database kemudian disimpan pada variabel context. Pada variabel ini juga ditambahkan atribut lain yaitu nama serta npm.

### 2. urls.py
Pada file ini ditambahkan sebuah routing terhadap katalog berupa path di urlpatterns dengan potongan kode berikut ('katalog/', include('katalog.urls')) pada folder product-django. 

### 3. Pemetaan data ke HTML (katalog.html)
Pada file ini ditambahkan {{nama}} serta {{npm}} yang diambil dari fungsi show_katalog. Kemudian pada file ini juga ditambahkan loop untuk menampilkan data dari list_katalog.

### 4. Deploy ke Heroku
Pada tahap ini dibuat aplikasi baru pada heroku. Kemudian dihubungkan dengan github melalui secrets yang ditambahkan HEROKU_APP_NAME dan HEROKU_API_KEY



