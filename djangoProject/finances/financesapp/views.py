from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from financesapp.forms import SignUP,AddPostForm
from django.shortcuts import redirect
from django.contrib import messages 

from django.contrib.auth.decorators import login_required

# Auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Models 
from financesapp.models import Posts

def mainHome(request):
    
    return render(request, 'mainHome.html', context={})

def Loginn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        
        if not User.objects.filter(username=username).exists():
            
            messages.error(request, 'Algum dado está errado!')
            return redirect(Loginn)
        
      
        elif username.__len__() > 30 or password.__len__() > 30:
            messages.info(request, "Apenas 30 caracteres")
            return redirect(formvalid)
        
        
        user = authenticate(username=username, password=password)
         
        if user is None:
            
            messages.error(request, 'Algum campo está errado!')
            return redirect(Loginn)
        else:
            
            login(request, user)
            messages.info(request, f"{username} você está logado!")
            return redirect(HomePage)
     
    
    form = SignUP()
    return render(request, 'signIn.html', {'form':form})

@login_required
def HomePage(request):
    username = request.user.username
    users = User.objects.all()
    posts = Posts.objects.filter(author=username)
    
    form = AddPostForm()
    return render(request, 'HomePage.html', context={'user':username, 'form':form, 'posts':posts})

def Logout(request):
    logout(request)
    messages.error(request, "Logout sucessful!")
    return redirect(mainHome)

def formvalid(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
         
        
        user = User.objects.filter(username=username)
         
        if user.exists():
            
            messages.info(request, "Username already taken!")
            return redirect(formvalid)
        elif username.__len__() > 30 or password.__len__() > 30:
            messages.info(request, "Apenas 30 caracteres")
            return redirect(formvalid)
        form_cleaned = SignUP(request.POST)
        if form_cleaned.is_valid():
            user_cleaned = form_cleaned.cleaned_data['username']
            pass_cleaned = form_cleaned.cleaned_data['password']
            
            user = User.objects.create_user(
                password=password,
                username=username
            )
         
            
            user.set_password(password)
            user.save()
         
        
        messages.info(request, "Account created Successfully!")
        
        return redirect(mainHome)
     
    
    form = SignUP()
    return render(request, 'signUp.html', {'form':form})

@login_required
def AddPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.user.username;
        text = request.POST.get('text')
        form_post = AddPostForm(request.POST)
        if not Posts.objects.filter(title=title).exists() and form_post.is_valid():
        

            title_clean = form_post.cleaned_data['title']
            
            text_clean = form_post.cleaned_data['text']
            
            post = Posts.objects.create(
                title=title_clean,
                author=author,
                text=text_clean
            )
            post.save()
            messages.info(request,'Post adicionado!')
            
            return redirect(HomePage)
    messages.info(request, "Título já existe!")
    return redirect(HomePage)

@login_required
def DeletePost(request):
    if request.method == 'POST':
        user_session = request.user.username;
        title = request.POST.get('title')
        author = request.POST.get('author')

        
            
        if user_session == author:
            db1 = Posts.objects.filter(title=title)
            db1.delete()
            
            messages.info(request, 'Removido!')
            return redirect(HomePage)
        else:
            messages.info(request, 'Houve um erro!')
            return redirect(HomePage)
    return redirect(HomePage)

@login_required
def Post(request, id):
    user_session = request.user.username;
    print(id)
    
    Post = Posts.objects.get(id_p=id)

    return render(request, 'Post.html', context={'post':Post})
