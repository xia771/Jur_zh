from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User

def users(request):
    return HttpResponse("Hello World")

def shouye(request):
    return render(request, 'shouye.html')
def index(request):
    return render(request, 'index.html')

def user_rgb(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        hobbies = request.POST.get('hobbies')
        interests = request.POST.get('interests')

        if password != confirm_password:
            messages.error(request, '两次密码输入不一致，请重新输入')
            return redirect('user_rgb')

        User.objects.create(
            username=username,
            password=password,
            phone=phone,
            address=address,
            hobbies=hobbies,
            interests=interests
        )
        messages.success(request, "注册成功，请登录")
        return redirect('login')

    return render(request, 'zhuce.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                messages.success(request, "登录成功")
                return redirect('shouye')
            else:
                messages.error(request, "密码错误，请重试")
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "用户不存在，请先注册")

    return render(request, 'login.html')