from django.shortcuts import render
from world.models import users

# Create your views here.
def home(request):
    login =  'error'
    data = {
        'login' : login
    }
    return render(request, 'index.html', data)

def index(request, username):
    login =  'success'
    data = {
        'login' : login,
        'username': username
    }
    return render(request, 'index.html', data)

def changePassword(request, username):
    password = ''
    is_oldpassword = ''
    if request.method == 'POST':
        oldpassword = request.POST.get('old-password')
        newpassword = request.POST.get('new-password')
        record = users.objects.filter(username=username,password=oldpassword)

        for r in record:
            password = r.password
        
        if password == '':
            is_oldpassword = 'error'
        else:
            is_oldpassword = 'success'
            users.objects.filter(username=username).update(password=newpassword)

    data = {
        'is_password': is_oldpassword,
        'username':username
    }
    return render(request, 'change-password.html',data)

def logOut(request):
    login =  'error'
    data = {
        'login' : login
    }
    return render(request, 'index.html', data)

def map(request, username):
    data = {
        'username':username
    }
    return render(request, 'map.html', data)

def updateDetails(request, username):
    is_update = ''
    data = {
        'is_update':is_update,
        'username':username
    }
    return render(request, 'update-details.html', data)

def login(request):
    login = ''
    userName = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        record = users.objects.filter(username=username, password=password)
        
        userName = ''
        for r in record:
            userName = r.username
        
        if userName == "":
            login = 'error'
        else:
            login = 'success'

    data = {
        'login':login,
        'username': userName
    }
    return render(request, 'index.html', data)

def updateInfo(request, username):
    update = 'error'
    login = 'success'
    if request.method == 'POST':
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        email = request.POST.get('email')

        users.objects.filter(username=username).update(firstName=firstname, lastName=lastname, email=email)
        update = 'success'

    data = {
        'is_update':update,
        'login':login,
        'username':username
    }

    return render(request, 'update-details.html', data)

def signup(request):
    is_account = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            en = users(username = username, password = password, firstName = "", lastName = "", email = "" )
            en.save()
            is_account = 'success'
        except:
            is_account = 'error'
        
    data = {
        'username': 0,
        "is_account" : is_account
    }
    return render(request, 'sign-up.html', data)
