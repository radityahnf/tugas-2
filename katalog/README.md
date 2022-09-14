# TUGAS 2

### Deployment Link
---- [Heroku](https://pbp-tugas2-mrh.herokuapp.com/) ----
[Katalog](https://pbp-tugas2-mrh.herokuapp.com/katalog) ----

### Bagan
![Blank diagram (12)](https://user-images.githubusercontent.com/90910827/190218417-a9715656-483d-477a-aabf-9cfd699c3245.png)

User akan memberikan suatu request kepada URLs, kemudian akan diteruskan melalui views. Pada tahap ini, fungsi yang bersesuaian dengan request akan dipanggil. Kemudian views.py akan mengambil data dari models.py. Setelah itu, tahapan diakhiri dengan mengembalikan response yang kemudian akan dirender dan ditampilkan kepada client.

### Mengapa menggunakan virtual environment
Dengan menggunakan virtual environment, maka project yang sedang dikerjakan akan terisolasi dari project lain. Dengan menggunakan virtual environment packages serta dependencies yang digunakan tidak akan tercampur antar project. Sehingga penggunaannya akan berguna apabila terdapat beberapa project yang memerlukan package dengan version berbeda

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?



