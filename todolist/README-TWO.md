

## Assignment 6

[Heroku Link](https://pbp-tugas2-mrh.herokuapp.com/todolist/)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Pada synchronous programming, program akan berjalan secara sequential, yaitu ketika suatu perintah dieksekusi maka harus menunggu sampai perintah tersebut selesai dieksekusi. Sedangkan, pada asynchrinous programming, program tidak perlu menunggu suatu proses selesai terlebih dahulu. Dengan asynchronous programming
suatu program bisa mengeksekusi berbagai perintah secara bersamaan 


## Event-Driven Programming
Pada event-driven programming suatu program akan dieksekusi berdasarkan 'event' yang ada.Contohnya adalah ketika kita meng click suatu button 'Add Task' program akan menampilkan suatu modal untuk menambahkan task


## Jelaskan penerapan asynchronous programming pada AJAX.

Ketika terjadi sebuah event, maka AJAX akan dijalankan. Misalnya ketika mengklik button pada 'ADD TASK' untuk membuat task baru, maka yang terjadi adalah dilakukannya fungsi POST untuk mengirim data ke server. Setelah server selesai mengolah data tersebut, akan dijalankan callback function yang telah dibuat sebelumnya.

## Implementation

1. Membuat fungsi show_json pada views.py untuk return data yang dibuat oleh user 
2. Membuat fungsi add_task_ajax pada views.py dan menambahkannya ke routing pada file urls.py
3. Menyesuaikan html dengan fungsi baru yang telah dibuat
