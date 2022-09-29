# Deployment
[Heroku Link](https://pbp-tugas2-mrh.herokuapp.com/todolist/)

# Pertanyaan 
## Apa kegunaan {% csrf_token %} pada elemen form? 

## Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Untuk membuat form, kita perlu memanfaatkan elemen `<table>`. Pada table tersebut kita dapat membuat field untuk user mengisi data yang kita inginkan dengan menggunakan `<input>` dan `<input type= 'submit'>` untuk mengirim data dari form yang telah diisi.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama user akan mengisi form dengan data yang sesuai. Kemudian ketika user menekan tombol dengan fungsi submit, maka akan dikirimkan suatu HTTP Request ke dalam server. Selanjutnya akan dijalankan fungsi untuk menambahkan data yang dibuat oleh user ke dalam database. Kemudian untuk menampilkan data sesuai yang diinginkan, maka pada hal ini akan dijalankan fungsi yang memfilter data sesuai user yang sedang login untuk ditampilkan ke dalam HTML.
