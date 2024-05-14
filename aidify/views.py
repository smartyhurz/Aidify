from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from aidify.models import post
from aidify.models import contact
from aidify.models import profile
from aidify.models import time
from . import views
from .models import post 
import datetime
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

 #de contact(request):
 #   return render(request,"contact.html")

def dele(request):
    return render(request,"delete.html")

def editprofile(request):
    return render(request,"editprofile.html")

def newpost(request):
    return render(request,"newpst.html")

def signup(request):
    return render(request,"signup.html")

def user(request):
    return render(request,"username.html")


def register(request):
  context={}
  if request.method == 'POST':
    username = request.POST["uname"]
    password=request.POST["upass"]
    confirmpass=request.POST["ucpass"]
    
    if username=="" or password=="" or confirmpass=="" :
      context['errmsg']="Fields cannot be empty"
      return render(request, "signup.html",context)
    else:
      u=User.objects.create(password=password,username=username,email=username)
      u.set_password(password) #hashing the password
      u.save()
      context['success']="Succesfully Registered"
      return render(request,'signup.html',context)
  else: 
     return render(request,'signup.html',context)
 
 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validate username and password are not empty
        if not username or not password:
            return render(request, 'login.html', {'error_message1': 'Email and password are required.'})

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication was successful
        if user is not None:
            login(request, user)
            # Redirect to a success page after login
            return redirect('/index')
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error_message': 'Invalid Email or password.'})
    else:
        return render(request, 'login.html')
    
    
def forse(request):
  #print(request.POST)
  if request.method=="GET":
    return render(request,"newpst.html")  
  else:
    recipename = request.POST['Rname']
    description = request.POST['desc']
    author = request.POST['cook']
    image = request.FILES.get('image')  # Access uploaded image
    
    print("Name is",recipename)
    print("Date of birth is",description)
    print("Phone Number is",author)
    
    m=post.objects.create(recipename=recipename,description=description,author=author,image=image)
    m.save()
    return redirect("/index")

def view_posts(request): 
    # Retrieve all posts from the database
    posts = post.objects.all()
    return render(request, 'index.html', {'posts': posts})    

def delete(request,rid):
  m=post.objects.get(id=rid)
  m.delete()
  return redirect("/d")
  
  
  
def cont(request):
  #print(request.POST)
  if request.method=="GET":
    return render(request,"contact.html")  
  else:
    name = request.POST['fname']
    mobile = request.POST['mobile']
    email = request.POST['email']
    address = request.POST['msg']
    
    
    print("Name is",name)
    print("Date of birth is",mobile)
    print("Phone Number is",email)
    print("Phone Number is",address)
    
    c = contact.objects.create(Name=name,Mobile=mobile,Email=email,Address=address)
    c.save()
    return redirect("/contact")



def pfp(request):
  #print(request.POST)
  if request.method=="GET":
    return render(request,"editprofile.html")  
  else:
    name = request.POST.get('name','')
    uname = request.POST.get('uname','')
    email= request.POST.get('email','')
    address = request.POST.get('address','')
    aboutme = request.POST.get('aboutme','')
    image = request.FILES.get('image')  # Access uploaded image
    
    p=profile.objects.create(name=name,uname=uname,email=email,address=address,aboutme=aboutme,image=image)
    p.save()
    return redirect("/user")

def view_user(request):
    # Retrieve all posts from the database
    pro = profile.objects.all()
    return render(request, 'username.html', {'pro': pro}) 
  
  
  
  
  
def search_results(request):
    query = request.GET.get('q')
    results = None

    if query:
        # Perform the search query on the post model
        results = post.objects.filter(recipename__icontains=query)  # Searching by recipe name

    return render(request, 'search.html', {'query': query, 'results': results})  
  
  
def view_post(request,post_id):
    Post = get_object_or_404(post, pk=post_id)
    return render(request, 'view_post.html', {'post': Post})  
  
  
  
  
def datetime(request,User_id):
    user= get_object_or_404(time,pk=User_id)
    date=time.objects.create(date=datetime)
    return render(request,'usertime.html',{ 'user': user}) 