from django.shortcuts import render,redirect
# required for login and logout
from django.contrib import messages
from django.contrib.auth.models import auth
from . import models
import random

operators = ['+','-','*']
alphanums = ['1','2','3','4','5','6','7','8','9','0','~','!','@','#','$','%','^','&','*','(',')','{','}','[',']','|',':',';','>','<','?','/','.']
# For Signup
def Signup(request):

    if request.method =='GET':
        # Send some random captcha
        captcha = str(random.randint(1, 10)) + random.choice(operators) + str(random.randint(1, 10))
        content = {
            'captcha':captcha
                    }
        return render(request,'accounts/signup.html',content)
    if request.method=='POST':
        # Receive the inputs
        username = request.POST['Username']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']
        answer = request.POST['answer']
        captcha = request.POST['captcha']

        # Check if the username already exists
        if models.Account.objects.filter(username = username).exists():
            messages.error(request,'Username already exists !')
            return redirect('users:Signup')

        # Check if the password are matching
        if Password1 != Password2:
            messages.error(request, 'Password do not match !')
            return redirect('users:Signup')

        # Check for captcha answer
        if eval(captcha) != int(answer):
            messages.error(request,'Your answer for captcha was wrong !')
            return redirect('users:Signup')

        # Check the strength of password
        if len(Password1)>7 and any(i in alphanums for i in Password1):
            new_user = models.Account(
                username = username
            )
            new_user.set_password(Password1)
            new_user.save()
            messages.success(request, 'You have successfully registered !')
            return redirect('users:login')
        else:
            messages.error(request, 'Please set a strong password !')
            return redirect('users:Signup')



#For Login
def Login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        # Check if the user exists
        if user is not None:
            # Login the user
            auth.login(request, user)
            return redirect('Blog:MyBlogs')
        # If the user does not exists
        else:
            messages.error(request, 'invalid username or password')
            return redirect('users:login')
    else:
        return render(request, 'accounts/login.html')

# For Logout
def Logout(request):
    auth.logout(request)
    return redirect('Blog:HomeView')
