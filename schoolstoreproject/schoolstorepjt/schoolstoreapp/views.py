from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Faculties
from .models import Latestnews
from .models import Departments
from .models import Courses
from .models import Materials
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserForm


# Create your views here.

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create and save a UserProfile instance with the form data
            user_profile = UserProfile(
                name=form.cleaned_data['name'],
                dob=form.cleaned_data['dob'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                purpose=form.cleaned_data['purpose'],
                department=form.cleaned_data['department'],
                course=form.cleaned_data['course'],

            )
            user_profile.save()

            # For materials provided, you can add them to the user_profile
            for material in form.cleaned_data['materials_provided']:
                user_profile.materials_provided.add(material)

            # You can also display a message after saving the data
            messages.success(request, 'Order Confirmed')

            # Redirect to a success page or any other page as needed
            return redirect('orderconfirm')
    else:
        form = UserForm()

    return render(request, 'form.html', {'form': form})


def index(request):
    obj1 = Faculties.objects.all()
    obj2 = Latestnews.objects.all()
    obj3 = Departments.objects.all()
    obj4 = Courses.objects.all()
    obj5 = Materials.objects.all()
    return render(request, "index.html",
                  {'result1': obj1, 'result2': obj2, 'result3': obj3, 'result4': obj4, 'result5': obj5})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('User Created')
                return redirect('log')
        else:
            messages.info(request, "Password Mismatch")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('log')
    return render(request, 'log.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def newpage(request):
    return render(request, 'newpage.html')


def orderconfirm(request):
    return render(request, 'orderconfirm.html')


def user_profile(request, user_id):
    # Retrieve the user profile based on the user_id
    userprofile = UserProfile.objects.get(pk=user_id)

    # Pass the user profile to the template
    return render(request, 'userprofile.html', {'userprofile': userprofile})


def departments(request):
    return render(request, 'departments.html')


def courses(request):
    return render(request, 'courses.html')


def materials_provided(request):
    return render(request, 'materials_provided.html')
