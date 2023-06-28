from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from.models import Blog
from.forms import Edit_Blog

# Create your views here.
# def Index(request):
#     blog = Blog.objects.all()
#     context = {'blogs':blog}
#     return render(request, 'blog/index.html',  context)
def Index(request):
    content = Blog.objects.all()
    params = {'blogs':content}
    return render(request, 'blog/index2.html',  params)


def Register(request):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        password1 = request.POST.get('password')
        password2 = request.POST.get('cnf-password')
        if password1 !=password2:
            messages.warning(request, 'Sorry..! Password are not same...')
            return redirect('Register')
        else:
            if User.objects.filter(username = username).exists():
                messages.warning(request, 'Sorry..! Username is already taken...')
                return redirect('Register')

        user = User.objects.create_user(username, email, password1)
        user.save()
        messages.success(request, 'User Successfully Register...')
        return redirect ('Login')
    return render(request, 'blog/register.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Invalid credentials...")
            return redirect('Login')  
    return render(request, 'blog/login.html')
   


def Logout(request):
    logout(request)
    messages.success(request, "Successfully Logout...")
    return redirect('/')


def UploadPost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        excerpt = request.POST.get('excerpt')
        desc = request.POST.get('desc')
        img = request.FILE['images']
        user = request.user  # Get the current authenticated user
        blog = Blog(user_id=user, title=title, excerpt=excerpt, desc=desc, upload = img)
        blog.save()
        messages.success(request, "Post is successfully submitted.")
        return redirect("/")
    return render(request, 'blog/uploadpost.html')

def BlogDetail(request, id):
    blog = Blog.objects.get(id = id)
    contexet = {'blog': blog}
    return render (request, 'blog/detailpost.html', contexet)


def Delete(request, id):
    blog = Blog.objects.get(id =id)
    blog.delete()
    messages.success(request, "Post is deleted permanently")
    return redirect ('/')


def EditBlog(request, id):
    blog = Blog.objects.get(id =id)
    editblog = Edit_Blog(instance=blog)
    if request.method == "POST":
        form = Edit_Blog(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Post has been updated..")
            return redirect('/')
    return render(request, 'blog/edit.html', {'edit_blog':editblog})
