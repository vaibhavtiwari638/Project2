from django.shortcuts import render,redirect
from django.http import HttpResponse
from Myapp.models import *
from .models import PatientProfile
from django.contrib.auth import authenticate , login , logout 
from django.db import connection

def index(request):
    user = request.session.get('user_data', None)
    allPosts= Post.objects.all()
    sr = {'user': user , 'allPosts': allPosts}
    return render(request,'blog/home.html' ,sr)
def login(request):
    return render(request,'blog/login.html')
def patient(request):
    return render(request,'blog/login2.html')

def add(request):
    return render(request,'blog/addpost.html')

def dsn(request):
        loginusername=request.POST['username'] 
        loginpassword=request.POST['password'] 
        users = DoctorProfile.objects.filter(username=loginusername, password=loginpassword)

        if users.exists():
                user = users.first()
                user = users.first()
                user_data = {
                    'username': user.username,
                    'email': user.email,
                    'type' :"doctor",
                    # Add other fields as needed
                }
                request.session['user_data'] = user_data
                # Successful login, you can add further logic here
                return render(request, 'blog/home.html', {'user': user})

        else:
                # Invalid credentials
                return HttpResponse("Login failed Invalid Credentials")
def dsp(request):
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      address_line1=request.POST['address_line1']
      city=request.POST['city']
      state=request.POST['state']
      pincode=request.POST['pincode']
      address=address_line1+" " + city+" " + state+" " + pincode 
      c = DoctorProfile(username=username , first_name= first_name,last_name=last_name,email=email,password=password,address=address)
      c.save()
      user_data = {
                    'username': username,
                    'email': email,
                    'type' :"doctor",
                    # Add other fields as needed
                }
      request.session['user_data'] = user_data
      return HttpResponse('done')

def psn(request):
    if request.method =='POST':
            loginusername=request.POST['username'] 
            loginpassword=request.POST['password'] 
            users = PatientProfile.objects.filter(username=loginusername, password=loginpassword)

            if users.exists():
                user = users.first()
                user_data = {
                    'username': user.username,
                    'email': user.email,
                    'type' :"patient",
                    # Add other fields as needed
                }
                request.session['user_data'] = user_data
                # Successful login, you can add further logic here
                return render(request, 'blog/home.html',{'user': user})

            else:
                # Invalid credentials
                return HttpResponse("Login failed Invalid Credentials")
            
def psp(request):
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      address_line1=request.POST['address_line1']
      city=request.POST['city']
      state=request.POST['state']
      pincode=request.POST['pincode']
      address=address_line1+" " + city+" " + state+" " + pincode 
      c = PatientProfile(username=username , first_name= first_name,last_name=last_name,email=email,password=password,address=address)
      c.save()
      user_data = {
                    'username': username,
                    'email': email,
                    'type' :"patient",
                    # Add other fields as needed
                }
      request.session['user_data'] = user_data
      return HttpResponse('done')

def logout(request):
    del request.session['user_data']
    return render(request,'blog/home.html')

    
def addpost(request):
     if request.method == 'POST':
        print(f"Received FILES: {request.FILES}")
        user_data = request.session.get('user_data', {})
        uname = user_data.get('username', None)
        title = request.POST['heading']
        image = request.FILES.get('image', None)
        print(f"Received image: {image}")
        content = request.POST['description']
        category = request.POST['category']
        author = request.POST['author_name']
        slug = request.POST['heading']  # Adjust as needed based on your requirements

        # Create a new Post instance and save it to the database
        Post.objects.create(
            uname=uname,
            title=title,
            image=image,
            category=category,
            content=content,
            author=author,
            slug=slug,
        )
     return HttpResponse("done")

def mypost(request):
    user = request.session.get('user_data', None)
    allPosts= Post.objects.all()
    sr = {'user': user , 'allPosts': allPosts}
    return render(request,'blog/mypost.html' ,sr)