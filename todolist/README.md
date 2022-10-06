# Deployment
[Heroku Link](https://pbp-tugas2-mrh.herokuapp.com/todolist/)

# Tugas 4
# Pertanyaan 
## Apa kegunaan {% csrf_token %} pada elemen form? 
CSRF token digunakan untuk menambahkans suatu keamanan ke dalam website. CSRF token bekerja dengan membandingkan suatu token, yang dibuat ketika merender suatu halaman, dengan token yang diterima ketika ada suatu HTTP request yang masuk. Dengan adanya CSRF token maka apabila token tidak sesuai, maka request tidak akan dijalankan. 

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
    
def logout_user(request):
    logout(request)
    return redirect('todolist:login_user')
```
### Poin 5
Membuat halaman utama pada pada web dengan code sebagai berikut
```
<div>
  <div class="header" style="text-align: center">
      <p>Hello {{username}}</p>
  </div>

  
 

  
  <table style="border:1px ;margin-left:auto;margin-right:auto;">
    {% if task_count > 0 %}
    <tr>
      <th>Date</th>
      <th>Task</th>
      <th>Description</th>
      <th>Status</th>

    </tr>
    {% endif %}

    {% if task_count == 0 %}
    <tr>
      <th>Belum ada task yang dibuat</th>
      

    </tr>
    {% endif %}


    {% comment %} Add the data below this line {% endcomment %}
    {% for todo in todolist %}
    <tr>
        <th>{{todo.date}}</th>
        <th>{{todo.title}}</th>
        <th>{{todo.description}}</th>
        <th>
          {% if todo.is_finished %}
          Selesai
          {% else %}
          Belum Selesai
          {% endif %}
        </th>
        
        <th>
          <button><a href="{% url 'todolist:change' todo.id %}" title="">Change Status</a></button>
          <button><a href="{% url 'todolist:delete' todo.id %}" title="">Delete</a></button>
        </th>
    </tr>
    {% endfor %}
  </table>
  
  <br>
  <div style="text-align: center">
    <button onclick="location.href='/todolist/create-task'">Create New Task</button>
    <button><a href="{% url 'todolist:logout_user' %}">Logout</a></button>
  </div>
    
</div>
```

### Poin 6
Membuat html yang menampilkan form untuk menambahkan Task baru.
```
{% extends 'base.html' %}

{% block meta %}
<title>Create New Todo List</title>
{% endblock meta %}

{% block content %}

<div class = "create">

    <h1>Add New Task</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Task:</td>
                <td><input type="text" name="task" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Description: </td>
                <td><input type="text" name="description" class="form-control"></td>
            </tr>
        </table>

        <input type="submit" name="submit" value="Add"/>
    </form>


</div>

{% endblock content %}
```

### Poin 7
Menambahkan routing untuk semua fungsi pada `views.py` ke dalam `urls.py` pada folder `todolist`


---

# Tugas 5
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline : kode CSS diletakkan dalam tag elemen HTML dengan atribut 'style'. 
Kelebihannya terdapat ketika ingin melakukan perubahan dapat dengan mudah dilakukan dan style dapat dengan mudah diuji coba. 
Kekurangannya adalah kurang efektif ketika menerapkan style yang sama ke elemen yang berbeda sehingga file HTML menjadi penuh dan kurang rapi
- Internal : kode CSS diletakkan dalam bagian `<head>` di file HTML dalam tag  `<style></style>`
Kelebihannya style dapat dengan mudah untuk diterapkan di suatu halaman HTML sehingga tidak bercampur-campur dengan HTML lain.
Kekurangannya yaitu ketika menambahkan kode CSS ke dalam file akan memperbesar ukuran memori dari HTML yang membuat melambatnya loading time.
- External : kode CSS diletakkan di file khusus .css dan dihubungkan ke file HTML dengan mencantumkan link atau file .css
Kelebihannya ialah kode CSS tersebut dapat digunakan untuk beberapa halaman HTML
Kekurangannya ketika ada perubahan, halaman HTML berpotensi tidak dapat dirender dengan benar.

## Jelaskan tag HTML5 yang kamu ketahui.
* ```<button>```: Membuat button
* ```<p>``` : Menambahkan text atau paragraf
* ```<b>```: Membuat text menjadi bold
* ```<br>```: Menambahkan break line
* ```<data>```: Me-link konten dengan terjemahan yang bisa dibaca mesin
* ```<form>```: Mendefinisikan form HTML untuk input user
* ```<html>```: Mendefinisikan root dokumen HTML

## Jelaskan tipe-tipe CSS selector yang kamu ketahui
* Selektor Tag dapat disebut sebagai type selector dan memiliki elemen berdasarkan nama tag.
* Selektor Class: Diberikan titik di depannya di nama elemen untuk selektor yang akan diberikan elemen 
* Selektor ID: Mirip dengan selektor Class, tetapi hanya dapat digunakan oleh satu elemen saja (unik) yang ditandai dengan tanda # didepannya.
* Selektor Atribut: Mirip dengan selektor Tag, selektor Atribut memiliki elemen berdasarkan atribut.
* Selektor Universal: Selektor yang digunakan untuk menyeleksi elemen pada scope tertentu
* Pseudo Selektor: Selektor untuk menyeleksi elemen-elemen semu seperti state dari suatu elemen, elemen before dan after, dsb. Terdapat 2 macam pseudo selektor, yaitu pseudo class selektor untuk state elemen dan pseudo-element selektor untuk elemen semu di HTML.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menambahkan styling terhadap semua file html, berupa border, background, font, alignment, dan lainnya.
2. Pada file todolist.html membuat card untuk menampilkan masing-masing task yang terdapat pada setiap akun.

