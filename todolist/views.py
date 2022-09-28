import datetime
from todolist.models import Task
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

def add_task(request):

    if request.method == 'POST':
        task = Task(
            title = request.POST.get('task'),
            description = request.POST.get('description'),
            date = datetime.datetime.now(),
            user = request.user,
            status = False)
        task.save()

        return redirect('todolist:show_todolist')
    
    return render(request, 'add_task.html')

def delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('todolist:show_todolist')

def change(request, pk):
    data = Task.objects.get(id=pk)
    data.status = not(data.status)
    data.save()
    return redirect('todolist:show_todolist')