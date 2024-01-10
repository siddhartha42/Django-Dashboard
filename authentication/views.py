from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import CustomUser 
from authentication.backends import CustomUserBackend
from django.contrib import messages
from django.contrib.auth import login, logout

def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        pfp = request.FILES.get('pic')

        if CustomUser.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('home')
        
        if CustomUser.objects.filter(email=email):
            messages.error(request, "Email already in use for other account")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "username must be under 10 characters")
            return redirect('home')
        
        if pass1!=pass2:
            messages.error(request, "passwords do not match")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "username can only contain alpha numberic characters")
            return redirect('home')
        
        user_type = request.POST['user_type'].lower()
        print(f"User type received: {user_type}")
        address_line1 = request.POST['line1']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        myuser=CustomUser.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.user_type=user_type
        myuser.address_line1=address_line1
        myuser.city=city
        myuser.state=state
        myuser.pincode=pincode
        myuser.profile_image=pfp

        myuser.save()
        print(f"User type saved: {myuser.user_type}")

        messages.success(request, "Your account has been created")

        return redirect('/login')

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = CustomUserBackend().authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            email = user.email
            user_type = user.user_type
            address=user.address_line1
            city=user.city
            state=user.state
            pincode=user.pincode
            pfp = user.profile_image 

            print(f"User type retrieved: {user.user_type}")
            return render(request, "authentication/index.html", {'fname': fname, 'lname':lname, 'user_type': user_type, 'email':email, 'address': address, 'city':city, 'state':state, 'pincode':pincode, 'pfp': pfp})
        else:
            messages.error(request, "Bad credentials")
            return redirect('home')

    return render(request, "authentication/login.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out")
    return redirect('home')
