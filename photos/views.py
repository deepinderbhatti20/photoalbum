from django.shortcuts import render,redirect
from photos.models import Category,Photo
from photos.forms import PhotoAddForm,UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Add Post
@login_required(login_url='signin')
def addpost(request):
    if request.method == 'POST':
        eform = PhotoAddForm(request.POST,request.FILES) 
        category_new = request.POST['category_new']
        if category_new != '' and eform.is_valid(): 
            categ, created = Category.objects.get_or_create(name=category_new)  
            new_photo=eform.save(commit=False)
            new_photo.category = categ
            new_photo.save()
            eform.save_m2m()
        elif eform.is_valid():
            eform.save()
        
        return redirect('gallery')     

    else:
        eform = PhotoAddForm()
        ctxt = {
            'form' : eform
        }
        return render(request, 'add.html', ctxt)


# View Gallery
@login_required(login_url='signin')
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photo = Photo.objects.all()
    else:
        photo = Photo.objects.filter(category__name=category)

    category = Category.objects.all() 
    ctxt = {
        'category' : category,
        'photo' : photo
    }
    return render(request, 'home.html', ctxt)


# View Photo
def viewphoto(request,pk):
    photo = Photo.objects.get(id=pk)
    ctxt = {
        'photo' : photo
    }
    return render(request, 'newviewphoto.html', ctxt)


# Register User
def register(request):
    if request.method == 'POST':
        eform = UserRegisterForm(request.POST)
        if eform.is_valid():
            new_user = eform.save()
            login(request,new_user)
            return redirect('gallery')
        else:
            ctxt = {
                'form':eform
            }
            return render (request,'newregister.html',ctxt)
    else:
        eform = UserRegisterForm()
        ctxt = {
            'form' : eform
        }
        return render (request, 'newregister.html', ctxt)

# Sign In
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('gallery')
        else:
            messages.info(request,'Please check Username or Password.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

# Sign Out
def signout(request):
    logout(request)
    return redirect('signin')

# About
def about(request):
    return render(request, 'about.html')
