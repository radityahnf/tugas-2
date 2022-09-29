# Deployment
[Heroku Link](https://pbp-tugas2-mrh.herokuapp.com/todolist/)

# Pertanyaan 
## Apa kegunaan {% csrf_token %} pada elemen form? 

## Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Untuk membuat form, kita perlu memanfaatkan elemen `<table>`. Pada table tersebut kita dapat membuat field untuk user mengisi data yang kita inginkan dengan menggunakan `<input>` dan `<input type= 'submit'>` untuk mengirim data dari form yang telah diisi.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama user akan mengisi form dengan data yang sesuai. Kemudian ketika user menekan tombol dengan fungsi submit, maka akan dikirimkan suatu HTTP Request ke dalam server. Selanjutnya akan dijalankan fungsi untuk menambahkan data yang dibuat oleh user ke dalam database. Kemudian untuk menampilkan data sesuai yang diinginkan, maka pada hal ini akan dijalankan fungsi yang memfilter data sesuai user yang sedang login untuk ditampilkan ke dalam HTML.

## Implementasi checklist
### Poin 1
Menjalankan `py manage.py startapp todolist`.

### Poin 2
Menambahkan todolist ke dalam `urls.py` pada folder `project_django`.

### Poin 3
Membuat model `Task` pada `models.py` dengan atribut `user`, `date`, `title`, dan `description`.

### Poin 4
Membuat fungsi login, logout, register yang dihubungkan dengan html masing-masing. Kemudian menambahkan sebuah restriksi agar user harus melakukan login terlebih dahulu sebelum bisa mengakses fungsi lainnya.
```

@login_required(login_url='/todolist/login/')
def show_todolist(req):
    data_todolist = Task.objects.filter(user=req.user)
    task_count = data_todolist.count()
    username = req.user
    ctx = {
        'task_count' : task_count,
        'todolist':  data_todolist,
        'nama': 'Muhammad Raditya Hanif',
        'id': '2106750585',
        'username' : username
    }

    return render(req, "a.html", ctx)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
```
